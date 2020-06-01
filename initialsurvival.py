import pandas as pd
import numpy as np
import multiprocessing as mp
import os
import sys
import datetime
from matplotlib import pyplot as plt
from scipy import stats

maindirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
investigator = str(sys.argv[1])
numberofgroups = int(sys.argv[2])
criterion = 70
directory0 = maindirectory + investigator + "/"
now = datetime.datetime.now()
month = str(now.month)
day = str(now.day)
year = str(now.year)
today = month + "-" + day + "-" + year

treatment1 = "?"
treatment2 = "?"
treatment3 = "?"
treatment4 = "?"
treatment5 = "?"
treatment6 = "?"
treatment7 = "?"
treatment8 = "?"
treatment9 = "?"
treatment10 = "?"
treatment11 = "?"
treatment12 = "?"
Color1 = "green"
Color2 = "blue"
Color3 = "orange"
Color4 = "yellow"
Color5 = "red"
Color6 = "brown"
Color7 = "black"
Color8 = "purple"
Color9 = "darkgreen"
Color10 = "darkred"
Color11 = "pink"
Color12 = "darkblue"

if (numberofgroups == 1):
	treatment1 = str(sys.argv[3])
	Color1 = str(sys.argv[4])
	criterion = int(sys.argv[5])
if (numberofgroups == 2):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	Color1 = str(sys.argv[5])
	Color2 = str(sys.argv[6])
	criterion = int(sys.argv[7])
if (numberofgroups == 3):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	Color1 = str(sys.argv[6])
	Color2 = str(sys.argv[7])
	Color3 = str(sys.argv[8])
	criterion = int(sys.argv[9])
if (numberofgroups == 4):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	Color1 = str(sys.argv[7])
	Color2 = str(sys.argv[8])
	Color3 = str(sys.argv[9])
	Color4 = str(sys.argv[10])
	criterion = int(sys.argv[11])
if (numberofgroups == 5):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	Color1 = str(sys.argv[8])
	Color2 = str(sys.argv[9])
	Color3 = str(sys.argv[10])
	Color4 = str(sys.argv[11])
	Color5 = str(sys.argv[12])
	criterion = int(sys.argv[13])
if (numberofgroups == 6):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	Color1 = str(sys.argv[9])
	Color2 = str(sys.argv[10])
	Color3 = str(sys.argv[11])
	Color4 = str(sys.argv[12])
	Color5 = str(sys.argv[13])
	Color6 = str(sys.argv[14])
	criterion = int(sys.argv[15])

if (numberofgroups == 7):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	Color1 = str(sys.argv[10])
	Color2 = str(sys.argv[11])
	Color3 = str(sys.argv[12])
	Color4 = str(sys.argv[13])
	Color5 = str(sys.argv[14])
	Color6 = str(sys.argv[15])
	Color7 = str(sys.argv[16])
	criterion = int(sys.argv[17])
	
if (numberofgroups == 8):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	treatment8 = str(sys.argv[10])
	Color1 = str(sys.argv[11])
	Color2 = str(sys.argv[12])
	Color3 = str(sys.argv[13])
	Color4 = str(sys.argv[14])
	Color5 = str(sys.argv[15])
	Color6 = str(sys.argv[16])
	Color7 = str(sys.argv[17])
	Color8 = str(sys.argv[18])	
	criterion = int(sys.argv[19])
	
if (numberofgroups == 9):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	treatment8 = str(sys.argv[10])
	treatment9 = str(sys.argv[11])
	Color1 = str(sys.argv[12])
	Color2 = str(sys.argv[13])
	Color3 = str(sys.argv[14])
	Color4 = str(sys.argv[15])
	Color5 = str(sys.argv[16])
	Color6 = str(sys.argv[17])
	Color7 = str(sys.argv[18])
	Color8 = str(sys.argv[19])
	Color9 = str(sys.argv[20])	
	criterion = int(sys.argv[21])
	
