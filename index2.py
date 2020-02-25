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
if (numberofgroups == 2):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	Color1 = str(sys.argv[5])
	Color2 = str(sys.argv[6])
if (numberofgroups == 3):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	Color1 = str(sys.argv[6])
	Color2 = str(sys.argv[7])
	Color3 = str(sys.argv[8])
if (numberofgroups == 4):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	Color1 = str(sys.argv[7])
	Color2 = str(sys.argv[8])
	Color3 = str(sys.argv[9])
	Color4 = str(sys.argv[10])
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

directory1 = directory0 + "Data/Indexes/Cumulative/" + treatment1
directory2 = directory0 + "Data/Indexes/Cumulative/" + treatment2
directory3 = directory0 + "Data/Indexes/Cumulative/" + treatment3
directory4 = directory0 + "Data/Indexes/Cumulative/" + treatment4
directory5 = directory0 + "Data/Indexes/Cumulative/" + treatment5
directory6 = directory0 + "Data/Indexes/Cumulative/" + treatment6
directory7 = directory0 + "Data/Indexes/Cumulative/" + treatment7
directory8 = directory0 + "Data/Indexes/Cumulative/" + treatment8
directory9 = directory0 + "Data/Indexes/Cumulative/" + treatment9
directory10 = directory0 + "Data/Indexes/Cumulative/" + treatment10
directory11 = directory0 + "Data/Indexes/Cumulative/" + treatment11
directory12 = directory0 + "Data/Indexes/Cumulative/" + treatment12

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
	groupsize = int(len(inputarray[inputarray["Hour"] == 1]))
	inputarray = inputarray.reset_index()
	del inputarray["index"]
	treatment = inputarray["Group"][0]
	IndexMeans = np.zeros(89)
	IndexErrors = np.zeros(89)
	Hour = np.array(range(1, 90))
	Hour = pd.DataFrame(Hour)
	indexer = 1
	for element in range(0, 89):
		temp = inputarray["CumulativeIndex"][(inputarray["Hour"] == indexer)]
		IndexMeans[element] = temp.mean()
		IndexErrors[element] = stats.sem(temp)
		indexer = indexer + 1
		del temp
	IndexMeans = pd.DataFrame(IndexMeans)
	IndexErrors = pd.DataFrame(IndexErrors)
	Index = pd.concat([Hour, IndexMeans, IndexErrors], axis = 1)
	Index.columns = ["Hour", "CumulativeIndex", "Error"]
	Index.to_csv("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Temp/" + treatment + "index.csv")
	return Index

grouplist = ["1", "2", "3", "4", "5", "6"]

