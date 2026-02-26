# OmicsCleaner

**OmicsCleaner** is a small command-line utility for cleaning and standardizing FASTA files generated from genome and transcriptome projects.

During RNA-seq assemblies, ORF prediction, or annotation workflows, FASTA files often contain duplicate sequences, inconsistent identifiers, strange characters, or very short fragments. These small issues quietly break downstream tools such as BLAST database creation, TransDecoder, primer design, gene expression matching, and network analysis.

This program prepares sequences so they can be used reliably in downstream bioinformatics analysis.

---

## What problem does this solve?

Most genomics pipelines assume that sequence identifiers are clean and unique.
In reality, assembly outputs usually look like this:

* headers with spaces or symbols
* multiple transcripts having identical sequences
* IDs changing between tools
* short fragments included with real genes
* invalid characters inside sequences

Because of this:

* BLAST databases fail to build
* annotation tools cannot map genes
* WGCNA drops genes due to mismatched IDs
* downstream analyses become difficult to reproduce

OmicsCleaner fixes these issues automatically and produces a consistent dataset ready for analysis.

---

## What the tool does

OmicsCleaner will:

* remove duplicate sequences
* rename sequence IDs in a consistent format
* remove problematic characters
* filter very short sequences
* generate a mapping between old IDs and new IDs
* produce basic statistics of the dataset

The cleaned FASTA file can be directly used for BLAST, functional annotation, expression analysis, or comparative genomics.

---

## Installation

Clone the repository:

```
git clone https://github.com/eerapagula/OmicsCleaner.git
cd OmicsCleaner
```

Create a conda environment:

```
conda create -n omicscleaner python=3.10 -y
conda activate omicscleaner
```

Install dependencies and the tool:

```
pip install -r requirements.txt
pip install -e .
```

---

## Usage

Basic run:

```
omicscleaner input.fasta
```

Typical use:

```
omicscleaner transcripts.fasta --prefix AMAR --minlen 100 --outdir cleaned_data
```

### Options

| Option      | Meaning                                       |
| ----------- | --------------------------------------------- |
| input.fasta | Input FASTA file                              |
| --prefix    | Prefix used for renamed IDs (default: GENE)   |
| --minlen    | Minimum sequence length to keep (default: 50) |
| --outdir    | Output directory (default: output)            |

---

## Output

The program creates four files:

**cleaned.fasta**
Final cleaned sequences with standardized identifiers

**id_mapping.tsv**
Table connecting original IDs to new IDs

**duplicates.txt**
Sequences removed because they were identical to another entry

**stats.txt**
Basic statistics such as number of sequences and length distribution

---

## Example

Input FASTA:

```
>transcript|abc 1
ATGCGTAGCTAGCTAGCTAGCTAGCTAG

>duplicate_seq
ATGCGTAGCTAGCTAGCTAGCTAGCTAG
```

After running OmicsCleaner:

```
>GENE_000001
ATGCGTAGCTAGCTAGCTAGCTAGCTAG
```

---

## When should you use this?

This tool is useful before:

* building a BLAST database
* running TransDecoder
* functional annotation pipelines
* WGCNA or expression studies
* comparative genomics analysis
* primer or marker development

---

## Citation

If this tool is useful in your research, please cite:

Ramesh Eerapagula, *OmicsCleaner: FASTA preprocessing tool for genomics datasets*, GitHub repository.

---

## Author

Ramesh Eerapagula
Computational Biology and Genomics Researcher

