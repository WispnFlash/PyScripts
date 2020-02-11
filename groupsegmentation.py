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
treatment11 = "A treatment group"
treatment12 = "A treatment group"
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
Color11 = "black"
Color12 = "black"
directory0 = maindirectory + investigator + "/Data/Segmentation/Frequency/"

def SegmentDistribution(grouplocation):
	os.chdir(grouplocation)
	animals = os.listdir()
	numberofanimals = len(animals)
	Distance = np.full((240, 1), 0, dtype='float32')
	Frequency = np.full((240, 1), 0, dtype='float32')
	number = len(directory0)
	groupname = grouplocation[number:(len(grouplocation)-1)]
	print(groupname)
	dataset = None
	for i in animals:
		if dataset is not None:
			temp = pd.read_csv(i)
			dataset = pd.concat([dataset, temp], axis=0)
		if dataset is None:
			dataset = pd.read_csv(i)
	rangeStart = -11.0
	rangeEnd = -10.9
	for j in range(0, 240):
		temp = dataset["Frequency"][(dataset["Distance"] >= rangeStart) & (dataset["Distance"] < rangeEnd)]
		if (len(temp) == 0):
			Frequency[j, 0] = Frequency[j-1, 0]
		if (len(temp) != 0):
			Frequency[j, 0] = temp.mean()
		Distance[j, 0] = rangeStart
		rangeStart = rangeStart + 0.100
		rangeEnd = rangeEnd + 0.100
		del temp
	array = np.concatenate((Distance, Frequency), axis=1)
	array = pd.DataFrame(array)
	GroupSegments = array
	GroupSegments.columns = ["Distance", "Frequency"]
	GroupSegments.to_csv(maindirectory + "Temp/" + groupname + "segmentfrequency.csv")
	print(groupname + " finished!")
	return GroupSegments



if (numberofgroups == 1):
	treatment1 = str(sys.argv[3])
	directory1 = directory0 + treatment1 + "/"
	Color1 = str(sys.argv[4])
	n1 = str(len(os.listdir(directory1)))
	group1 = SegmentDistribution(directory1)
	plt.plot(group1["Distance"], group1["Frequency"], Color1)
	plt.title(treatment1 + " Movement Segment Distribution ")
	plt.xlabel("Log2 of Distance moved (cm)")
	plt.ylabel("Frequency")
	plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
	plt.yticks([0, 100, 200, 300, 400, 500, 600])
	plt.legend([treatment1 + " (n=" + n1 + ")"])
	plt.show()
	plt.clf()
if (numberofgroups == 2):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	Color1 = str(sys.argv[5])
	Color2 = str(sys.argv[6])
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	groups = [directory1, directory2]
	value = 0
	if __name__=='__main__':
		pool = mp.Pool(processes=2)
		pool.map_async(SegmentDistribution, groups)
		pool.close()
		pool.join()
		value = 1
	if (value == 1):
		group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "segmentfrequency.csv")
		group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "segmentfrequency.csv")
		plt.plot(group1["Distance"], group1["Frequency"], Color1)
		plt.plot(group2["Distance"], group2["Frequency"], Color2)
		plt.title("Movement Segment Distribution ")
		plt.xlabel("Log2 of Distance moved (cm)")
		plt.ylabel("Frequency")
		plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
		plt.yticks([0, 100, 200, 300, 400, 500, 600])
		plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")"])
		plt.show()
		plt.clf()
if (numberofgroups == 3):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	Color1 = str(sys.argv[6])
	Color2 = str(sys.argv[7])
	Color3 = str(sys.argv[8])
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	groups = [directory1, directory2, directory3]
	value = 0
	if __name__=='__main__':
		pool = mp.Pool(processes=3)
		pool.map_async(SegmentDistribution, groups)
		pool.close()
		pool.join()
		value = 1
	if (value == 1):
		group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "segmentfrequency.csv")
		group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "segmentfrequency.csv")
		group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "segmentfrequency.csv")
		plt.plot(group1["Distance"], group1["Frequency"], Color1)
		plt.plot(group2["Distance"], group2["Frequency"], Color2)
		plt.plot(group3["Distance"], group3["Frequency"], Color3)
		plt.title("Movement Segment Distribution ")
		plt.xlabel("Log2 of Distance moved (cm)")
		plt.ylabel("Frequency")
		plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
		plt.yticks([0, 100, 200, 300, 400, 500, 600])
		plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")"])
		plt.show()
		plt.clf()
