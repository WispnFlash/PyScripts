import pandas as pd
import numpy as np
import sys
import os

maindirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
investigator = str(sys.argv[1])
treatment = str(sys.argv[2])
choice = int(sys.argv[3])
directory0 = maindirectory + investigator + "/"
directory1 = directory0 + "Data/"

def CombineMice(treatmentlocation, choice2):
	os.chdir(treatmentlocation)
	animals = os.listdir()
	dataset = None
	if ((choice2 == "ETCinitial") or ((choice2 == "ETCreversal"))):
		for i in animals:
			if dataset is not None:
				temp = pd.read_csv(i)
				temp = temp[["AnimalID", "Treatment", "EntriestoSeventy", "EntriestoEighty", "EntriestoNinety", "HourstoSeventy", "HourstoEighty", "HourstoNinety"]]
				dataset = pd.concat([dataset, temp], axis=0)
				del temp
			if dataset is None:
				dataset = pd.read_csv(i)
				dataset = dataset[["AnimalID", "Treatment", "EntriestoSeventy", "EntriestoEighty", "EntriestoNinety", "HourstoSeventy", "HourstoEighty", "HourstoNinety"]]
	return dataset
	
if (choice == 1):
	choicestring = "movement"
	directory2 = directory1 + "Distance moved/" + treatment + "/"
	data = CombineMice(directory2, "movement")
	data.to_csv(directory0 + "Spreadsheets/" + treatment + choicestring + ".csv", index=False)
if (choice == 2):
	choicestring = "feeding"
	directory2 = directory1 + "Feeding/" + treatment + "/"
	data = CombineMice(directory2, "feeding")
	data.to_csv(directory0 + "Spreadsheets/" + treatment + choicestring + ".csv", index=False)
if (choice == 3):
	choicestring = "ETCinitial"
	directory2 = directory1 + "Entries to Criterion/Initial Discrimination/" + treatment + "/"
	data = CombineMice(directory2, "ETCinitial")
	data.to_csv(directory0 + "Spreadsheets/" + treatment + choicestring + ".csv", index=False)
if (choice == 4):
	choicestring = "ETCreversal"
	directory2 = directory1 + "Entries to Criterion/Reversal/" + treatment + "/"
	data = CombineMice(directory2, "ETCreversal")
	data.to_csv(directory0 + "Spreadsheets/" + treatment + choicestring + ".csv", index=False)
if (choice == 5):
	choicestring = "InitialDiscrimination"
	directory2 = directory1 + "Initial Discrimination/" + treatment + "/"
	data = CombineMice(directory2, "InitialDiscrimination")
	data.to_csv(directory0 + "Spreadsheets/" + treatment + choicestring + ".csv", index=False)
if (choice == 6):
	choicestring = "Reversal"
	directory2 = directory1 + "Entries to Criterion/Reversal/" + treatment + "/"
	data = CombineMice(directory2, "Reversal")
	data.to_csv(directory0 + "Spreadsheets/" + treatment + choicestring + ".csv", index=False)
if (choice == 7):
	choicestring = "independentindex"
	directory2 = directory0 + "Data/Indexes/Independent/" + treatment + "/"
	data = CombineMice(directory2, "independentindex")
	data.to_csv(directory0 + "Spreadsheets/" + treatment + choicestring + ".csv", index=False)
if (choice == 8):
	choicestring = "cumulativeindex"
	directory2 = directory0 + "Data/Indexes/Cumulative/" + treatment + "/"
	data = CombineMice(directory2, "cumulativeindex")
	data.to_csv(directory0 + "Spreadsheets/" + treatment + choicestring + ".csv", index=False)