if (numberofgroups == 10):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	treatment8 = str(sys.argv[10])
	treatment9 = str(sys.argv[11])
	treatment10 = str(sys.argv[12])
	Color1 = str(sys.argv[13])
	Color2 = str(sys.argv[14])
	Color3 = str(sys.argv[15])
	Color4 = str(sys.argv[16])
	Color5 = str(sys.argv[17])
	Color6 = str(sys.argv[18])
	Color7 = str(sys.argv[19])
	Color8 = str(sys.argv[20])
	Color9 = str(sys.argv[21])
	Color10 = str(sys.argv[22])
	criterion = int(sys.argv[23])
	
if (numberofgroups == 11):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	treatment8 = str(sys.argv[10])
	treatment9 = str(sys.argv[11])
	treatment10 = str(sys.argv[12])
	treatment11 = str(sys.argv[13])
	Color1 = str(sys.argv[14])
	Color2 = str(sys.argv[15])
	Color3 = str(sys.argv[16])
	Color4 = str(sys.argv[17])
	Color5 = str(sys.argv[18])
	Color6 = str(sys.argv[19])
	Color7 = str(sys.argv[20])
	Color8 = str(sys.argv[21])
	Color9 = str(sys.argv[22])
	Color10 = str(sys.argv[23])
	Color11 = str(sys.argv[24])
	criterion = int(sys.argv[25])
	
if (numberofgroups == 12):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	treatment8 = str(sys.argv[10])
	treatment9 = str(sys.argv[11])
	treatment10 = str(sys.argv[12])
	treatment11 = str(sys.argv[13])
	treatment12 = str(sys.argv[14])
	Color1 = str(sys.argv[15])
	Color2 = str(sys.argv[16])
	Color3 = str(sys.argv[17])
	Color4 = str(sys.argv[18])
	Color5 = str(sys.argv[19])
	Color6 = str(sys.argv[20])
	Color7 = str(sys.argv[21])
	Color8 = str(sys.argv[22])
	Color9 = str(sys.argv[23])
	Color10 = str(sys.argv[24])
	Color11 = str(sys.argv[25])
	Color12 = str(sys.argv[26])
	criterion = int(sys.argv[27])
	
directory1 = directory0 + "Data/Initial Discrimination/" + treatment1
directory2 = directory0 + "Data/Initial Discrimination/" + treatment2
directory3 = directory0 + "Data/Initial Discrimination/" + treatment3
directory4 = directory0 + "Data/Initial Discrimination/" + treatment4
directory5 = directory0 + "Data/Initial Discrimination/" + treatment5
directory6 = directory0 + "Data/Initial Discrimination/" + treatment6
directory7 = directory0 + "Data/Initial Discrimination/" + treatment7
directory8 = directory0 + "Data/Initial Discrimination/" + treatment8
directory9 = directory0 + "Data/Initial Discrimination/" + treatment9
directory10 = directory0 + "Data/Initial Discrimination/" + treatment10
directory11 = directory0 + "Data/Initial Discrimination/" + treatment11
directory12 = directory0 + "Data/Initial Discrimination/" + treatment12

def CreateCohort(location):
	os.chdir(location)
	files = os.listdir(location)
	dataset = None
	for i in files:
		if dataset is not None:
			temp = pd.read_csv(i)
			temp = temp[["AnimalNumber", "Treatment", "EntryNumber", "SeventyQualifier", "EightyQualifier", "NinetyQualifier"]]
			dataset = pd.concat([dataset, temp], axis=0)
			del temp
		if dataset is None:
			dataset = pd.read_csv(i)
			dataset = dataset[["AnimalNumber", "Treatment", "EntryNumber", "SeventyQualifier", "EightyQualifier", "NinetyQualifier"]]
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
	Cognition.to_csv("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Temp/" + treatment + "InitialSurvival.csv")
	return Cognition

if (numberofgroups == 1):
	Group1 = CreateCohort(directory1)
	CriterionReached(Group1)
	value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	

if (numberofgroups == 2):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	grouplist = [Group1, Group2]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=2) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()
	
if (numberofgroups == 3):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	grouplist = [Group1, Group2, Group3]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=3) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	
	
