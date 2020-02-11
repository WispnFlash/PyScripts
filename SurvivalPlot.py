import pandas as pd
import numpy as np
import multiprocessing as mp
import os
from matplotlib import pyplot as plt
import sys

maindirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
investigator = str(sys.argv[1])
numberofgroups = int(sys.argv[2])
version = int(sys.argv[3])
directory0 = maindirectory + investigator + "/"

treatment1 = "?"
treatment2 = "?"
treatment3 = "?"
treatment4 = "?"
treatment5 = "?"
treatment6 = "?"
Color1 = "green"
Color2 = "blue"
Color3 = "orange"
Color4 = "yellow"
Color5 = "red"
Color6 = "brown"

def CreateCohort(location):
	os.chdir(location)
	files = os.listdir(location)
	dataset = None
	for i in files:
		if dataset is not None:
			temp = pd.read_csv(i)
			dataset = pd.concat([dataset, temp])
			del temp
		if dataset is None:
			dataset = pd.read_csv(i)
	return dataset
	
def CriterionReached(groupdataset):
	inputarray = groupdataset
	groupsize = int(len(inputarray[inputarray["EntryNumber"] == 1]))
	inputarray = inputarray.reset_index()
	del inputarray["index"]
	treatment = inputarray["Treatment"][0]
	outputarray1 = np.zeros(6000)
	outputarray2 = np.zeros(6000)
	outputarray3 = np.zeros(6000)
	Entry = np.array(range(1, 6001))
	Entry = pd.DataFrame(Entry)
	indexer = 1
	for element in range(0, 6000):
		outputarray1[element] = inputarray["SeventyQualifier"][(inputarray["EntryNumber"] == indexer)].sum() / groupsize * 100
		outputarray2[element] = inputarray["EightyQualifier"][(inputarray["EntryNumber"] == indexer)].sum() / groupsize * 100
		outputarray3[element] = inputarray["NinetyQualifier"][(inputarray["EntryNumber"] == indexer)].sum() / groupsize * 100
		indexer = indexer + 1
	outputarray1 = pd.DataFrame(outputarray1)
	outputarray2 = pd.DataFrame(outputarray2)
	outputarray3 = pd.DataFrame(outputarray3)
	Cognition = pd.concat([Entry, outputarray1, outputarray2, outputarray3], axis = 1)
	Cognition.columns = ["Entry", "Seventy", "Eighty", "Ninety"]
	Cognition.to_csv("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Temp/" + treatment + "Survival.csv")
	return Cognition

if (version == 1):
	if (numberofgroups == 1):
		treatment1 = str(sys.argv[4])
		Color1 = str(sys.argv[5])
		directory1 = directory0 + "Data/Initial Discrimination/" + treatment1 + "/"
		group1 = CreateCohort(directory1)
		CriterionReached(group1)
		group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "Survival.csv")
		plt.plot(group1["Entry"][0:2000], group1["Eighty"][0:2000], Color1)
		plt.title("Reversal 80%")
		plt.ylabel("% of group that reached criterion")
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xlabel("Entry Number")
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.legend([treatment1])
		plt.show()
	if (numberofgroups == 2):
		print("Nothing designed yet")
	if (numberofgroups == 3):
		print("Nothing designed yet")
	if (numberofgroups == 4):
		print("Nothing designed yet")
	if (numberofgroups == 5):
		print("Nothing designed yet")
	if (numberofgroups == 6):
		print("Nothing designed yet")
	if (numberofgroups == 7):
		print("Nothing designed yet")
	if (numberofgroups == 8):
		print("Nothing designed yet")
	if (numberofgroups == 9):
		print("Nothing designed yet")
	if (numberofgroups == 10):
		print("Nothing designed yet")
if (version == 2):
	if (numberofgroups == 1):
		treatment1 = str(sys.argv[4])
		Color1 = str(sys.argv[5])
		directory1 = directory0 + "Data/Reversal/" + treatment1 + "/"
		group1 = CreateCohort(directory1)
		CriterionReached(group1)
		group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "Survival.csv")
		plt.plot(group1["Entry"][0:2000], group1["Eighty"][0:2000], Color1)
		plt.title("Initial Discrimination 80%")
		plt.ylabel("% of group that reached criterion")
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xlabel("Entry Number")
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.legend([treatment1])
		plt.show()
	if (numberofgroups == 2):
		print("Nothing designed yet")
	if (numberofgroups == 3):
		print("Nothing designed yet")
	if (numberofgroups == 4):
		print("Nothing designed yet")
	if (numberofgroups == 5):
		print("Nothing designed yet")
	if (numberofgroups == 6):
		print("Nothing designed yet")
	if (numberofgroups == 7):
		print("Nothing designed yet")
	if (numberofgroups == 8):
		print("Nothing designed yet")
	if (numberofgroups == 9):
		print("Nothing designed yet")
	if (numberofgroups == 10):
		print("Nothing designed yet")