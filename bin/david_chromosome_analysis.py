#!/usr/bin/python

import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

inputFolder = "../results/150318_DAVID_chromosome_stats/"
cellLines = ["U251","A431","U2OS"]

highIn = "cyto"

def getBackgroundGeneDist():
  #return [0.090,0.069,0.053,0.044,0.049,0.050,0.050,0.041,0.039,0.038,0.056,0.050,0.023,
  #        0.038,0.037,0.041,0.051,0.019,0.049,0.024,0.015,0.023,0.041,0.010,0.0]
  return [0.102,0.064,0.053,0.037,0.043,0.051,0.048,0.033,0.038,0.036,0.065,0.051,0.016,
          0.040,0.030,0.043,0.059,0.013,0.072,0.027,0.012,0.024,0.040,0.004,0.0]
          
def getChromKey(key):
  if key == "Y":
    return 24
  elif key == "X":
    return 23
  elif key == "Un":
    return 25
  else:
    return int(key)

ax = plt.subplot(111, polar = True)
colors = [plt.cm.summer(0.0),plt.cm.summer(0.3),plt.cm.summer(0.6)]
#fig, ax = plt.subplots()
bgCounts = [list() for x in range(25)]
for idx, highIn in enumerate(["total", "cyto"]):
  catCounts = []
  cats = []
  for i, cellLine in enumerate(cellLines):
    davidFile = os.path.join(inputFolder, cellLine + "_high_in_" + highIn + ".txt")
    reader = csv.reader(open(davidFile,'rb'), delimiter='\t')
    reader.next()
    for row in reader:
      cat = row[1]
      count = float(row[3])/100
      bg = count/float(row[9])
      bgCounts[getChromKey(cat)-1].append(bg)
      if float(row[-2]) < 0.01:
        print highIn, cellLine, cat, row[-2]
      if cat not in cats:
        cats.append(cat)
        catCounts.append([0,0,0])
      catCounts[cats.index(cat)][i] = count

  catCounts = [x for (y,x) in sorted(zip(map(getChromKey, cats),catCounts), reverse = False)]
  cats = [x for (y,x) in sorted(zip(map(getChromKey, cats),cats), reverse = False)]
  
  #ind = np.arange(len(cats))
  ind = np.linspace(0.0, 2 * np.pi, len(cats), endpoint=False)
  width = ind[1]/3

  plt.bar(ind + width/2 + idx*width, [np.mean(count) for count in catCounts], width, color = colors[idx], yerr = [np.std(count) for count in catCounts], ecolor = colors[idx+1], capsize = 2)
  #for i, cellLine in enumerate(cellLines):
  #  plt.bar(ind+i*width, [mult*count[i] for count in catCounts], width, color = colors[i])

bgDist = [np.mean(counts) for counts in bgCounts]
plt.bar(ind, bgDist, width = ind[1], color = colors[2], alpha = 0.4)
#plt.ylabel('Percentage of DE genes', fontsize = 28)
#plt.xlabel('Chromosome', fontsize = 28)

# a is an axes object, from figure.get_axes()

# Hide major tick labels
ax.xaxis.set_major_locator(ticker.FixedLocator(ind))
ax.xaxis.set_major_formatter(ticker.NullFormatter())

# Customize minor tick labels
ax.xaxis.set_minor_locator(ticker.FixedLocator(ind + width*1.5))
ax.xaxis.set_minor_formatter(ticker.FixedFormatter(cats))
for tick in ax.xaxis.get_minor_ticks():
  tick.label.set_fontsize(20)

ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")
ax.set_rgrids(np.arange(0.05,0.20,0.05), angle = 0, ha = "right", fontsize = 14)

#plt.yticks(np.arange(0,0.20,0.05), fontsize = 14)
#plt.tick_params(axis='both', which='major', labelsize=20)
#ax.set_xticklabels(cats)
#ax.get_yaxis().set_visible(False)

plt.legend(["Total", "Cyto", "Bg"], loc='center', fontsize = 20)
#plt.tight_layout()
plt.grid(True)
plt.xlim([-1*width, len(cats)])
plt.ylim([-0.07, 0.15])
plt.show()
