# OmicsCleaner

OmicsCleaner is a command-line bioinformatics tool designed to clean and standardize FASTA sequence files from genomics and transcriptomics datasets before downstream analysis.

Modern sequencing assemblies (RNA-seq transcriptomes, genome annotations, ORF predictions) frequently contain:
- duplicate sequences
- inconsistent headers
- invalid characters
- very short fragments
- problematic IDs that break BLAST, TransDecoder, WGCNA and annotation pipelines

OmicsCleaner automatically fixes these issues and produces a ready-to-analyze dataset.

---

## Why this tool is needed

Many downstream tools fail due to messy FASTA headers:

Examples:
- BLAST database creation fails
- TransDecoder cannot map transcripts
- MISA primer design crashes
- Gene expression tools cannot match IDs
- WGCNA loses genes due to inconsistent identifiers

OmicsCleaner standardizes sequences so they are compatible with downstream genomics workflows.

---

## Features

• Removes duplicate sequences  
• Renames sequence IDs systematically  
• Removes illegal characters (N, spaces, symbols)  
• Filters short sequences  
• Generates dataset statistics  
• Creates ID mapping table (old ID → new ID)  
• Ready for BLAST / annotation / WGCNA / phylogeny

---

## Installation

Clone the repository:
git clone https://github.com/eerapagula/OmicsCleaner.git
cd OmicsCleaner
# Create environment:
conda create -n omicscleaner python=3.10 -y
# activate environment
conda activate omicscleaner
# Install dependencies
pip install -r requirements.txt
pip install -e .
# Usage
omicscleaner input.fasta
# with options
omicscleaner input.fasta --prefix ER --minlen 100 --outdir results


### Parameters

| Parameter | Description |
|----------|------------|
| input.fasta | input FASTA file |
| --prefix | prefix for renamed IDs (default: GENE) |
| --minlen | minimum sequence length (default: 50) |
| --outdir | output directory (default: output) |

---

## Output Files

The program creates:

**cleaned.fasta**
Cleaned sequences with standardized IDs

**id_mapping.tsv**  
Mapping between original IDs and new IDs

**duplicates.txt**  
List of removed duplicate sequences

**stats.txt**  
Dataset statistics (counts and length distribution)

---

## Typical Applications

• RNA-seq transcriptome preprocessing  
• Genome annotation cleanup  
• Preparing BLAST databases  
• Preparing sequences for WGCNA  
• Functional annotation pipelines  
• Comparative genomics datasets

---

## Citation

If you use this tool in research, please cite:

Ramesh Eerapagula. OmicsCleaner: FASTA preprocessing tool for genomics datasets. GitHub repository.

---

## Author
Ramesh Eerapagula  
Computational Biology / Genomics Research
