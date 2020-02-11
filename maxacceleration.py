import pandas as pd
import multiprocessing as mp
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

def Acceleration(grouplocation):
	os.chdir(grouplocation)
	animals = os.listdir()
	numberofanimals = len(animals)
	Hour = np.full((240, 1), 0, dtype='int64')
	Acceleration = np.full((240, 1), 0, dtype='float32')
	dataset = None
	for i in animals:
		if dataset is not None:
			temp = pd.read_csv(i)
			dataset = pd.concat([dataset, temp], axis=0)
		if dataset is None:
			dataset = pd.read_csv(i)
	interval = 1
	for j in range(0, 240):
		temp = dataset["Acceleration"][(dataset["Hour"] == interval)]	
		Hour[j, 0] = interval
		Acceleration[j, 0] = temp.mean()
		interval = interval + 1
		del temp
	array = np.concatenate((Hour, Acceleration), axis=1)
	array = pd.DataFrame(array)
	GroupAcc = array
	GroupAcc.columns = ["Hour", "Acceleration"]
	return GroupAcc


maindirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
investigator = str(sys.argv[1])
directory0 = maindirectory + investigator + "/Data/Segmentation/Acceleration/"
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
Color1 = "green"
Color2 = "blue"
Color3 = "orange"
Color4 = "yellow"
Color5 = "red"
Color6 = "brown"
Color7 = "black"
Color8 = "black"
Color9 = "black"
Color10 = "black"


if (numberofgroups == 1):
	treatment1 = str(sys.argv[3])
	Color1 = str(sys.argv[4])
	directory1 = directory0 + treatment1 + "/"
	group1 = Acceleration(directory1)
	plt.plot(group1["Hour"], group1["Acceleration"], Color1)
	plt.title(treatment1 + " Maximum Acceleration by Hour ")
	plt.xlabel("Hour")
	plt.ylabel("Acceleration (cm/s²)")
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 500, 1000, 1500, 2000])
	plt.legend([treatment1])
	plt.show()
	plt.clf()
if (numberofgroups == 2):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	Color1 = str(sys.argv[5])
	Color2 = str(sys.argv[6])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	group1 = Acceleration(directory1)
	group2 = Acceleration(directory2)
	plt.plot(group1["Hour"], group1["Acceleration"], Color1)
	plt.plot(group2["Hour"], group2["Acceleration"], Color2)
	plt.title("Maximum Acceleration by Hour ")
	plt.xlabel("Hour")
	plt.ylabel("Acceleration (cm/s²)")
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 500, 1000, 1500, 2000])
	plt.legend([treatment1, treatment2])
	plt.show()
	plt.clf()
if (numberofgroups == 3):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	Color1 = str(sys.argv[6])
	Color2 = str(sys.argv[7])
	Color3 = str(sys.argv[8])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	group1 = Acceleration(directory1)
	group2 = Acceleration(directory2)
	group3 = Acceleration(directory3)
	plt.plot(group1["Hour"], group1["Acceleration"], Color1)
	plt.plot(group2["Hour"], group2["Acceleration"], Color2)
	plt.plot(group3["Hour"], group3["Acceleration"], Color3)
	plt.title("Maximum Acceleration by Hour ")
	plt.xlabel("Hour")
	plt.ylabel("Acceleration (cm/s²)")
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 500, 1000, 1500, 2000])
	plt.legend([treatment1, treatment2, treatment3])
	plt.show()
	plt.clf()
if (numberofgroups == 4):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
if (numberofgroups == 5):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
if (numberofgroups == 6):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
if (numberofgroups == 7):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
if (numberofgroups == 8):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	treatment8 = str(sys.argv[10])
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

	
	
