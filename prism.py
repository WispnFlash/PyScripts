import pandas as pd
import numpy as np
import os
import sys

maindirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
investigator = str(sys.argv[1]) + "/"
treatment = str(sys.argv[2])
type = int(sys.argv[3])
directory0 = maindirectory + investigator + "/"


def IndIndex(location):
	os.chdir(location)
	animals = os.listdir()
	Hour = np.array(range(1, 90))
	Hour = pd.DataFrame(Hour)
	AnimalID = np.full(len(animals), "mouse9999999")
	j = 0
	dataset = None
	for i in animals:
		if dataset is not None:
			temp = pd.read_csv(i)
			index = temp["LearningIndex"]
			AnimalI = temp["Name"][j]
			AnimalID[j] = AnimalI
			dataset = pd.concat([dataset, index], axis=1)
			
			del temp, index, AnimalI
			j = j + 1
		if dataset is None:
			temp = pd.read_csv(i)
			index = temp["LearningIndex"]
			AnimalI = temp["Name"][0]
			AnimalID[0] = AnimalI
			dataset = pd.concat([Hour, index], axis=1)
			del temp, index, AnimalI
			j = j + 1
	
	HourTitle = np.full(1, "Hour")
	dataset.columns = np.concatenate([HourTitle, AnimalID], axis=0)
	return dataset

def CumIndex(location):
	os.chdir(location)
	animals = os.listdir()
	Hour = np.array(range(1, 90))
	Hour = pd.DataFrame(Hour)
	AnimalID = np.full(len(animals), "mouse9999999")
	j = 0
	dataset = None
	for i in animals:
		if dataset is not None:
			temp = pd.read_csv(i)
			index = temp["CumulativeIndex"]
			AnimalI = temp["Name"][j]
			AnimalID[j] = AnimalI
			dataset = pd.concat([dataset, index], axis=1)
			
			del temp, index, AnimalI
			j = j + 1
		if dataset is None:
			temp = pd.read_csv(i)
			index = temp["CumulativeIndex"]
			AnimalI = temp["Name"][0]
			AnimalID[0] = AnimalI
			dataset = pd.concat([Hour, index], axis=1)
			del temp, index, AnimalI
			j = j + 1
	
	HourTitle = np.full(1, "Hour")
	dataset.columns = np.concatenate([HourTitle, AnimalID], axis=0)
	return dataset
	
def Movement(location):
	os.chdir(location)
	animals = os.listdir()
	Hour = np.array(range(1, 90))
	Hour = pd.DataFrame(Hour)
	AnimalID = np.full(len(animals), "mouse9999999")
	j = 0
	dataset = None
	for i in animals:
		if dataset is not None:
			temp = pd.read_csv(i)
			mov = temp["TotPathlength"]
			AnimalI = temp["AnimalNumber"][j]
			AnimalID[j] = AnimalI
			dataset = pd.concat([dataset, mov], axis=1)
			
			del temp, mov, AnimalI
			j = j + 1
		if dataset is None:
			temp = pd.read_csv(i)
			mov = temp["TotPathlength"]
			AnimalI = temp["AnimalNumber"][0]
			AnimalID[0] = AnimalI
			dataset = pd.concat([Hour, mov], axis=1)
			del temp, mov, AnimalI
			j = j + 1
	
	HourTitle = np.full(1, "Hour")
	dataset.columns = np.concatenate([HourTitle, AnimalID], axis=0)
	return dataset
	
def Feeding(location):
	os.chdir(location)
	animals = os.listdir()
	Hour = np.array(range(1, 90))
	Hour = pd.DataFrame(Hour)
	AnimalID = np.full(len(animals), "mouse9999999")
	j = 0
	dataset = None
	for i in animals:
		if dataset is not None:
			temp = pd.read_csv(i)
			fed = temp["TotFeeding"]
			AnimalI = temp["AnimalNumber"][j]
			AnimalID[j] = AnimalI
			dataset = pd.concat([dataset, fed], axis=1)
			
			del temp, fed, AnimalI
			j = j + 1
		if dataset is None:
			temp = pd.read_csv(i)
			fed = temp["TotFeeding"]
			AnimalI = temp["AnimalNumber"][0]
			AnimalID[0] = AnimalI
			dataset = pd.concat([Hour, fed], axis=1)
			del temp, fed, AnimalI
			j = j + 1
	
	HourTitle = np.full(1, "Hour")
	dataset.columns = np.concatenate([HourTitle, AnimalID], axis=0)
	return dataset
	
def SegPrism(location):
	os.chdir(location)
	animals = os.listdir()
	sample = pd.read_csv(animals[0])
	Distance = sample["Distance"]
	del sample
	AnimalID = np.full(len(animals), "mouse9999999")
	j = 0
	dataset = None
	for i in animals:
		if dataset is not None:
			temp = pd.read_csv(i)
			Freq = temp["Frequency"]
			AnimalI = i[:3]
			AnimalID[j] = AnimalI
			dataset = pd.concat([dataset, Freq], axis=1)
			
			del temp, Freq, AnimalI
			j = j + 1
		if dataset is None:
			temp = pd.read_csv(i)
			Freq = temp["Frequency"]
			AnimalI = i[:3]
			AnimalID[0] = AnimalI
			dataset = pd.concat([Distance, Freq], axis=1)
			del temp, Freq, AnimalI
			j = j + 1
	
	DistanceTitle = np.full(1, "Distance")
	dataset.columns = np.concatenate([DistanceTitle, AnimalID], axis=0)
	return dataset


if (type == 1):
	directory = directory0 + "Data/Indexes/Independent/" + treatment + "/"
	data = IndIndex(directory)
	data.to_csv(directory0 + "Spreadsheets/" + treatment + "prismIndIndexResults.csv")
	
if (type == 2):
	directory = directory0 + "Data/Indexes/Cumulative/" + treatment + "/"
	data = CumIndex(directory)
	data.to_csv(directory0 + "Spreadsheets/" + treatment + "prismCumIndexResults.csv")
	
if (type == 3):
	directory = directory0 + "Data/Distance moved/" + treatment + "/"	
	data = Movement(directory)
	data.to_csv(directory0 + "Spreadsheets/" + treatment + "prismMovementResults.csv")
	
if (type == 4):
	directory = directory0 + "Data/Feeding/" + treatment + "/"
	data = Feeding(directory)
	data.to_csv(directory0 + "Spreadsheets/" + treatment + "prismFeedingResults.csv")
	
if (type == 5):
	directory = directory0 + "Data/Segmentation/Frequency/" + treatment + "/"
	data = SegPrism(directory)
	data.to_csv(directory0 + "Spreadsheets/" + treatment + "segmentprismresults.csv")
	
	
	

	

			