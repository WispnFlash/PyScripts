import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import os
import sys
import time

maindirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
investigator = str(sys.argv[1])
treatment = str(sys.argv[2])
mouse = str(sys.argv[3])
variablechoice = int(sys.argv[4])
timechoice = int(sys.argv[5])
xmin = int(sys.argv[6])
xmax = int(sys.argv[7])
xint = int(sys.argv[8])
ymin = int(sys.argv[9])
ymax = int(sys.argv[10])
yint = int(sys.argv[11])
color = str(sys.argv[12])
mouselocation = maindirectory + investigator + "/Data/Raw/" + treatment + "/" + mouse + ".txt"

def FindHeader(textfile):
	mouseText = open(textfile, "r")
	header = 0
	count = 0
	while(count < 100):
		current = mouseText.readline()
		if (current[1:11] == "Trial time"):
			header = count
			break
		count = count + 1
	mouseText.close()
	return header
	
start = time.time()
Header = FindHeader(mouselocation)
mouse = pd.read_csv(mouselocation, sep=";", header=Header, na_values=["-", "s", "s?", "cm", "cm?", "cm/s", "cm/s?"])
mouse = mouse.drop(mouse.index[[0]])
mouse = mouse.reset_index()
del mouse["index"]
elapsed = str(time.time()-start)
print("mouse loaded in " + elapsed + " seconds")

def Movement(mouseframe, timechoice, xmin, xmax, xint, ymin, ymax, yint, color):
	xsize = int(((xmax-xmin)+1)/xint)
	xvalues = np.array(range(xmin, xmax, xint*4))
	yvalues = np.array(range(ymin, ymax, yint))
	if (timechoice == 1):
		Time = np.array(range(xmin, xmax+1)).reshape(-1,1)
		Distance = np.zeros(xsize).reshape(-1,1)
		mouseMov = np.concatenate([Time, Distance], axis=1)
		mouseMov = pd.DataFrame(mouseMov)
		mouseMov.columns = ["Seconds", "Distance"]
		rangeStart = xmin
		rangeEnd = xmin + xint
		for i in range(0, xsize):
			mouseMov["Distance"][i] = mouseframe["Distance moved"][(mouseframe["Recording time"] > rangeStart) & (mouseframe["Recording time"] <= rangeEnd)].sum()
			rangeStart = rangeStart + xint
			rangeEnd = rangeEnd + xint
		plt.plot(mouseMov["Seconds"], mouseMov["Distance"], color)
		plt.title("Distance moved by Second")
		plt.ylabel("distance moved (cm)")
		plt.xlabel("seconds")
		"""plt.xticks(xvalues)"""
		plt.yticks(yvalues)
		plt.show()
		plt.clf()

		
if (variablechoice == 1):
	Movement(mouse, timechoice, xmin, xmax, xint, ymin, ymax, yint, color)

		