if (numberofgroups == 4):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	grouplist = [Group1, Group2, Group3, Group4]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	
	
if (numberofgroups == 5):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	grouplist = [Group1, Group2, Group3, Group4, Group5]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		G5N = str(len(os.listdir(directory5)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Seventy"][0:2000], Color=Color5)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Eighty"][0:2000], Color=Color5)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Ninety"][0:2000], Color=Color5)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	
	
if (numberofgroups == 6):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	Group6 = CreateCohort(directory6)
	grouplist = [Group1, Group2, Group3, Group4, Group5, Group6]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		G5N = str(len(os.listdir(directory5)))
		G6N = str(len(os.listdir(directory6)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "InitialSurvival.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Seventy"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Seventy"][0:2000], Color=Color6)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Eighty"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Eighty"][0:2000], Color=Color6)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Ninety"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Ninety"][0:2000], Color=Color6)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	
	
if (numberofgroups == 7):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	Group6 = CreateCohort(directory6)
	Group7 = CreateCohort(directory7)
	grouplist = [Group1, Group2, Group3, Group4, Group5, Group6, Group7]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		G5N = str(len(os.listdir(directory5)))
		G6N = str(len(os.listdir(directory6)))
		G7N = str(len(os.listdir(directory7)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "InitialSurvival.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "InitialSurvival.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Seventy"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Seventy"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Seventy"][0:2000], Color=Color7)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Eighty"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Eighty"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Eighty"][0:2000], Color=Color7)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Ninety"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Ninety"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Ninety"][0:2000], Color=Color7)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	
	
if (numberofgroups == 8):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	Group6 = CreateCohort(directory6)
	Group7 = CreateCohort(directory7)
	Group8 = CreateCohort(directory8)
	grouplist = [Group1, Group2, Group3, Group4, Group5, Group6, Group7, Group8]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		G5N = str(len(os.listdir(directory5)))
		G6N = str(len(os.listdir(directory6)))
		G7N = str(len(os.listdir(directory7)))
		G8N = str(len(os.listdir(directory8)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "InitialSurvival.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "InitialSurvival.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "InitialSurvival.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Seventy"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Seventy"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Seventy"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Seventy"][0:2000], Color=Color8)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Eighty"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Eighty"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Eighty"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Eighty"][0:2000], Color=Color8)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Ninety"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Ninety"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Ninety"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Ninety"][0:2000], Color=Color8)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	
	
if (numberofgroups == 9):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	Group6 = CreateCohort(directory6)
	Group7 = CreateCohort(directory7)
	Group8 = CreateCohort(directory8)
	Group9 = CreateCohort(directory9)
	grouplist = [Group1, Group2, Group3, Group4, Group5, Group6, Group7, Group8, Group9]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		G5N = str(len(os.listdir(directory5)))
		G6N = str(len(os.listdir(directory6)))
		G7N = str(len(os.listdir(directory7)))
		G8N = str(len(os.listdir(directory8)))
		G9N = str(len(os.listdir(directory9)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "InitialSurvival.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "InitialSurvival.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "InitialSurvival.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "InitialSurvival.csv")
		Group9 = pd.read_csv(maindirectory + "Temp/" + treatment9 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Seventy"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Seventy"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Seventy"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Seventy"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Seventy"][0:2000], Color=Color9)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Eighty"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Eighty"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Eighty"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Eighty"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Eighty"][0:2000], Color=Color9)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Ninety"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Ninety"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Ninety"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Ninety"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Ninety"][0:2000], Color=Color9)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")", treatment9 + " (n=" + G9N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	
	
if (numberofgroups == 10):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	Group6 = CreateCohort(directory6)
	Group7 = CreateCohort(directory7)
	Group8 = CreateCohort(directory8)
	Group9 = CreateCohort(directory9)
	Group10 = CreateCohort(directory10)
	grouplist = [Group1, Group2, Group3, Group4, Group5, Group6, Group7, Group8, Group9, Group10]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		G5N = str(len(os.listdir(directory5)))
		G6N = str(len(os.listdir(directory6)))
		G7N = str(len(os.listdir(directory7)))
		G8N = str(len(os.listdir(directory8)))
		G9N = str(len(os.listdir(directory9)))
		G10N = str(len(os.listdir(directory10)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "InitialSurvival.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "InitialSurvival.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "InitialSurvival.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "InitialSurvival.csv")
		Group9 = pd.read_csv(maindirectory + "Temp/" + treatment9 + "InitialSurvival.csv")
		Group10 = pd.read_csv(maindirectory + "Temp/" + treatment10 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Seventy"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Seventy"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Seventy"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Seventy"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Seventy"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Seventy"][0:2000], Color=Color10)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Eighty"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Eighty"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Eighty"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Eighty"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Eighty"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Eighty"][0:2000], Color=Color10)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Ninety"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Ninety"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Ninety"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Ninety"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Ninety"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Ninety"][0:2000], Color=Color10)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")", treatment9 + " (n=" + G9N + ")", treatment10 + " (n=" + G10N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()	
	
if (numberofgroups == 11):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	Group6 = CreateCohort(directory6)
	Group7 = CreateCohort(directory7)
	Group8 = CreateCohort(directory8)
	Group9 = CreateCohort(directory9)
	Group10 = CreateCohort(directory10)
	Group11 = CreateCohort(directory11)
	grouplist = [Group1, Group2, Group3, Group4, Group5, Group6, Group7, Group8, Group9, Group10, Group11]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		G5N = str(len(os.listdir(directory5)))
		G6N = str(len(os.listdir(directory6)))
		G7N = str(len(os.listdir(directory7)))
		G8N = str(len(os.listdir(directory8)))
		G9N = str(len(os.listdir(directory9)))
		G10N = str(len(os.listdir(directory10)))
		G11N = str(len(os.listdir(directory11)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "InitialSurvival.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "InitialSurvival.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "InitialSurvival.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "InitialSurvival.csv")
		Group9 = pd.read_csv(maindirectory + "Temp/" + treatment9 + "InitialSurvival.csv")
		Group10 = pd.read_csv(maindirectory + "Temp/" + treatment10 + "InitialSurvival.csv")
		Group11 = pd.read_csv(maindirectory + "Temp/" + treatment11 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Seventy"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Seventy"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Seventy"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Seventy"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Seventy"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Seventy"][0:2000], Color=Color10)
			plt.plot(Group11["Entry"][0:2000], Group11["Seventy"][0:2000], Color=Color11)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Eighty"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Eighty"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Eighty"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Eighty"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Eighty"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Eighty"][0:2000], Color=Color10)
			plt.plot(Group11["Entry"][0:2000], Group11["Eighty"][0:2000], Color=Color11)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Ninety"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Ninety"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Ninety"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Ninety"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Ninety"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Ninety"][0:2000], Color=Color10)
			plt.plot(Group11["Entry"][0:2000], Group11["Ninety"][0:2000], Color=Color11)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")", treatment9 + " (n=" + G9N + ")", treatment10 + " (n=" + G10N + ")", treatment11 + " (n=" + G11N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()
	
