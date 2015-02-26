#!/bin/bash
# This is the template sbatch script for Lab3 at BB2490 spring 2015

# Run the script like this:
# sbatch <OPTIONS> sbatch_template.sh
# Where the OPTIONS are all of:
# -A g2015009 -t 2:00:00 -p node -n 8 -o sbatch_star.out
#
# sbatch -A g2015009 -t 2:00:00 -p node -n 8 -o sbatch_star.out sbatch_star.sh
#
# You may change the job name (-o my_job_name.out) to anything you like.

# Any line that starts with '# ' (dash followed by space) is a comment and will not be executed

# First add the modules needed for the program(s) your're about to run:
# bioinfo-tools
# bwa/0.5.9 
# samtools
# BEDTools
# python
# tophat/1.2.0  (we need to specify the tophat version since the default version at Uppmax is obsolete)
# bowtie
# htseq
module add bioinfo-tools
module add star

base=$1
# cd to the directory where the data is (of course, use your own user name):
mkdir -p /glob/matth/cyto-rna/data/STAR/${base}
cd /glob/matth/cyto-rna/data/STAR/${base}

STAR --genomeDir /glob/matth/GRCh38_Gencode21/ --runThreadN 8 --readFilesIn /proj/g2015009/cytoplasm/raw_data/${base}.fastq.gz --outFileNamePrefix ${base}.output --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate > ${base}.log 2>&1
