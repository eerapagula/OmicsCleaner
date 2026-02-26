#!/usr/bin/env python3

import click
from Bio import SeqIO
from Bio.Seq import Seq
import pandas as pd
import re
import os

def clean_sequence(seq):
    """Remove illegal characters and normalize sequence"""
    seq = str(seq).upper()
    seq = re.sub(r'[^A-Z*]', '', seq)
    return seq

@click.command()
@click.argument("input_fasta")
@click.option("--prefix", default="GENE", help="Prefix for renamed IDs")
@click.option("--minlen", default=50, help="Minimum allowed sequence length")
@click.option("--outdir", default="output", help="Output directory")
def main(input_fasta, prefix, minlen, outdir):

    os.makedirs(outdir, exist_ok=True)

    cleaned_fasta = os.path.join(outdir, "cleaned.fasta")
    mapping_file = os.path.join(outdir, "id_mapping.tsv")
    stats_file = os.path.join(outdir, "stats.txt")
    duplicate_file = os.path.join(outdir, "duplicates.txt")

    seen_sequences = {}
    mapping = []
    duplicates = []

    total = 0
    kept = 0
    lengths = []

    with open(cleaned_fasta, "w") as out_fasta:
        for record in SeqIO.parse(input_fasta, "fasta"):

            total += 1
            seq = clean_sequence(record.seq)

            if len(seq) < minlen:
                continue

            if seq in seen_sequences:
                duplicates.append(record.id)
                continue

            new_id = f"{prefix}_{kept+1:06d}"
            seen_sequences[seq] = new_id

            mapping.append([record.id, new_id, len(seq)])

            record.id = new_id
            record.description = ""
            record.seq = Seq(seq)

            SeqIO.write(record, out_fasta, "fasta")

            kept += 1
            lengths.append(len(seq))

    # mapping table
    pd.DataFrame(mapping, columns=["Old_ID", "New_ID", "Length"]).to_csv(mapping_file, sep="\t", index=False)

    # duplicates
    with open(duplicate_file, "w") as f:
        for d in duplicates:
            f.write(d + "\n")

    # statistics
    with open(stats_file, "w") as f:
        f.write(f"Total_sequences\t{total}\n")
        f.write(f"Kept_sequences\t{kept}\n")
        f.write(f"Removed_duplicates\t{len(duplicates)}\n")
        if lengths:
            f.write(f"Min_length\t{min(lengths)}\n")
            f.write(f"Max_length\t{max(lengths)}\n")
            f.write(f"Average_length\t{sum(lengths)/len(lengths):.2f}\n")

    print("\nOmicsCleaner finished successfully")
    print(f"Clean FASTA: {cleaned_fasta}")
    print(f"Mapping table: {mapping_file}")
    print(f"Statistics: {stats_file}")

if __name__ == "__main__":
    main()