if (numberofgroups == 4):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	Color1 = str(sys.argv[7])
	Color2 = str(sys.argv[8])
	Color3 = str(sys.argv[9])
	Color4 = str(sys.argv[10])
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	groups = [directory1, directory2, directory3, directory4]
	value = 0
	if __name__=='__main__':
		pool = mp.Pool(processes=4)
		pool.map_async(SegmentDistribution, groups)
		pool.close()
		pool.join()
		value = 1
	if (value == 1):
		group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "segmentfrequency.csv")
		group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "segmentfrequency.csv")
		group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "segmentfrequency.csv")
		group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "segmentfrequency.csv")
		plt.plot(group1["Distance"], group1["Frequency"], Color1)
		plt.plot(group2["Distance"], group2["Frequency"], Color2)
		plt.plot(group3["Distance"], group3["Frequency"], Color3)
		plt.plot(group4["Distance"], group4["Frequency"], Color4)
		plt.title("Movement Segment Distribution ")
		plt.xlabel("Log2 of Distance moved (cm)")
		plt.ylabel("Frequency")
		plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
		plt.yticks([0, 100, 200, 300, 400, 500, 600])
		plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")"])
		plt.show()
		plt.clf()
if (numberofgroups == 5):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	directory5 = directory0 + treatment5 + "/"
	Color1 = str(sys.argv[8])
	Color2 = str(sys.argv[9])
	Color3 = str(sys.argv[10])
	Color4 = str(sys.argv[11])
	Color5 = str(sys.argv[12])
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	groups = [directory1, directory2, directory3, directory4, directory5]
	value = 0
	if __name__=='__main__':
		pool = mp.Pool(processes=4)
		pool.map_async(SegmentDistribution, groups)
		pool.close()
		pool.join()
		value = 1
	if (value == 1):
		group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "segmentfrequency.csv")
		group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "segmentfrequency.csv")
		group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "segmentfrequency.csv")
		group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "segmentfrequency.csv")
		group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "segmentfrequency.csv")
		plt.plot(group1["Distance"], group1["Frequency"], Color1)
		plt.plot(group2["Distance"], group2["Frequency"], Color2)
		plt.plot(group3["Distance"], group3["Frequency"], Color3)
		plt.plot(group4["Distance"], group4["Frequency"], Color4)
		plt.plot(group5["Distance"], group5["Frequency"], Color5)
		plt.title("Movement Segment Distribution ")
		plt.xlabel("Log2 of Distance moved (cm)")
		plt.ylabel("Frequency")
		plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
		plt.yticks([0, 100, 200, 300, 400, 500, 600])
		plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")"])
		plt.show()
		plt.clf()
if (numberofgroups == 6):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	directory5 = directory0 + treatment5 + "/"
	directory6 = directory0 + treatment6 + "/"
	Color1 = str(sys.argv[9])
	Color2 = str(sys.argv[10])
	Color3 = str(sys.argv[11])
	Color4 = str(sys.argv[12])
	Color5 = str(sys.argv[13])
	Color6 = str(sys.argv[14])
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	n6 = str(len(os.listdir(directory6)))
	group1 = SegmentDistribution(directory1)
	group2 = SegmentDistribution(directory2)
	group3 = SegmentDistribution(directory3)
	group4 = SegmentDistribution(directory4)
	group5 = SegmentDistribution(directory5)
	group6 = SegmentDistribution(directory6)
	plt.plot(group1["Distance"], group1["Frequency"], Color1)
	plt.plot(group2["Distance"], group2["Frequency"], Color2)
	plt.plot(group3["Distance"], group3["Frequency"], Color3)
	plt.plot(group4["Distance"], group4["Frequency"], Color4)
	plt.plot(group5["Distance"], group5["Frequency"], Color5)
	plt.plot(group6["Distance"], group6["Frequency"], Color6)
	plt.title("Movement Segment Distribution ")
	plt.xlabel("Log2 of Distance moved (cm)")
	plt.ylabel("Frequency")
	plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
	plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400])
	plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")", treatment6 + " (n=" + n6 + ")"])
	plt.show()
	plt.clf()

