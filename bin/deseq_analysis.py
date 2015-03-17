#!/usr/bin/python

import csv
import sys

deseqFNs = ["../data/DESeq/fdr1_A431.txt", "../data/DESeq/fdr1_U251.txt", "../data/DESeq/fdr1_U2OS.txt"]
cellLines = ["A431","U251","U2OS"]

def getBaseFN(filename):
  return ".".join(filename.split(".")[:-1])


for highIn in ["cyto","total"]:
  print "DE genes, high in", highIn
  geneSets = []
  for i, deseqFN in enumerate(deseqFNs):
    reader = csv.reader(open(deseqFN,'rb'), delimiter=' ', skipinitialspace=True)
    
    reader.next() # skip headers
    
    geneSets.append(set())
    for row in reader:
      if (float(row[6]) > 0 and highIn == "cyto") or (float(row[6]) < 0 and highIn == "total"):
        geneSets[-1].add(row[1])
    
    with open(getBaseFN(deseqFN) + "_high_in_" + highIn + ".txt",'w') as f:
      count = 0
      for gene in sorted(list(geneSets[-1])):
        f.write(gene.split('.')[0] + '\n')
        count += 1
      print cellLines[i] + ":", count

  totalIntersection = geneSets[0].intersection(geneSets[1]).intersection(geneSets[2])
  totalUnion = geneSets[0].union(geneSets[1]).union(geneSets[2])
  print "Intersection of all gene sets:", len(totalIntersection), "(union:", str(len(totalUnion)) + ")"

  with open("../data/DESeq/fdr1_union_high_in_" + highIn + ".txt",'w') as f:
    for gene in sorted(list(totalUnion)):
      f.write(gene.split('.')[0] + '\n')

  with open("../data/DESeq/fdr1_intersection_high_in_" + highIn + ".txt",'w') as f:
    for gene in sorted(list(totalIntersection)):
      f.write(gene.split('.')[0] + '\n')
      
  if True:
    for i, geneSet in enumerate(geneSets):
      for j in range(i+1, len(geneSets)):
        intersection = geneSet.intersection(geneSets[j])
        union = geneSet.union(geneSets[j])
        print "Intersection of", cellLines[i], "and", cellLines[j], ":", len(intersection), "(union:", str(len(union)) + ")"
  
