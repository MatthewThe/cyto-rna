#!/usr/bin/python

import os
import csv
import matplotlib.pyplot as plt
import numpy as np

inputFolder = "../results/150318_DAVID_chromosome_stats/"
cellLines = ["A431","U2OS","U251"]

catCounts = []
cats = []

davidFile = os.path.join(inputFolder, "DAVID.tsv")
reader = csv.reader(open(davidFile,'rb'), delimiter='\t')
reader.next()
reader.next()
esVector = {}
for row in reader:
  mainCat = row[0]
  subCat = row[1]
  if mainCat not in esVector:
    esVector[mainCat] = {}
  esVector[mainCat][subCat] = [float(es) if len(es) > 0 else 0.0 for es in row[2:]]

for mainCat in esVector:
  print mainCat
  fig, ax = plt.subplots()
  subCats = esVector[mainCat].keys()
  
  ind = np.arange(len(subCats))
  width = 0.25
  colors = [plt.cm.summer(0.0),plt.cm.summer(0.3),plt.cm.summer(0.6)]

  for i in range(6):
    if i % 2 == 0:
      mult = 1
    else:
      mult = -1
    plt.bar(ind+(i%3)*width, [mult*esVector[mainCat][subCat][i] for subCat in esVector[mainCat]], width, color = colors[i % 3])

  plt.ylabel('DAVID Enrichment score', fontsize = 28)
  plt.xticks(ind+1.5*width, fontsize = 20)
  plt.tick_params(axis='both', which='major', labelsize=16)
  ax.set_xticklabels(subCats, rotation=45, ha = "right")
  plt.title(mainCat, fontsize = 28)
  plt.legend(cellLines, loc='best', fontsize = 24)
  plt.tight_layout()
  plt.grid()
  plt.plot([-1*width, len(subCats)],[0, 0], color = 'k')
  plt.xlim([-1*width, len(subCats)])
  plt.ylim([-25, 25])
  
plt.show()