if (numberofgroups == 7):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	directory5 = directory0 + treatment5 + "/"
	directory6 = directory0 + treatment6 + "/"
	directory7 = directory0 + treatment7 + "/"
	Color1 = str(sys.argv[10])
	Color2 = str(sys.argv[11])
	Color3 = str(sys.argv[12])
	Color4 = str(sys.argv[13])
	Color5 = str(sys.argv[14])
	Color6 = str(sys.argv[15])
	Color7 = str(sys.argv[16])
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	n6 = str(len(os.listdir(directory6)))
	n7 = str(len(os.listdir(directory7)))
	groups = [directory1, directory2, directory3, directory4, directory5, directory6, directory7]
	value = 0
	if __name__=='__main__':
		pool = mp.Pool(processes=4)
		pool.map_async(SegmentDistribution, groups)
		pool.close()
		pool.join()
		value = 1
	if (value == 1):
		group1 = pd.read_csv(maindirectory + "Temp/" + treatment1 + "segmentfrequency.csv")
		group2 = pd.read_csv(maindirectory + "Temp/" + treatment2 + "segmentfrequency.csv")
		group3 = pd.read_csv(maindirectory + "Temp/" + treatment3 + "segmentfrequency.csv")
		group4 = pd.read_csv(maindirectory + "Temp/" + treatment4 + "segmentfrequency.csv")
		group5 = pd.read_csv(maindirectory + "Temp/" + treatment5 + "segmentfrequency.csv")
		group6 = pd.read_csv(maindirectory + "Temp/" + treatment6 + "segmentfrequency.csv")
		group7 = pd.read_csv(maindirectory + "Temp/" + treatment7 + "segmentfrequency.csv")
		plt.plot(group1["Distance"], group1["Frequency"], Color1)
		plt.plot(group2["Distance"], group2["Frequency"], Color2)
		plt.plot(group3["Distance"], group3["Frequency"], Color3)
		plt.plot(group4["Distance"], group4["Frequency"], Color4)
		plt.plot(group5["Distance"], group5["Frequency"], Color5)
		plt.plot(group6["Distance"], group6["Frequency"], Color6)
		plt.plot(group7["Distance"], group7["Frequency"], Color7)
		plt.title("Movement Segment Distribution ")
		plt.xlabel("Log2 of Distance moved (cm)")
		plt.ylabel("Frequency")
		plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
		plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400])
		plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")", treatment6 + " (n=" + n6 + ")", treatment7 + " (n=" + n7 + ")"])
		plt.show()
		plt.clf()	
	