if (numberofgroups == 1):
	Group1 = CreateCohort(directory1)
	CriterionReached(Group1)
	G1N = str(len(os.listdir(directory1)))
	Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
	plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
	plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
	caplines1[0].set_marker('_')
	caplines1[0].set_markersize(3)
	plt.title("Cumulative Learning Index by Hour", fontsize=20)
	plt.xlabel("Hour", fontsize=16)
	plt.ylabel("Cumulative Index", fontsize=16)
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
	plt.axvspan(3, 15, alpha=0.5, color="lightgray")
	plt.axvspan(27, 39, alpha=0.5, color="lightgray")
	plt.axvspan(51, 63, alpha=0.5, color="lightgray")
	plt.axvspan(75, 87, alpha=0.5, color="lightgray")
	plt.legend([treatment1 + " (n=" + G1N + ")"], fontsize=8)
	plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
	
	
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
	
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		plt.plot(Group5["Hour"], Group5["CumulativeIndex"], Color=Color5, marker=",", linestyle="-")
		plotline5, caplines5, line5 = plt.errorbar(Group5["Hour"], Group5["CumulativeIndex"], yerr=Group5["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines5[0].set_marker('_')
		caplines5[0].set_markersize(3)
		
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "index.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		plt.plot(Group5["Hour"], Group5["CumulativeIndex"], Color=Color5, marker=",", linestyle="-")
		plotline5, caplines5, line5 = plt.errorbar(Group5["Hour"], Group5["CumulativeIndex"], yerr=Group5["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines5[0].set_marker('_')
		caplines5[0].set_markersize(3)
		
		plt.plot(Group6["Hour"], Group6["CumulativeIndex"], Color=Color6, marker=",", linestyle="-")
		plotline6, caplines6, line6 = plt.errorbar(Group6["Hour"], Group6["CumulativeIndex"], yerr=Group6["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines6[0].set_marker('_')
		caplines6[0].set_markersize(3)
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
		

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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "index.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "index.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		plt.plot(Group5["Hour"], Group5["CumulativeIndex"], Color=Color5, marker=",", linestyle="-")
		plotline5, caplines5, line5 = plt.errorbar(Group5["Hour"], Group5["CumulativeIndex"], yerr=Group5["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines5[0].set_marker('_')
		caplines5[0].set_markersize(3)
		
		plt.plot(Group6["Hour"], Group6["CumulativeIndex"], Color=Color6, marker=",", linestyle="-")
		plotline6, caplines6, line6 = plt.errorbar(Group6["Hour"], Group6["CumulativeIndex"], yerr=Group6["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines6[0].set_marker('_')
		caplines6[0].set_markersize(3)
		
		plt.plot(Group7["Hour"], Group7["CumulativeIndex"], Color=Color7, marker=",", linestyle="-")
		plotline7, caplines7, line7 = plt.errorbar(Group7["Hour"], Group7["CumulativeIndex"], yerr=Group7["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines7[0].set_marker('_')
		caplines7[0].set_markersize(3)
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
				
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "index.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "index.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "index.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		plt.plot(Group5["Hour"], Group5["CumulativeIndex"], Color=Color5, marker=",", linestyle="-")
		plotline5, caplines5, line5 = plt.errorbar(Group5["Hour"], Group5["CumulativeIndex"], yerr=Group5["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines5[0].set_marker('_')
		caplines5[0].set_markersize(3)
		
		plt.plot(Group6["Hour"], Group6["CumulativeIndex"], Color=Color6, marker=",", linestyle="-")
		plotline6, caplines6, line6 = plt.errorbar(Group6["Hour"], Group6["CumulativeIndex"], yerr=Group6["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines6[0].set_marker('_')
		caplines6[0].set_markersize(3)
		
		plt.plot(Group7["Hour"], Group7["CumulativeIndex"], Color=Color7, marker=",", linestyle="-")
		plotline7, caplines7, line7 = plt.errorbar(Group7["Hour"], Group7["CumulativeIndex"], yerr=Group7["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines7[0].set_marker('_')
		caplines7[0].set_markersize(3)
		
		plt.plot(Group8["Hour"], Group8["CumulativeIndex"], Color=Color8, marker=",", linestyle="-")
		plotline8, caplines8, line8 = plt.errorbar(Group8["Hour"], Group8["CumulativeIndex"], yerr=Group8["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines8[0].set_marker('_')
		caplines8[0].set_markersize(3)
		
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
				
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "index.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "index.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "index.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "index.csv")
		Group9 = pd.read_csv(maindirectory + "Temp/" + treatment9 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		plt.plot(Group5["Hour"], Group5["CumulativeIndex"], Color=Color5, marker=",", linestyle="-")
		plotline5, caplines5, line5 = plt.errorbar(Group5["Hour"], Group5["CumulativeIndex"], yerr=Group5["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines5[0].set_marker('_')
		caplines5[0].set_markersize(3)
		
		plt.plot(Group6["Hour"], Group6["CumulativeIndex"], Color=Color6, marker=",", linestyle="-")
		plotline6, caplines6, line6 = plt.errorbar(Group6["Hour"], Group6["CumulativeIndex"], yerr=Group6["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines6[0].set_marker('_')
		caplines6[0].set_markersize(3)
		
		plt.plot(Group7["Hour"], Group7["CumulativeIndex"], Color=Color7, marker=",", linestyle="-")
		plotline7, caplines7, line7 = plt.errorbar(Group7["Hour"], Group7["CumulativeIndex"], yerr=Group7["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines7[0].set_marker('_')
		caplines7[0].set_markersize(3)
		
		plt.plot(Group8["Hour"], Group8["CumulativeIndex"], Color=Color8, marker=",", linestyle="-")
		plotline8, caplines8, line8 = plt.errorbar(Group8["Hour"], Group8["CumulativeIndex"], yerr=Group8["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines8[0].set_marker('_')
		caplines8[0].set_markersize(3)
		
		plt.plot(Group9["Hour"], Group9["CumulativeIndex"], Color=Color9, marker=",", linestyle="-")
		plotline9, caplines9, line9 = plt.errorbar(Group9["Hour"], Group9["CumulativeIndex"], yerr=Group9["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines9[0].set_marker('_')
		caplines9[0].set_markersize(3)
		
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")", treatment9 + " (n=" + G9N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
				
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "index.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "index.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "index.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "index.csv")
		Group9 = pd.read_csv(maindirectory + "Temp/" + treatment9 + "index.csv")
		Group10 = pd.read_csv(maindirectory + "Temp/" + treatment10 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		plt.plot(Group5["Hour"], Group5["CumulativeIndex"], Color=Color5, marker=",", linestyle="-")
		plotline5, caplines5, line5 = plt.errorbar(Group5["Hour"], Group5["CumulativeIndex"], yerr=Group5["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines5[0].set_marker('_')
		caplines5[0].set_markersize(3)
		
		plt.plot(Group6["Hour"], Group6["CumulativeIndex"], Color=Color6, marker=",", linestyle="-")
		plotline6, caplines6, line6 = plt.errorbar(Group6["Hour"], Group6["CumulativeIndex"], yerr=Group6["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines6[0].set_marker('_')
		caplines6[0].set_markersize(3)
		
		plt.plot(Group7["Hour"], Group7["CumulativeIndex"], Color=Color7, marker=",", linestyle="-")
		plotline7, caplines7, line7 = plt.errorbar(Group7["Hour"], Group7["CumulativeIndex"], yerr=Group7["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines7[0].set_marker('_')
		caplines7[0].set_markersize(3)
		
		plt.plot(Group8["Hour"], Group8["CumulativeIndex"], Color=Color8, marker=",", linestyle="-")
		plotline8, caplines8, line8 = plt.errorbar(Group8["Hour"], Group8["CumulativeIndex"], yerr=Group8["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines8[0].set_marker('_')
		caplines8[0].set_markersize(3)
		
		plt.plot(Group9["Hour"], Group9["CumulativeIndex"], Color=Color9, marker=",", linestyle="-")
		plotline9, caplines9, line9 = plt.errorbar(Group9["Hour"], Group9["CumulativeIndex"], yerr=Group9["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines9[0].set_marker('_')
		caplines9[0].set_markersize(3)
		
		plt.plot(Group10["Hour"], Group10["CumulativeIndex"], Color=Color10, marker=",", linestyle="-")
		plotline10, caplines10, line10 = plt.errorbar(Group10["Hour"], Group10["CumulativeIndex"], yerr=Group10["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines10[0].set_marker('_')
		caplines10[0].set_markersize(3)
		
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")", treatment9 + " (n=" + G9N + ")", treatment10 + " (n=" + G10N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
				
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "index.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "index.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "index.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "index.csv")
		Group9 = pd.read_csv(maindirectory + "Temp/" + treatment9 + "index.csv")
		Group10 = pd.read_csv(maindirectory + "Temp/" + treatment10 + "index.csv")
		Group11 = pd.read_csv(maindirectory + "Temp/" + treatment11 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		plt.plot(Group5["Hour"], Group5["CumulativeIndex"], Color=Color5, marker=",", linestyle="-")
		plotline5, caplines5, line5 = plt.errorbar(Group5["Hour"], Group5["CumulativeIndex"], yerr=Group5["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines5[0].set_marker('_')
		caplines5[0].set_markersize(3)
		
		plt.plot(Group6["Hour"], Group6["CumulativeIndex"], Color=Color6, marker=",", linestyle="-")
		plotline6, caplines6, line6 = plt.errorbar(Group6["Hour"], Group6["CumulativeIndex"], yerr=Group6["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines6[0].set_marker('_')
		caplines6[0].set_markersize(3)
		
		plt.plot(Group7["Hour"], Group7["CumulativeIndex"], Color=Color7, marker=",", linestyle="-")
		plotline7, caplines7, line7 = plt.errorbar(Group7["Hour"], Group7["CumulativeIndex"], yerr=Group7["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines7[0].set_marker('_')
		caplines7[0].set_markersize(3)
		
		plt.plot(Group8["Hour"], Group8["CumulativeIndex"], Color=Color8, marker=",", linestyle="-")
		plotline8, caplines8, line8 = plt.errorbar(Group8["Hour"], Group8["CumulativeIndex"], yerr=Group8["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines8[0].set_marker('_')
		caplines8[0].set_markersize(3)
		
		plt.plot(Group9["Hour"], Group9["CumulativeIndex"], Color=Color9, marker=",", linestyle="-")
		plotline9, caplines9, line9 = plt.errorbar(Group9["Hour"], Group9["CumulativeIndex"], yerr=Group9["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines9[0].set_marker('_')
		caplines9[0].set_markersize(3)
		
		plt.plot(Group10["Hour"], Group10["CumulativeIndex"], Color=Color10, marker=",", linestyle="-")
		plotline10, caplines10, line10 = plt.errorbar(Group10["Hour"], Group10["CumulativeIndex"], yerr=Group10["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines10[0].set_marker('_')
		caplines10[0].set_markersize(3)
		
		plt.plot(Group11["Hour"], Group11["CumulativeIndex"], Color=Color11, marker=",", linestyle="-")
		plotline11, caplines11, line11 = plt.errorbar(Group11["Hour"], Group11["CumulativeIndex"], yerr=Group11["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines11[0].set_marker('_')
		caplines11[0].set_markersize(3)
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")", treatment9 + " (n=" + G9N + ")", treatment10 + " (n=" + G10N + ")", treatment11 + " (n=" + G11N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
				
		
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
		Group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "index.csv")
		Group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "index.csv")
		Group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "index.csv")
		Group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "index.csv")
		Group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "index.csv")
		Group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "index.csv")
		Group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "index.csv")
		Group8 = pd.read_csv(maindirectory + "Temp/" + treatment8 + "index.csv")
		Group9 = pd.read_csv(maindirectory + "Temp/" + treatment9 + "index.csv")
		Group10 = pd.read_csv(maindirectory + "Temp/" + treatment10 + "index.csv")
		Group11 = pd.read_csv(maindirectory + "Temp/" + treatment11 + "index.csv")
		Group12 = pd.read_csv(maindirectory + "Temp/" + treatment12 + "index.csv")
		
		plt.plot(Group1["Hour"], Group1["CumulativeIndex"], Color=Color1, marker=",", linestyle="-")
		plotline1, caplines1, line1 = plt.errorbar(Group1["Hour"], Group1["CumulativeIndex"], yerr=Group1["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines1[0].set_marker('_')
		caplines1[0].set_markersize(3)
		
		plt.plot(Group2["Hour"], Group2["CumulativeIndex"], Color=Color2, marker=",", linestyle="-")
		plotline2, caplines2, line2 = plt.errorbar(Group2["Hour"], Group2["CumulativeIndex"], yerr=Group2["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines2[0].set_marker('_')
		caplines2[0].set_markersize(3)
		
		plt.plot(Group3["Hour"], Group3["CumulativeIndex"], Color=Color3, marker=",", linestyle="-")
		plotline3, caplines3, line3 = plt.errorbar(Group3["Hour"], Group3["CumulativeIndex"], yerr=Group3["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines3[0].set_marker('_')
		caplines3[0].set_markersize(3)
		
		plt.plot(Group4["Hour"], Group4["CumulativeIndex"], Color=Color4, marker=",", linestyle="-")
		plotline4, caplines4, line4 = plt.errorbar(Group4["Hour"], Group4["CumulativeIndex"], yerr=Group4["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines4[0].set_marker('_')
		caplines4[0].set_markersize(3)
		
		plt.plot(Group5["Hour"], Group5["CumulativeIndex"], Color=Color5, marker=",", linestyle="-")
		plotline5, caplines5, line5 = plt.errorbar(Group5["Hour"], Group5["CumulativeIndex"], yerr=Group5["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines5[0].set_marker('_')
		caplines5[0].set_markersize(3)
		
		plt.plot(Group6["Hour"], Group6["CumulativeIndex"], Color=Color6, marker=",", linestyle="-")
		plotline6, caplines6, line6 = plt.errorbar(Group6["Hour"], Group6["CumulativeIndex"], yerr=Group6["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines6[0].set_marker('_')
		caplines6[0].set_markersize(3)
		
		plt.plot(Group7["Hour"], Group7["CumulativeIndex"], Color=Color7, marker=",", linestyle="-")
		plotline7, caplines7, line7 = plt.errorbar(Group7["Hour"], Group7["CumulativeIndex"], yerr=Group7["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines7[0].set_marker('_')
		caplines7[0].set_markersize(3)
		
		plt.plot(Group8["Hour"], Group8["CumulativeIndex"], Color=Color8, marker=",", linestyle="-")
		plotline8, caplines8, line8 = plt.errorbar(Group8["Hour"], Group8["CumulativeIndex"], yerr=Group8["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines8[0].set_marker('_')
		caplines8[0].set_markersize(3)
		
		plt.plot(Group9["Hour"], Group9["CumulativeIndex"], Color=Color9, marker=",", linestyle="-")
		plotline9, caplines9, line9 = plt.errorbar(Group9["Hour"], Group9["CumulativeIndex"], yerr=Group9["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines9[0].set_marker('_')
		caplines9[0].set_markersize(3)
		
		plt.plot(Group10["Hour"], Group10["CumulativeIndex"], Color=Color10, marker=",", linestyle="-")
		plotline10, caplines10, line10 = plt.errorbar(Group10["Hour"], Group10["CumulativeIndex"], yerr=Group10["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines10[0].set_marker('_')
		caplines10[0].set_markersize(3)
		
		plt.plot(Group11["Hour"], Group11["CumulativeIndex"], Color=Color11, marker=",", linestyle="-")
		plotline11, caplines11, line11 = plt.errorbar(Group11["Hour"], Group11["CumulativeIndex"], yerr=Group11["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines11[0].set_marker('_')
		caplines11[0].set_markersize(3)
		
		plt.plot(Group12["Hour"], Group12["CumulativeIndex"], Color=Color12, marker=",", linestyle="-")
		plotline12, caplines12, line12 = plt.errorbar(Group12["Hour"], Group12["CumulativeIndex"], yerr=Group12["Error"],  fmt='none', ecolor="black", elinewidth=1, capsize=1, lolims=True)
		caplines12[0].set_marker('_')
		caplines12[0].set_markersize(3)
		
		plt.title("Cumulative Learning Index by Hour", fontsize=20)
		plt.xlabel("Hour", fontsize=16)
		plt.ylabel("Cumulative Index", fontsize=16)
		plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
		plt.yticks([-1, -0.75, -0.50, -0.25, 0, 0.25, 0.50, 0.75, 1])
		plt.axvspan(3, 15, alpha=0.5, color="lightgray")
		plt.axvspan(27, 39, alpha=0.5, color="lightgray")
		plt.axvspan(51, 63, alpha=0.5, color="lightgray")
		plt.axvspan(75, 87, alpha=0.5, color="lightgray")
		plt.legend([treatment1 + " (n=" + G1N + ")", treatment2 + " (n=" + G2N + ")", treatment3 + " (n=" + G3N + ")", treatment4 + " (n=" + G4N + ")", treatment5 + " (n=" + G5N + ")", treatment6 + " (n=" + G6N + ")", treatment7 + " (n=" + G7N + ")", treatment8 + " (n=" + G8N + ")", treatment9 + " (n=" + G9N + ")", treatment10 + " (n=" + G10N + ")", treatment11 + " (n=" + G11N + ")", treatment12 + " (n=" + G12N + ")"], fontsize=8)
		plt.savefig(directory0 + "Graphs/cumulativeindex" + today + ".jpg")
		
