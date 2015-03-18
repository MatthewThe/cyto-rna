#!/usr/bin/python

import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

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
      bottom = 0
    else:
      bottom = -25
    plt.bar(ind + width/2 + (i%3)*width, [esVector[mainCat][subCat][i] for subCat in esVector[mainCat]], width, bottom = bottom, color = colors[i % 3])

  plt.ylabel('DAVID Enrichment score', fontsize = 28)
  # Hide major tick labels
  ax.xaxis.set_major_locator(ticker.FixedLocator(ind))
  ax.xaxis.set_major_formatter(ticker.NullFormatter())

  # Customize minor tick labels
  ax.xaxis.set_minor_locator(ticker.FixedLocator(ind + 0.7))
  ax.xaxis.set_minor_formatter(ticker.FixedFormatter(subCats))
  
  ax.yaxis.set_major_locator(ticker.FixedLocator([-25, -15, -5, 0, 10, 20]))
  ax.yaxis.set_major_formatter(ticker.FixedFormatter([0, 10, 20, 0, 10, 20]))
  
  ax.text(0.1, 22, "Total", fontsize = 20, va = "center", bbox={'facecolor':'white', 'pad':10})
  ax.text(0.1, -3, "Cyto", fontsize = 20, va = "center", bbox={'facecolor':'white', 'pad':10})
  for tick in ax.xaxis.get_minor_ticks():
    tick.label.set_fontsize(20)
    tick.label.set_rotation(45)
    tick.label.set_ha("right")
  #plt.xticks(ind+1.5*width, fontsize = 20)
  #plt.tick_params(axis='both', which='major', labelsize=16)
  #ax.set_xticklabels(subCats, rotation=30, ha = "right")
  plt.title(mainCat, fontsize = 28)
  if mainCat == "Proteins":
    plt.legend(cellLines, loc='lower right', fontsize = 24)
  #plt.tight_layout()
  plt.grid()
  plt.plot([0, len(subCats)],[0, 0], color = 'k')
  plt.plot([0, len(subCats)],[-25, -25], color = 'k')
  plt.xlim([0, len(subCats)])
  plt.ylim([-25, 25])
  fig.subplots_adjust(bottom=0.4)
  
plt.show()