if (numberofgroups == 8):
	treatment1 = str(sys.argv[3])
	treatment2 = str(sys.argv[4])
	treatment3 = str(sys.argv[5])
	treatment4 = str(sys.argv[6])
	treatment5 = str(sys.argv[7])
	treatment6 = str(sys.argv[8])
	treatment7 = str(sys.argv[9])
	treatment8 = str(sys.argv[10])
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	directory5 = directory0 + treatment5 + "/"
	directory6 = directory0 + treatment6 + "/"
	directory7 = directory0 + treatment7 + "/"
	directory8 = directory0 + treatment8 + "/"
	Color1 = str(sys.argv[11])
	Color2 = str(sys.argv[12])
	Color3 = str(sys.argv[13])
	Color4 = str(sys.argv[14])
	Color5 = str(sys.argv[15])
	Color6 = str(sys.argv[16])
	Color7 = str(sys.argv[17])
	Color8 = str(sys.argv[18])
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	n6 = str(len(os.listdir(directory6)))
	n7 = str(len(os.listdir(directory7)))
	n8 = str(len(os.listdir(directory8)))
	group1 = SegmentDistribution(directory1)
	group2 = SegmentDistribution(directory2)
	group3 = SegmentDistribution(directory3)
	group4 = SegmentDistribution(directory4)
	group5 = SegmentDistribution(directory5)
	group6 = SegmentDistribution(directory6)
	group7 = SegmentDistribution(directory7)
	group8 = SegmentDistribution(directory8)
	plt.plot(group1["Distance"], group1["Frequency"], Color1)
	plt.plot(group2["Distance"], group2["Frequency"], Color2)
	plt.plot(group3["Distance"], group3["Frequency"], Color3)
	plt.plot(group4["Distance"], group4["Frequency"], Color4)
	plt.plot(group5["Distance"], group5["Frequency"], Color5)
	plt.plot(group6["Distance"], group6["Frequency"], Color6)
	plt.plot(group7["Distance"], group7["Frequency"], Color7)
	plt.plot(group8["Distance"], group8["Frequency"], Color8)
	plt.title("Movement Segment Distribution ")
	plt.xlabel("Log2 of Distance moved (cm)")
	plt.ylabel("Frequency")
	plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
	plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400])
	plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")", treatment6 + " (n=" + n6 + ")", treatment7 + " (n=" + n7 + ")", treatment8 + " (n=" + n8 + ")", treatment9 + " (n=" + n9 + ")"])
	plt.show()
	plt.clf()	
	
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
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	directory5 = directory0 + treatment5 + "/"
	directory6 = directory0 + treatment6 + "/"
	directory7 = directory0 + treatment7 + "/"
	directory8 = directory0 + treatment8 + "/"
	directory9 = directory0 + treatment9 + "/"
	Color1 = str(sys.argv[12])
	Color2 = str(sys.argv[13])
	Color3 = str(sys.argv[14])
	Color4 = str(sys.argv[15])
	Color5 = str(sys.argv[16])
	Color6 = str(sys.argv[17])
	Color7 = str(sys.argv[18])
	Color8 = str(sys.argv[19])
	Color9 = str(sys.argv[20])
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	n6 = str(len(os.listdir(directory6)))
	n7 = str(len(os.listdir(directory7)))
	n8 = str(len(os.listdir(directory8)))
	n9 = str(len(os.listdir(directory9)))
	group1 = SegmentDistribution(directory1)
	group2 = SegmentDistribution(directory2)
	group3 = SegmentDistribution(directory3)
	group4 = SegmentDistribution(directory4)
	group5 = SegmentDistribution(directory5)
	group6 = SegmentDistribution(directory6)
	group7 = SegmentDistribution(directory7)
	group8 = SegmentDistribution(directory8)
	group9 = SegmentDistribution(directory9)
	plt.plot(group1["Distance"], group1["Frequency"], Color1)
	plt.plot(group2["Distance"], group2["Frequency"], Color2)
	plt.plot(group3["Distance"], group3["Frequency"], Color3)
	plt.plot(group4["Distance"], group4["Frequency"], Color4)
	plt.plot(group5["Distance"], group5["Frequency"], Color5)
	plt.plot(group6["Distance"], group6["Frequency"], Color6)
	plt.plot(group7["Distance"], group7["Frequency"], Color7)
	plt.plot(group8["Distance"], group8["Frequency"], Color8)
	plt.plot(group9["Distance"], group9["Frequency"], Color9)
	plt.title("Movement Segment Distribution ")
	plt.xlabel("Log2 of Distance moved (cm)")
	plt.ylabel("Frequency")
	plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
	plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400])
	plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")", treatment6 + " (n=" + n6 + ")", treatment7 + " (n=" + n7 + ")", treatment8 + " (n=" + n8 + ")", treatment9 + " (n=" + n9 + ")"])
	plt.show()
	plt.clf()	
	
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
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	directory5 = directory0 + treatment5 + "/"
	directory6 = directory0 + treatment6 + "/"
	directory7 = directory0 + treatment7 + "/"
	directory8 = directory0 + treatment8 + "/"
	directory9 = directory0 + treatment9 + "/"
	directory10 = directory0 + treatment10 + "/"
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
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	n6 = str(len(os.listdir(directory6)))
	n7 = str(len(os.listdir(directory7)))
	n8 = str(len(os.listdir(directory8)))
	n9 = str(len(os.listdir(directory9)))
	n10 = str(len(os.listdir(directory10)))
	group1 = SegmentDistribution(directory1)
	group2 = SegmentDistribution(directory2)
	group3 = SegmentDistribution(directory3)
	group4 = SegmentDistribution(directory4)
	group5 = SegmentDistribution(directory5)
	group6 = SegmentDistribution(directory6)
	group7 = SegmentDistribution(directory7)
	group8 = SegmentDistribution(directory8)
	group9 = SegmentDistribution(directory9)
	group10 = SegmentDistribution(directory10)
	plt.plot(group1["Distance"], group1["Frequency"], Color1)
	plt.plot(group2["Distance"], group2["Frequency"], Color2)
	plt.plot(group3["Distance"], group3["Frequency"], Color3)
	plt.plot(group4["Distance"], group4["Frequency"], Color4)
	plt.plot(group5["Distance"], group5["Frequency"], Color5)
	plt.plot(group6["Distance"], group6["Frequency"], Color6)
	plt.plot(group7["Distance"], group7["Frequency"], Color7)
	plt.plot(group8["Distance"], group8["Frequency"], Color8)
	plt.plot(group9["Distance"], group9["Frequency"], Color9)
	plt.plot(group10["Distance"], group10["Frequency"], Color10)
	plt.title("Movement Segment Distribution ")
	plt.xlabel("Log2 of Distance moved (cm)")
	plt.ylabel("Frequency")
	plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
	plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400])
	plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")", treatment6 + " (n=" + n6 + ")", treatment7 + " (n=" + n7 + ")", treatment8 + " (n=" + n8 + ")", treatment9 + " (n=" + n9 + ")", treatment10 + " (n=" + n10 + ")"])
	plt.show()
	plt.clf()	
	
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
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	directory5 = directory0 + treatment5 + "/"
	directory6 = directory0 + treatment6 + "/"
	directory7 = directory0 + treatment7 + "/"
	directory8 = directory0 + treatment8 + "/"
	directory9 = directory0 + treatment9 + "/"
	directory10 = directory0 + treatment10 + "/"
	directory11 = directory0 + treatment11 + "/"
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
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	n6 = str(len(os.listdir(directory6)))
	n7 = str(len(os.listdir(directory7)))
	n8 = str(len(os.listdir(directory8)))
	n9 = str(len(os.listdir(directory9)))
	n10 = str(len(os.listdir(directory10)))
	n11 = str(len(os.listdir(directory11)))
	group1 = SegmentDistribution(directory1)
	group2 = SegmentDistribution(directory2)
	group3 = SegmentDistribution(directory3)
	group4 = SegmentDistribution(directory4)
	group5 = SegmentDistribution(directory5)
	group6 = SegmentDistribution(directory6)
	group7 = SegmentDistribution(directory7)
	group8 = SegmentDistribution(directory8)
	group9 = SegmentDistribution(directory9)
	group10 = SegmentDistribution(directory10)
	group11 = SegmentDistribution(directory11)
	plt.plot(group1["Distance"], group1["Frequency"], Color1)
	plt.plot(group2["Distance"], group2["Frequency"], Color2)
	plt.plot(group3["Distance"], group3["Frequency"], Color3)
	plt.plot(group4["Distance"], group4["Frequency"], Color4)
	plt.plot(group5["Distance"], group5["Frequency"], Color5)
	plt.plot(group6["Distance"], group6["Frequency"], Color6)
	plt.plot(group7["Distance"], group7["Frequency"], Color7)
	plt.plot(group8["Distance"], group8["Frequency"], Color8)
	plt.plot(group9["Distance"], group9["Frequency"], Color9)
	plt.plot(group10["Distance"], group10["Frequency"], Color10)
	plt.plot(group11["Distance"], group11["Frequency"], Color11)
	plt.title("Movement Segment Distribution ")
	plt.xlabel("Log2 of Distance moved (cm)")
	plt.ylabel("Frequency")
	plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
	plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400])
	plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")", treatment6 + " (n=" + n6 + ")", treatment7 + " (n=" + n7 + ")", treatment8 + " (n=" + n8 + ")", treatment9 + " (n=" + n9 + ")", treatment10 + " (n=" + n10 + ")", treatment11 + " (n=" + n11 + ")"])
	plt.show()
	plt.clf()	
	
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
	directory1 = directory0 + treatment1 + "/"
	directory2 = directory0 + treatment2 + "/"
	directory3 = directory0 + treatment3 + "/"
	directory4 = directory0 + treatment4 + "/"
	directory5 = directory0 + treatment5 + "/"
	directory6 = directory0 + treatment6 + "/"
	directory7 = directory0 + treatment7 + "/"
	directory8 = directory0 + treatment8 + "/"
	directory9 = directory0 + treatment9 + "/"
	directory10 = directory0 + treatment10 + "/"
	directory11 = directory0 + treatment11 + "/"
	directory12 = directory0 + treatment12 + "/"
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
	n1 = str(len(os.listdir(directory1)))
	n2 = str(len(os.listdir(directory2)))
	n3 = str(len(os.listdir(directory3)))
	n4 = str(len(os.listdir(directory4)))
	n5 = str(len(os.listdir(directory5)))
	n6 = str(len(os.listdir(directory6)))
	n7 = str(len(os.listdir(directory7)))
	n8 = str(len(os.listdir(directory8)))
	n9 = str(len(os.listdir(directory9)))
	n10 = str(len(os.listdir(directory10)))
	n11 = str(len(os.listdir(directory11)))
	n12 = str(len(os.listdir(directory12)))
	group1 = SegmentDistribution(directory1)
	group2 = SegmentDistribution(directory2)
	group3 = SegmentDistribution(directory3)
	group4 = SegmentDistribution(directory4)
	group5 = SegmentDistribution(directory5)
	group6 = SegmentDistribution(directory6)
	group7 = SegmentDistribution(directory7)
	group8 = SegmentDistribution(directory8)
	group9 = SegmentDistribution(directory9)
	group10 = SegmentDistribution(directory10)
	group11 = SegmentDistribution(directory11)
	group12 = SegmentDistribution(directory12)
	plt.plot(group1["Distance"], group1["Frequency"], Color1)
	plt.plot(group2["Distance"], group2["Frequency"], Color2)
	plt.plot(group3["Distance"], group3["Frequency"], Color3)
	plt.plot(group4["Distance"], group4["Frequency"], Color4)
	plt.plot(group5["Distance"], group5["Frequency"], Color5)
	plt.plot(group6["Distance"], group6["Frequency"], Color6)
	plt.plot(group7["Distance"], group7["Frequency"], Color7)
	plt.plot(group8["Distance"], group8["Frequency"], Color8)
	plt.plot(group9["Distance"], group9["Frequency"], Color9)
	plt.plot(group10["Distance"], group10["Frequency"], Color10)
	plt.plot(group11["Distance"], group11["Frequency"], Color11)
	plt.plot(group12["Distance"], group12["Frequency"], Color12)
	plt.title("Movement Segment Distribution ")
	plt.xlabel("Log2 of Distance moved (cm)")
	plt.ylabel("Frequency")
	plt.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
	plt.yticks([0, 200, 400, 600, 800, 1000, 1200, 1400])
	plt.legend([treatment1 + " (n=" + n1 + ")", treatment2 + " (n=" + n2 + ")", treatment3 + " (n=" + n3 + ")", treatment4 + " (n=" + n4 + ")", treatment5 + " (n=" + n5 + ")", treatment6 + " (n=" + n6 + ")", treatment7 + " (n=" + n7 + ")", treatment8 + " (n=" + n8 + ")", treatment9 + " (n=" + n9 + ")", treatment10 + " (n=" + n10 + ")", treatment11 + " (n=" + n11 + ")", treatment12 + " (n=" + n12 + ")"])
	plt.show()
	plt.clf()