if (numberofgroups == 12):
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	Group6 = CreateCohort(directory6)
	Group7 = CreateCohort(directory7)
	Group8 = CreateCohort(directory8)
	Group9 = CreateCohort(directory9)
	Group10 = CreateCohort(directory10)
	Group11 = CreateCohort(directory11)
	Group12 = CreateCohort(directory12)
	grouplist = [Group1, Group2, Group3, Group4, Group5, Group6, Group7, Group8, Group9, Group10, Group11, Group12]
	value = 0
	if __name__ == '__main__':
		with mp.Pool(processes=4) as pool:
			pool.map_async(CriterionReached, grouplist)
			pool.close()
			pool.join()
			value = 1
	if (value == 1):
		G1N = str(len(os.listdir(directory1)))
		G2N = str(len(os.listdir(directory2)))
		G3N = str(len(os.listdir(directory3)))
		G4N = str(len(os.listdir(directory4)))
		G5N = str(len(os.listdir(directory5)))
		G6N = str(len(os.listdir(directory6)))
		G7N = str(len(os.listdir(directory7)))
		G8N = str(len(os.listdir(directory8)))
		G9N = str(len(os.listdir(directory9)))
		G10N = str(len(os.listdir(directory10)))
		G11N = str(len(os.listdir(directory11)))
		G12N = str(len(os.listdir(directory12)))
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "InitialSurvival.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "InitialSurvival.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "InitialSurvival.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "InitialSurvival.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "InitialSurvival.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "InitialSurvival.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "InitialSurvival.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "InitialSurvival.csv")
		Group9 = pd.read_csv(maindirectory + "Temp/" + treatment9 + "InitialSurvival.csv")
		Group10 = pd.read_csv(maindirectory + "Temp/" + treatment10 + "InitialSurvival.csv")
		Group11 = pd.read_csv(maindirectory + "Temp/" + treatment11 + "InitialSurvival.csv")
		Group12 = pd.read_csv(maindirectory + "Temp/" + treatment12 + "InitialSurvival.csv")
		if (criterion == 70):
			plt.plot(Group1["Entry"][0:2000], Group1["Seventy"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Seventy"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Seventy"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Seventy"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Seventy"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Seventy"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Seventy"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Seventy"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Seventy"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Seventy"][0:2000], Color=Color10)
			plt.plot(Group11["Entry"][0:2000], Group11["Seventy"][0:2000], Color=Color11)
			plt.plot(Group12["Entry"][0:2000], Group12["Seventy"][0:2000], Color=Color12)
			plt.title("Initial Discrimination 70% criterion", fontsize=20)
		if (criterion == 80):
			plt.plot(Group1["Entry"][0:2000], Group1["Eighty"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Eighty"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Eighty"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Eighty"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Eighty"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Eighty"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Eighty"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Eighty"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Eighty"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Eighty"][0:2000], Color=Color10)
			plt.plot(Group11["Entry"][0:2000], Group11["Eighty"][0:2000], Color=Color11)
			plt.plot(Group12["Entry"][0:2000], Group12["Eighty"][0:2000], Color=Color12)
			plt.title("Initial Discrimination 80% criterion", fontsize=20)
		if (criterion == 90):
			plt.plot(Group1["Entry"][0:2000], Group1["Ninety"][0:2000], Color=Color1)
			plt.plot(Group2["Entry"][0:2000], Group2["Ninety"][0:2000], Color=Color2)
			plt.plot(Group3["Entry"][0:2000], Group3["Ninety"][0:2000], Color=Color3)
			plt.plot(Group4["Entry"][0:2000], Group4["Ninety"][0:2000], Color=Color4)
			plt.plot(Group5["Entry"][0:2000], Group5["Ninety"][0:2000], Color=Color5)
			plt.plot(Group6["Entry"][0:2000], Group6["Ninety"][0:2000], Color=Color6)
			plt.plot(Group7["Entry"][0:2000], Group7["Ninety"][0:2000], Color=Color7)
			plt.plot(Group8["Entry"][0:2000], Group8["Ninety"][0:2000], Color=Color8)
			plt.plot(Group9["Entry"][0:2000], Group9["Ninety"][0:2000], Color=Color9)
			plt.plot(Group10["Entry"][0:2000], Group10["Ninety"][0:2000], Color=Color10)
			plt.plot(Group11["Entry"][0:2000], Group11["Ninety"][0:2000], Color=Color11)
			plt.plot(Group12["Entry"][0:2000], Group12["Ninety"][0:2000], Color=Color12)
			plt.title("Initial Discrimination 90% criterion", fontsize=20)
		
		plt.xlabel("Entry Number", fontsize=16)
		plt.ylabel("% of mice that reached criterion", fontsize=16)
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
		plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")", treatment9 + " (n=" + G9N + ")", treatment10 + " (n=" + G10N + ")", treatment11 + " (n=" + G11N + ")", treatment12 + " (n=" + G12N + ")"])
		plt.savefig(directory0 + "Graphs/InitialSurvival" + today + ".jpg")
		plt.show()