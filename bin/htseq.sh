#!/bin/sh

samtools view $1/$1.outputAligned.sortedByCoord.out.bam -o $1/samfile.sam

htseq-count -m intersection-strict -s no -t exon -i gene_id $1/samfile.sam gencode.v21.chr_patch_hapl_scaff.annotation.gtf > htseq_count_$1.txt

rm $1/samfile.sam
