#!/usr/bin/python

import os
import csv
import matplotlib.pyplot as plt
import numpy as np

inputFolder = "../results/150318_DAVID_chromosome_stats/"
cellLines = ["U251","A431","U2OS"]

highIn = "cyto"

def getChromKey(key):
  if key == "Y":
    return 24
  elif key == "X":
    return 23
  elif key == "Un":
    return 25
  else:
    return int(key)

fig, ax = plt.subplots()
for idx, highIn in enumerate(["cyto", "total"]):
  catCounts = []
  cats = []
  for i, cellLine in enumerate(cellLines):
    davidFile = os.path.join(inputFolder, cellLine + "_high_in_" + highIn + ".txt")
    reader = csv.reader(open(davidFile,'rb'), delimiter='\t')
    reader.next()
    for row in reader:
      cat = row[1]
      count = float(row[3])/100
      if cat not in cats:
        cats.append(cat)
        catCounts.append([0,0,0])
      catCounts[cats.index(cat)][i] = count

  cats = [x for (y,x) in sorted(zip(map(getChromKey, cats),cats), reverse = False)]
  catCounts = [x for (y,x) in sorted(zip(map(getChromKey, cats),catCounts), reverse = False)]
  ind = np.arange(len(cats))
  width = 0.25
  colors = [plt.cm.summer(0.0),plt.cm.summer(0.3),plt.cm.summer(0.6)]
  
  if idx == 0:
    mult = 1
  else:
    mult = -1
  for i, cellLine in enumerate(cellLines):
    plt.bar(ind+i*width, [mult*count[i] for count in catCounts], width, color = colors[i])

plt.ylabel('Percentage of DE genes', fontsize = 28)
plt.xlabel('Chromosome', fontsize = 28)
plt.xticks(ind+1.5*width, fontsize = 20)
plt.tick_params(axis='both', which='major', labelsize=20)
ax.set_xticklabels(cats, rotation=90)

plt.legend(cellLines, loc='best', fontsize = 24)
#plt.tight_layout()
plt.grid()
plt.xlim([-1*width, len(cats)])
plt.ylim([-0.15, 0.15])
plt.show()
