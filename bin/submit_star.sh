#!/bin/bash

echo "Processing FASTQ files with STAR"
for fastq in /proj/g2015009/cytoplasm/raw_data/*.fastq.gz
do
  tmp=${fastq%%.fastq.gz}
  base=${tmp##*/}
  echo "  Submitting $base ..."

	sbatch -A g2015009 -t 2:00:00 -p node -n 8 -o sbatch_star_${base}.out sbatch_star.sh ${base}
done
echo "DONE"


