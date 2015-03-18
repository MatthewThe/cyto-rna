#!/usr/bin/python

import os
import csv
import matplotlib.pyplot as plt
import numpy as np

inputFolder = "../results/150311_DESeq_result_analysis/"
cellLines = ["U251","A431","U2OS"]

#feature = "molecular_function"
#feature = "biological_process"
feature = "protein_class"
highIn = "cyto"

catCounts = []
cats = []
for i, cellLine in enumerate(cellLines):
  pantherFile = os.path.join(inputFolder, feature + "_" + cellLine + "_high_" + highIn + ".txt")
  reader = csv.reader(open(pantherFile,'rb'), delimiter='\t')
  for row in reader:
    cat = " ".join(row[1].split(" ")[:-1]).replace("transcription factor","tf").replace("activity","act.")[:25]
    count = int(row[2])
    if cat not in cats:
      cats.append(cat)
      catCounts.append([0,0,0])
    catCounts[cats.index(cat)][i] = count

catCounts = [x for (y,x) in sorted(zip([sum(cnts) for cnts in catCounts],catCounts), reverse = True)]
cats = [x for (y,x) in sorted(zip([sum(cnts) for cnts in catCounts],cats), reverse = True)]
ind = np.arange(len(cats))
width = 0.25
colors = ['r','b','g']
fig, ax = plt.subplots()
for i, cellLine in enumerate(cellLines):
  plt.bar(ind+i*width, [count[i] for count in catCounts], width, color = colors[i])
plt.ylabel('Counts')
plt.title(feature + ' category count with higher expression in ' + highIn)
plt.xticks(ind+1.5*width)
ax.set_xticklabels(cats, rotation=90)

plt.legend(cellLines, loc='best')
plt.tight_layout()
plt.grid()
plt.xlim([-1*width, len(cats)])
plt.show()
