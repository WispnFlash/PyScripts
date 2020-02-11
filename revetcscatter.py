import pandas as pd
import multiprocessing as mp
import numpy as np
import os
import sys
import matplotlib.pyplot as plt


maindirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
investigator = str(sys.argv[1])
numberofgroups = int(sys.argv[2])

treatment1 = "A treatment group"
treatment2 = "A treatment group"
treatment3 = "A treatment group"
treatment4 = "A treatment group"
treatment5 = "A treatment group"
treatment6 = "A treatment group"
treatment7 = "A treatment group"
treatment8 = "A treatment group"
treatment9 = "A treatment group"
treatment10 = "A treatment group"

Color1 = "A treatment color"
Color2 = "A treatment color"
Color3 = "A treatment color"
Color4 = "A treatment color"
Color5 = "A treatment color"
Color6 = "A treatment color"
Color7 = "A treatment color"
Color8 = "A treatment color"
Color9 = "A treatment color"
Color10 = "A treatment color"

directory0 = maindirectory + investigator + "/"


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

	

if (numberofgroups == 1):
	treatment1 = str(sys.argv[3])
	Color1 = str(sys.argv[4])
	directory1 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment1 + "/"
	Group1 = CreateCohort(directory1)
	n1 = str(len(os.listdir(directory1)))
	plt.scatter(Group1["Treatment"], Group1["EntriestoEighty"], s=9, c=Color1)
	plt.title("Reversal - Entries to 80% criterion scatterplot")
	plt.ylabel("Entries to reach 80% criterion")
	plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000])
	"""plt.legend([treatment1 + " (n=" + n1 + ")"])"""
	plt.show()
if (numberofgroups == 2):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	Color1 = str(sys.argv[5])
	Color2 = str(sys.argv[6])
	directory1 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment1 + "/"
	directory2 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment2 + "/"
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	groups = pd.concat([Group1, Group2], axis=0)
	groups.to_csv(directory0 + "RevETCforallgroups.csv")
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	plt.scatter(Group1["Treatment"], Group1["EntriestoEighty"], s=9, c=Color1)
	plt.scatter(Group2["Treatment"], Group2["EntriestoEighty"], s=9, c=Color2)
	plt.title("Reversal - Entries to 80% criterion scatterplot")
	plt.ylabel("Entries to reach 80% criterion")
	plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000])
	"""plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")"])"""
	plt.show()	
if (numberofgroups == 3):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	Color1 = str(sys.argv[6])
	Color2 = str(sys.argv[7])
	Color3 = str(sys.argv[8])
	directory1 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment1 + "/"
	directory2 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment2 + "/"
	directory3 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment3 + "/"
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	groups = pd.concat([Group1, Group2, Group3], axis=0)
	groups.to_csv(directory0 + "RevETCforallgroups.csv")
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	plt.scatter(Group1["Treatment"], Group1["EntriestoEighty"], s=9, c=Color1)
	plt.scatter(Group2["Treatment"], Group2["EntriestoEighty"], s=9, c=Color2)
	plt.scatter(Group3["Treatment"], Group3["EntriestoEighty"], s=9, c=Color3)
	plt.title("Reversal - Entries to 80% criterion scatterplot")
	plt.ylabel("Entries to reach 80% criterion")
	plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000])
	"""plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")"])"""
	plt.show()
if (numberofgroups == 4):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	Color1 = str(sys.argv[7])
	Color2 = str(sys.argv[8])
	Color3 = str(sys.argv[9])
	Color4 = str(sys.argv[10])
	directory1 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment1 + "/"
	directory2 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment2 + "/"
	directory3 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment3 + "/"
	directory4 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment4 + "/"
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	groups = pd.concat([Group1, Group2, Group3, Group4], axis=0)
	groups.to_csv(directory0 + "RevETCforallgroups.csv")
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	
	plt.scatter(Group1["Treatment"], Group1["EntriestoEighty"], s=9, c=Color1)
	plt.scatter(Group2["Treatment"], Group2["EntriestoEighty"], s=9, c=Color2)
	plt.scatter(Group3["Treatment"], Group3["EntriestoEighty"], s=9, c=Color3)
	plt.scatter(Group4["Treatment"], Group4["EntriestoEighty"], s=9, c=Color4)
	plt.title("Reversal - Entries to 80% criterion scatterplot")
	plt.ylabel("Entries to reach 80% criterion")
	plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000])
	"""plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")"])"""
	plt.show()
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
	directory1 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment1 + "/"
	directory2 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment2 + "/"
	directory3 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment3 + "/"
	directory4 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment4 + "/"
	directory5 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment5 + "/"
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	groups = pd.concat([Group1, Group2, Group3, Group4, Group5], axis=0)
	groups.to_csv(directory0 + "RevETCforallgroups.csv")
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	plt.scatter(Group1["Treatment"], Group1["EntriestoEighty"], s=9, c=Color1)
	plt.scatter(Group2["Treatment"], Group2["EntriestoEighty"], s=9, c=Color2)
	plt.scatter(Group3["Treatment"], Group3["EntriestoEighty"], s=9, c=Color3)
	plt.scatter(Group4["Treatment"], Group4["EntriestoEighty"], s=9, c=Color4)
	plt.scatter(Group5["Treatment"], Group5["EntriestoEighty"], s=9, c=Color5)
	plt.title("Reversal - Entries to 80% criterion scatterplot")
	plt.ylabel("Entries to reach 80% criterion")
	plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000])
	"""plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")"], bbox_to_anchor=(1,1))"""
	plt.show()
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
	directory1 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment1 + "/"
	directory2 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment2 + "/"
	directory3 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment3 + "/"
	directory4 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment4 + "/"
	directory5 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment5 + "/"
	directory6 = directory0 + "Data/Entries to Criterion/Reversal/" + treatment6 + "/"
	Group1 = CreateCohort(directory1)
	Group2 = CreateCohort(directory2)
	Group3 = CreateCohort(directory3)
	Group4 = CreateCohort(directory4)
	Group5 = CreateCohort(directory5)
	Group6 = CreateCohort(directory6)
	groups = pd.concat([Group1, Group2, Group3, Group4, Group5, Group6], axis=0)
	groups.to_csv(directory0 + "REVETCforallgroups.csv")
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	n6 = str(len(os.listdir(directory6)))
	plt.scatter(Group1["Treatment"], Group1["EntriestoEighty"], s=9, c=Color1)
	plt.scatter(Group2["Treatment"], Group2["EntriestoEighty"], s=9, c=Color2)
	plt.scatter(Group3["Treatment"], Group3["EntriestoEighty"], s=9, c=Color3)
	plt.scatter(Group4["Treatment"], Group4["EntriestoEighty"], s=9, c=Color4)
	plt.scatter(Group5["Treatment"], Group5["EntriestoEighty"], s=9, c=Color5)
	plt.scatter(Group6["Treatment"], Group6["EntriestoEighty"], s=9, c=Color6)
	plt.title("Reversal - Entries to 80% criterion scatterplot")
	plt.ylabel("Entries to reach 80% criterion")
	plt.yticks([0, 1000, 2000, 3000, 4000, 5000])
	"""plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")", treatment6 + " (n=" + n6 + ")"])"""
	plt.show()
