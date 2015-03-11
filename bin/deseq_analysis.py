#!/usr/bin/python

import csv
import sys

deseqFNs = ["../data/DESeq/fdr1_A431", "../data/DESeq/fdr1_U251", "../data/DESeq/fdr1_U2OS"]
cellLines = ["A431","U251","U2OS"]
geneSets = []
for deseqFN in deseqFNs:
  reader = csv.reader(open(deseqFN,'rb'), delimiter=' ', skipinitialspace=True)
  
  reader.next() # skip headers
  
  geneSets.append(set())
  for row in reader:
    if float(row[6]) > 0:
      geneSets[-1].add(row[1])
  
  with open(deseqFN + "_high_in_cyto.txt",'w') as f:
    for gene in sorted(list(geneSets[-1])):
      f.write(gene + '\n')

totalIntersection = geneSets[0].intersection(geneSets[1]).intersection(geneSets[2])
totalUnion = geneSets[0].union(geneSets[1]).union(geneSets[2])
print "Intersection of all gene sets:", len(totalIntersection), "(union:", str(len(totalUnion)) + ")"

with open("../data/DESeq/fdr1_union_high_in_cyto.txt",'w') as f:
  for gene in sorted(list(totalUnion)):
    f.write(gene + '\n')

with open("../data/DESeq/fdr1_intersection_high_in_cyto.txt",'w') as f:
  for gene in sorted(list(totalIntersection)):
    f.write(gene + '\n')
    
if True:
  for i, geneSet in enumerate(geneSets):
    for j in range(i+1, len(geneSets)):
      intersection = geneSet.intersection(geneSets[j])
      union = geneSet.union(geneSets[j])
      print "Intersection of", cellLines[i], "and", cellLines[j], ":", len(intersection), "(union:", str(len(union)) + ")"
  
