import numpy as np
import pandas as pd
import math
import time
import os
import matplotlib.pyplot as plt		
import multiprocessing as mp		
import sys
import cv2 as cv
from numba import cuda
from numba import autojit
from numba import jit
os.environ['R_HOME'] = 'C:\Program Files\R\R-3.6.3'
os.environ['R_USER'] = 'C:\Python37\Lib\site-packages\rpy2'
from rpy2.robjects import pandas2ri
pandas2ri.activate()
import rpy2.robjects as ro
import datetime as dt

import warnings
warnings.filterwarnings("ignore")


inputdirectory = str(sys.argv[1])

def PrepDirectory(mouselocation):
	HeaderValue = FindHeader(mouselocation)
	AnimalID = FindAnimalID(mouselocation, HeaderValue)
	treatment = FindTreatment(mouselocation, HeaderValue)
	Treatment = FindTreatment(mouselocation, HeaderValue)
	investigator = FindInvestigator(mouselocation, HeaderValue)
	outputdirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
	directories = np.full(29, outputdirectory + investigator + "/Data/Indexes/Cumulative/Cumulative/Cumulative/")
	directories[0] = outputdirectory + investigator + "/"
	directories[1] = outputdirectory + investigator + "/Data/raw/" + Treatment + "/"
	directories[2] = outputdirectory + investigator + "/Data/Distance moved/" + Treatment + "/"
	directories[3] = outputdirectory + investigator + "/Data/Feeding/" + Treatment + "/"
	directories[4] = outputdirectory + investigator + "/Data/Initial Discrimination/" + Treatment + "/"
	directories[5] = outputdirectory + investigator + "/Data/Reversal/" + Treatment + "/"
	directories[6] = outputdirectory + investigator + "/Data/Entries to Criterion/Initial Discrimination/" + Treatment + "/"
	directories[7] = outputdirectory + investigator + "/Data/Entries to Criterion/Reversal/" + Treatment + "/"
	directories[8] = outputdirectory + investigator + "/Data/Segmentation/Acceleration/" + Treatment + "/"
	directories[9] = outputdirectory + investigator + "/Data/Segmentation/Frequency/" + Treatment + "/"
	directories[10] = outputdirectory + investigator + "/Data/Segmentation/fromR/" + Treatment + "/"
	directories[11] = outputdirectory + investigator + "/Data/Segmentation/Graphs/Acceleration/" + Treatment + "/"
	directories[12] = outputdirectory + investigator + "/Data/Segmentation/Graphs/Distribution/" + Treatment + "/"
	directories[13] = outputdirectory + investigator + "/Data/Segmentation/Moving Segments/" + Treatment + "/"
	directories[14] = outputdirectory + investigator + "/Data/Segmentation/PreSegmentation/" + Treatment + "/"
	directories[15] = outputdirectory + investigator + "/Data/Segmentation/raw/" + Treatment + "/"
	directories[16] = outputdirectory + investigator + "/Graphs/Individual mice/Acceleration/" + Treatment + "/"
	directories[17] = outputdirectory + investigator + "/Graphs/Individual mice/Entry Choice/" + Treatment + "/"
	directories[18] = outputdirectory + investigator + "/Graphs/Individual mice/Feeding/Independent/" + Treatment + "/"
	directories[19] = outputdirectory + investigator + "/Graphs/Individual mice/Feeding/Cumulative/" + Treatment + "/"
	directories[20] = outputdirectory + investigator + "/Graphs/Individual mice/Figures/" + Treatment + "/"
	directories[21] = outputdirectory + investigator + "/Graphs/Individual mice/Indexes/Independent/" + Treatment + "/"
	directories[22] = outputdirectory + investigator + "/Graphs/Individual mice/Indexes/Cumulative/" + Treatment + "/"
	directories[23] = outputdirectory + investigator + "/Graphs/Individual mice/Movement/Independent/" + Treatment + "/"
	directories[24] = outputdirectory + investigator + "/Graphs/Individual mice/Movement/Cumulative/" + Treatment + "/"
	directories[25] = outputdirectory + investigator + "/Graphs/Individual mice/Segmentation/" + Treatment + "/"
	directories[26] = outputdirectory + investigator + "/Data/Indexes/Independent/" + Treatment + "/"
	directories[27] = outputdirectory + investigator + "/Data/Indexes/Cumulative/" + Treatment + "/"
	directories[28] = outputdirectory + investigator + "/Treatments/"
	for v in directories:
		if (os.path.isdir(v) == False):
			os.makedirs(v)
	TreatmentFile = open(directories[28] + Treatment + ".txt", "w+")
	TreatmentFile.write("Treatment: " + Treatment + "\n")
	TreatmentFile.write("Investigator: " + investigator + "\n")
	TreatmentFile.close()

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

def FindPhenNumber(textfile, header):
	mouseText = open(textfile, "r")
	Phen = "00"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:13] == "PhenoTyperID"):
			Phen = current[16:(len(current)-3)]
			break
		count = count + 1
	mouseText.close()
	return Phen
	
	
def FindAnimalID(textfile, header):
	mouseText = open(textfile, "r")
	AnimalID = "mouse????????"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:9] == "AnimalID"):
			AnimalID = current[12:(len(current)-3)]
			break
		count = count + 1
	mouseText.close()
	return AnimalID
	
def FindStrain(textfile, header):
	mouseText = open(textfile, "r")
	strain = "Unknown Strain"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:7] == "Strain"):
			strain = current[10:(len(current)-3)]
			break
		count = count + 1
	mouseText.close()
	return strain
	
def FindDOB(textfile, header):
	mouseText = open(textfile, "r")
	dob = "00/00/0000"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:14] == "Date of Birth"):
			dob = current[17:27]
			break
		count = count + 1
	mouseText.close()
	return dob	
	
def FindRD(textfile, header):
	mouseText = open(textfile, "r")
	rd = "00/00/0000"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:11] == "Start time"):
			rd = current[14:24]
			break
		count = count + 1
	mouseText.close()
	return rd
	
def CalculateAge(dateofbirth, rundate):
	months = 0.0
	try: 
		dob = dt.datetime(int(dateofbirth[6:10]), int(dateofbirth[0:2]), int(dateofbirth[3:5]))
		rd = dt.datetime(int(rundate[6:10]), int(rundate[0:2]), int(rundate[3:5]))
		duration = rd - dob
		days = duration.days
		months = int(days / 30)
	except:
		months = 0.0
	return months
	
def FindCageCard(textfile, header):
	mouseText = open(textfile, "r")
	cc = "00000000"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:12] == "Cage Card #"):
			cc = current[15:(len(current)-3)]
			break
		count = count + 1
	mouseText.close()
	return cc
	
def FindGender(textfile, header):
	mouseText = open(textfile, "r")
	gender = "Unknown Gender"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:7] == "Gender"):
			gender = current[10:(len(current)-3)]
			break
		count = count + 1
	mouseText.close()
	return gender
	
def FindTreatment(textfile, header):
	mouseText = open(textfile, "r")
	Treatment = "Unknown treatment"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:10] == "Treatment"):
			Treatment = current[13:(len(current)-3)]
			break
		count = count + 1
	mouseText.close()
	return Treatment

def FindPreWeight(textfile, header):
	mouseText = open(textfile, "r")
	prw = 0.00
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:10] == "PreWeight"):
			prw = float(current[13:(len(current)-3)])
			break
		count = count + 1
	mouseText.close()
	return prw
	
def FindPostWeight(textfile, header):
	mouseText = open(textfile, "r")
	pow = 0.00
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:11] == "PostWeight"):
			pow = float(current[14:(len(current)-3)])
			break
		count = count + 1
	mouseText.close()
	return pow
	
def CalculateWeightChange(pre, post):
	percentweightchange = 0.00
	try :
		percentweightchange = -((pre-post)/pre)*100
	except ZeroDivisionError:
		percentweightchange = 0.00
	return percentweightchange
	
def FindInvestigator(textfile, header):
	mouseText = open(textfile, "r")
	Investigator = "Unknown Investigator"
	count = 0
	while(count < header):
		current = mouseText.readline()
		if (current[1:13] == "Investigator"):
			Investigator = current[16:(len(current)-3)]
			break
		count = count + 1
	mouseText.close()
	return Investigator


 
def movingwindow(ar, number, outputarray):
    for x in range(0, number):
        value1 = 0.0
        value2 = 0.0
        if (x < 20):
            outputarray[x] = 0.0
        if (x == 29):
            for y in range(0, 30):
                value1 = value1 + ar[y]
            outputarray[x] = value1 / 30 
        if (x > 29):
            start = x - 29
            end = x + 1
            for z in range(start, end):
                value2 = value2 + ar[z]
            outputarray[x] = value2 / 30 
 
 
def ChangedCriterion(arr, number, outputarray2):
    value = 0
    for element in range(0, number):
        if ((arr[element] == 0.10) & (value <= 0.10)):
            value = 0.10    
        if ((arr[element] == 0.20) & (value <= 0.20)):
            value = 0.20    
        if ((arr[element] == 0.30) & (value <= 0.30)):
            value = 0.30    
        if ((arr[element] == 0.40) & (value <= 0.40)):
            value = 0.40    
        if ((arr[element] == 0.50) & (value <= 0.50)):
            value = 0.50    
        if ((arr[element] == 0.60) & (value <= 0.60)):
            value = 0.60    
        if ((arr[element] == 0.70) & (value <= 0.70)):
            value = 0.70    
        if ((arr[element] == 0.80) & (value <= 0.80)):
            value = 0.80         
        if ((arr[element] == 0.90) & (value <= 0.90)):
            value = 0.90    
        if (arr[element] == 1.0):
            value = 1.0
        outputarray2[element] = value
 
def ETCSeventyfinder(ar, ar2, number):
    counter1 = 0
    for member in range(0, number):
        if ((ar[member] == 0.70) & (counter1 == 0)):
            output1 = ar2[member]
            counter1 = 1
    if (counter1 == 0):
        output1 = 6000
    return output1
 
def ETCEightyfinder(ar, ar2, number):
    counter2 = 0
    for member in range(0, number):
        if ((ar[member] == 0.80) & (counter2 == 0)):
            output2 = ar2[member]
            counter2 = 1
    if (counter2 == 0):
        output2 = 6000
    return output2
 
def ETCNinetyfinder(ar, ar2, number):
    counter3 = 0
    for member in range(0, number):
        if ((ar[member] == 0.90) & (counter3 == 0)):
            output3 = ar2[member]
            counter3 = 1
    if (counter3 == 0):
        output3 = 6000
    return output3
 
def HourstoCriterion(entries, array, value):
    hours = 48
    if (value == 1):
        if (entries != 6000):
            hours = array[entries-1] / 3600
    if (value == 2):
        if (entries != 6000):
            hours = array[entries-1] / 3600 - 48
    return hours

def Qualifier(ar, number):
    for u in range(0, 6000):
        if (u < number-1):
            ar[u] = 0
        if (u >= number-1):
            ar[u] = 1
 
def SecondsToHours(ar, number):
    ar2 = np.zeros(number)
    for y in range(0, number):
        ar2[y] = ar[y] / 3600
    return ar2
 
 
def IndexFunction(ar1, ar2, ar3):
    outputarray = np.zeros(89)
    for v in range(0, 49):
        left = int(ar1[v])
        middle = int(ar2[v])
        right = int(ar3[v])
        difference = left - (middle + right)
        total = left + middle + right
        if (total == 0):
            outputarray[v] = 0
        if (total != 0):
            outputarray[v] = difference / total
    for y in range(49, 89):
        left = int(ar1[y])
        middle = int(ar2[y])
        right = int(ar3[y])
        difference = right - (left + middle)
        total = left + middle + right
        if (total == 0):
            outputarray[y] = 0
        if (total != 0):
            outputarray[y] = difference / total
    return outputarray
	
def Prep(mouse):
	mousePrep = mouse[["Recording time", "X center", "Y center", "Distance moved", "In zone(InShelter / center-point)"]]
	mousePrep.columns = ["Time", "X", "Y", "Distance moved", "InShelter"]
	return mousePrep

def RunningMedian(mouseframe):
	ro.globalenv['mouseR'] = pandas2ri.py2ri(mouseframe)
	ro.r('''
	mouseR = na.omit(mouseR)
	mouseR$X = runmed(mouseR$X, k=61, endrule="median")
	mouseR$X = runmed(mouseR$X, k=59, endrule="median")
	mouseR$X = runmed(mouseR$X, k=57, endrule="median")
	mouseR$X = runmed(mouseR$X, k=57, endrule="median")
	mouseR$Y = runmed(mouseR$Y, k=61, endrule="median")
	mouseR$Y = runmed(mouseR$Y, k=59, endrule="median")
	mouseR$Y = runmed(mouseR$Y, k=57, endrule="median")
	mouseR$Y = runmed(mouseR$Y, k=57, endrule="median")
	''')
	mouseR = ro.globalenv['mouseR']
	Rmouse = pandas2ri.ri2py(mouseR)
	Rmouse.columns = ["Time", "X", "Y", "Distance moved", "InShelter"]
	return Rmouse


def FindMaxVelocity(array, a):
	maxValue = 0
	max = 0
	size = len(array)
	for i in range(0, a+1):
		if (array[i] > maxValue):
			maxValue = array[i]
			max = i
	return max

def TimeElapsed(AnimalID, start, end):
	elapsed = end - start
	elapsed2 = ""
	if (elapsed < 60):
		elapsed2 = str(elapsed) + " seconds"
	if (elapsed >= 60):
		elapsed2 = str(elapsed/60) + " minutes"
	elapsed2 = AnimalID + " completed in " + elapsed2
	return elapsed2


#Time is column 0
#X is column 1
#Y is column 2
#Distance moved is column 3
#InShelter is column 4
#Segment type is column 5	
	
@jit(nopython=True)	
def Result(array, size):
	for i in range(0, size):
		if (array[i, 4] == 1):
			array[i, 5] = 0
		if (array[i, 4] == 0):
			if (i==0):
				array[i, 5] = 2
			if (i > 0):
				if (((array[i, 1] == array[i-1, 1]) & (array[i, 2] == array[i-1, 2])) == True):
					array[i, 5] = 1
				if (((array[i, 1] == array[i-1, 1]) & (array[i, 2] == array[i-1, 2])) == False):
					array[i, 5] = 2		
	return array
					
@jit(nopython=True)	
def WindowLength(array, size):
	segmenttype2 = np.full(size, 5)
	j = 0
	number = size-2
	while (j < number):	
		if (array[j, 5] != 2):
			if (array[j, 5] == 0):
				if (((array[j, 5] == 0) & (array[j+1, 5] == 0) & (array[j+2, 5] == 0)) == True):			
					segmenttype2[j] = 0
					segmenttype2[j+1] = 0
					segmenttype2[j+2] = 0
					j = j + 2
					if (j >= number):
						break;
				if (((array[j, 5] == 0) & (array[j+1, 5] == 0) & (array[j+2, 5] == 0)) == False):			
					if ((array[j+1, 5] != 0) & (array[j+1, 5] != 1)):
						j = j + 1
						if ((array[j+2, 5] != 0) & (array[j+2, 5] != 1)):
							j = j + 1
			if (array[j, 5] == 1):
				if (((array[j, 5] == 1) & (array[j+1, 5] == 1) & (array[j+2, 5] == 1)) == True):			
					segmenttype2[j] = 1
					segmenttype2[j+1] = 1
					segmenttype2[j+2] = 1		
					j = j + 2
					if (j >= number):
						break;
				if (((array[j, 5] == 1) & (array[j+1, 5] == 1) & (array[j+2, 5] == 1)) == False):			
					if ((array[j+1, 5] != 0) & (array[j+1, 5] != 1)):
						j = j + 1
						if ((array[j+2, 5] != 0) & (array[j+2, 5] != 1)):
							j = j + 1
		j = j + 1
	segmenttype2[segmenttype2 == 5] = 2
	segmenttype2.reshape(-1,1)
	array[:, 5] = segmenttype2
	return array

	

#distancemoved is column 0
#timespentmoving is column 1
#timepoints is column 2 
#MaxVelocity is column 3 
#MaxAcceleration is column 4 
	
#Shelter = 0
#Arrest  = 1
#Moving  = 2


def Activity(mousearray, size):
	segmentation = np.full((size, 5), 0, dtype="float32")
	p = 0
	q = 0
	a = 0
	counter = 0
	value = 0
	VelocityTemp = np.zeros(size)
	frame = 1 / 15
	for i in range(0, size):
		if (i == 0):
			if (mousearray[i, 5] == 2):	
				segmentation[p, 0] = segmentation[p, 0] + mousearray[i, 3]
				timestart = mousearray[0, 0]
				VelocityTemp[a] = mousearray[0, 6]
				a = a + 1
		if (i > 0):
			if ((mousearray[i, 5] == 2) & (value == 1)):	
				segmentation[p, 0] = segmentation[p, 0] + mousearray[i, 3]
				VelocityTemp[a] = mousearray[i, 6]
				a = a + 1
			if ((mousearray[i, 5] == 2) & (value == 0)):	
				segmentation[p, 0] = mousearray[i, 3]
				timestart = mousearray[i, 0]
				segmentation[p, 2] = timestart
				VelocityTemp[a] = mousearray[i, 6]
				value = 1
				a = a + 1
			if ((mousearray[i, 5] != 2) & (mousearray[i-1, 5] == 2)):
				timeend = mousearray[i, 0]
				segmentation[p, 1] = timeend - timestart
				Max = FindMaxVelocity(VelocityTemp, a)
				segmentation[p, 3] = VelocityTemp[Max]
				segmentation[p, 4] = VelocityTemp[Max] / ((Max+1)*frame)
				p = p + 1
				counter = counter + 1
				value = 0
				a = 0
				VelocityTemp = np.zeros(size)
	segmentation = segmentation[0:counter, :]
	return segmentation
	
	
def MovFrequency(inputframe):
	minimum = -10
	minimum = round(minimum)-1
	maximum = inputframe["Distance moved"].max()	
	maximum = 12
	interval = 0.1;
	divider = int(1/interval)
	valuesrange = int((maximum-minimum+1)*divider)
	x = np.zeros(int((maximum-minimum+1)*divider))
	y = np.zeros(int((maximum-minimum+1)*divider))
	rangeStart = minimum-interval;
	rangeEnd = minimum;
	for i in range(0, (valuesrange)):
		temp = inputframe["Distance moved"][(inputframe["Distance moved"] > rangeStart) & (inputframe["Distance moved"] < rangeEnd)]
		if (len(temp) == 0):
			y[i] = 0
			x[i] = rangeEnd
		if (len(temp) > 0):
			number = int(len(temp))
			y[i] = number
			x[i] = rangeEnd
		rangeStart = rangeStart+interval;
		rangeEnd = rangeEnd+interval

	x = pd.DataFrame(x)
	y = pd.DataFrame(y)
	FrequencyDistribution = pd.concat([x, y], axis=1)
	FrequencyDistribution.columns = ["Distance", "Frequency"]	
	return FrequencyDistribution
	
def MovFrequency2(mouseInput):
	inputframe = mouseInput
	inputframe["Distance moved"] = np.log2(inputframe["Distance moved"])
	max = 12
	Movement = np.zeros(max)
	Frequency = np.zeros(max)
	rangeStart = 0
	rangeEnd = 1
	for i in range(0, max):
		temp = inputframe["Distance moved"][(inputframe["Distance moved"] > rangeStart) & (inputframe["Distance moved"] < rangeEnd)]
		if (len(temp) == 0):
			Frequency[i] = 0
			Movement[i] = rangeEnd
		if (len(temp) > 0):
			number = int(len(temp))
			Frequency[i] = number
			Movement[i] = rangeEnd
		rangeStart = rangeStart+1
		rangeEnd = rangeEnd+1
	Movement = pd.DataFrame(Movement)
	Frequency = pd.DataFrame(Frequency)
	FrequencyDistribution = pd.concat([Movement, Frequency], axis=1)
	FrequencyDistribution.columns = ["Distance", "Frequency"]
	MaxFreq = FrequencyDistribution["Frequency"].max()
	Maximum = FrequencyDistribution["Distance"][FrequencyDistribution["Frequency"] == MaxFreq]
	LowerBound = Maximum-1
	UpperBound = Maximum+1
	LowerBound = int(2 ** (LowerBound))
	UpperBound = int(2 ** (UpperBound))
	IdealRange = np.array([LowerBound, UpperBound])
	del UpperBound, LowerBound
	return IdealRange
	
def Acceleration(mouseMov1, mouseMov2):
	mouse2 = mouseMov1
	mouse3 = mouseMov2
	IdealRange = MovFrequency2(mouse3)
	Lower = IdealRange[0]
	Upper = IdealRange[1]
	mouse2 = mouse2[(mouse2["Distance moved"] >= Lower) & (mouse2["Distance moved"] <= Upper)]
	mouse2 = mouse2.reset_index()
	del mouse2["index"]
	del Upper, Lower
	Hour = np.array(range(1, 90))
	Max = np.zeros(89)
	rangeStart = 0
	rangeEnd = 1
	for j in range(0, 89):
		temp = mouse2["Max Acceleration"][(mouse2["HoursAfterStart"] > rangeStart) & (mouse2["HoursAfterStart"] < rangeEnd)]
		if (len(temp) == 0):
			Max[j] = 0
		if (len(temp) > 0):
			Max[j] = temp.max()	
		rangeStart = rangeStart + 1
		rangeEnd = rangeEnd + 1
	Hour = pd.DataFrame(Hour)
	Max = pd.DataFrame(Max)
	mouse2 = pd.concat([Hour, Max], axis=1)
	mouse2.columns = ["Hour", "Acceleration"]
	return mouse2
	
def Figure(location, AnimalID, Treatment):
	"""Load the four graphs into Python"""
	image1 = cv.imread(location + "Entry Choice/" + Treatment + "/" +  AnimalID + "EntryChoice.jpg")
	#corrector = np.full((120, image1.shape[1], 3), 255)
	#image1 = np.concatenate((corrector, image1), axis=0)
	image2 = cv.imread(location + "Indexes/Cumulative/" + Treatment + "/" + AnimalID + "CumulativeIndex.jpg")
	#image2 = np.concatenate((corrector, image2), axis=0)
	image3 = cv.imread(location + "Movement/Independent/" + Treatment + "/" + AnimalID + "IndependentMovement.jpg")
	#image3 = np.concatenate((corrector, image3), axis=0)
	image4 = cv.imread(location + "Feeding/Independent/" + Treatment + "/" + AnimalID + "IndependentFeeding.jpg")
	#image4 = np.concatenate((corrector, image4), axis=0)
	image5 = cv.imread(location + "Segmentation/" + Treatment + "/" + AnimalID + "MovementSegmentDistribution.jpg")
	image6 = cv.imread(location + "Acceleration/" + Treatment + "/" + AnimalID + "Acc.jpg")
	"""Combine the Entry Choice and Index graphs"""
	image7 = np.concatenate((image1, image2, image6), axis=1)
	#corrector2 = np.full((image7.shape[0], 560, 3), 255)
	#image7 = np.concatenate((image7, corrector2), axis=1)
	"""Combine the Distance moved and Feeding graphs """
	image8 = np.concatenate((image3, image4, image5), axis=1)
	"""Cobine the two resultant figures into one figure"""
	image9 = np.concatenate((image7, image8), axis=0)
	"""Save the new figure"""
	almost = location + "Figures/"
	if (os.path.isdir(almost) == False):
		try:
			os.mkdir(almost)
		except OSError:
			print("Unable to create directory")
	finaldirectory = location + "Figures/" + Treatment + "/"
	if (os.path.isdir(finaldirectory) == True):
		cv.imwrite(finaldirectory + AnimalID + "figure.png", image9)
	if (os.path.isdir(finaldirectory) == False):
		try:
			os.mkdir(finaldirectory)
		except OSError:
			print("Unable to create directory")
		else:
			cv.imwrite(finaldirectory + AnimalID + "figure.png", image9)
	del image1, image2, image3, image4, image5, image6, image7, AnimalID
	
		
	
def MouseImport(mouselocation):	
	#write a function to find out the AnimalID and treatment from the text file
	start = time.time()
	HeaderValue = FindHeader(mouselocation)
	AnimalID = FindAnimalID(mouselocation, HeaderValue)
	treatment = FindTreatment(mouselocation, HeaderValue)
	Treatment = FindTreatment(mouselocation, HeaderValue)
	investigator = FindInvestigator(mouselocation, HeaderValue)
	Strain = FindStrain(mouselocation, HeaderValue)
	DOB = FindDOB(mouselocation, HeaderValue)
	RD = FindRD(mouselocation, HeaderValue)
	AGE = CalculateAge(DOB, RD)
	CC = FindCageCard(mouselocation, HeaderValue)
	Gender = FindGender(mouselocation, HeaderValue)
	PRW = FindPreWeight(mouselocation, HeaderValue)
	POW = FindPostWeight(mouselocation, HeaderValue)
	WC = CalculateWeightChange(PRW, POW)
	Ph = FindPhenNumber(mouselocation, HeaderValue)
	
	outputdirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
	directory0 = outputdirectory + investigator + "/"
	Hour = np.array(range(1, 90))
	Hour = pd.DataFrame(Hour)
	start2 = time.time()
	mouse = pd.read_csv(mouselocation, sep=";", header=HeaderValue, na_values=["-", "s", "s?", "cm", "cm?", "cm/s", "cm/s?"])
	mouse = mouse.drop(mouse.index[[0]])
	mouse = mouse.reset_index()
	del mouse["index"]
	print(AnimalID + " loaded in " + str(time.time()-start2) + " seconds!") 
	start3 = time.time()
	mouse2 = mouse[["Recording time", "X center", "Y center", "Distance moved", "Velocity", "In zone(InShelter / center-point)", "Include: Left Entrance D1", "Include: Mid Entrance D1", "Include: Right Entrance D1", "Include: Left Entrance D2", "Include: Mid Entrance D2", "Include: Right Entrance D2", "Include: Left Entrance Rev D1", "Include: Mid Entrance Rev D1", "Include: Right Entrance Rev D1", "Include: Left Entrance Rev D2", "Include: Mid Entrance Rev D2", "Include: Right Entrance Rev D2", "Hardware command", "Hardware continuous"]]
	mouse2.columns = ["Time", "X", "Y", "DistanceMoved", "Velocity", "InShelter", "LeftD1", "MiddleD1", "RightD1",  "LeftD2", "MiddleD2", "RightD2", "LeftD3", "MiddleD3", "RightD3", "LeftD4", "MiddleD4", "RightD4", "Command", "Continuous"]
	mouse2["Investigator"] = investigator
	mouse2["AnimalID"] = AnimalID
	mouse2["Treatment"] = Treatment
	mouse2["Strain"] = Strain
	mouse2["DOB"] = DOB
	mouse2["RunDate"] = RD
	mouse2["Age"] = AGE
	mouse2["CageCard"] = CC
	mouse2["Gender"] = Gender
	mouse2["PreWeight"] = PRW
	mouse2["PostWeight"] = POW
	mouse2["%WeightChange"] = WC
	mouse2["PhenotyperID"] = Ph
	mouse2.to_csv(directory0 + "Data/raw/" + treatment + "/mouse" + AnimalID + "raw.csv", index=False)
	mouse3 = mouse2[["Investigator", "Strain", "DOB", "RunDate", "Age", "CageCard", "Gender", "PreWeight", "PostWeight", "%WeightChange", "PhenotyperID"]][0:90]
	mouse4 = mouse2[["Investigator", "Strain", "DOB", "RunDate", "Age", "CageCard", "Gender", "PreWeight", "PostWeight", "%WeightChange", "PhenotyperID"]][0:5001]
	mouse5 = mouse2[["Investigator", "Strain", "DOB", "RunDate", "Age", "CageCard", "Gender", "PreWeight", "PostWeight", "%WeightChange", "PhenotyperID"]][0:6001]
	del mouse2
	print(AnimalID + " raw data exported in " + str(time.time()-start3) + " seconds") 
	mouseMov = mouse[["Recording time", "Distance moved"]]
	mouseMov.columns = ["Time", "Movement"]
	mouseMov = mouseMov[mouseMov["Movement"] >= 0.1]
	mouseMov = mouseMov.reset_index()
	del mouseMov["index"]
	movementrownumbers = int(len(mouseMov))
	mouseMov["Time"] = SecondsToHours(mouseMov["Time"], movementrownumbers)
	TotPathlength = np.array([mouseMov["Movement"][(mouseMov["Time"] < 1)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 1) & (mouseMov["Time"] < 2)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 2) & (mouseMov["Time"] < 3)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 3) & (mouseMov["Time"] < 4)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 4) & (mouseMov["Time"] < 5)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 5) & (mouseMov["Time"] < 6)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 6) & (mouseMov["Time"] < 7)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 7) & (mouseMov["Time"] < 8)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 8) & (mouseMov["Time"] < 9)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 9) & (mouseMov["Time"] < 10)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 10) & (mouseMov["Time"] < 11)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 11) & (mouseMov["Time"] < 12)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 12) & (mouseMov["Time"] < 13)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 13) & (mouseMov["Time"] < 14)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 14) & (mouseMov["Time"] < 15)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 15) & (mouseMov["Time"] < 16)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 16) & (mouseMov["Time"] < 17)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 17) & (mouseMov["Time"] < 18)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 18) & (mouseMov["Time"] < 19)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 19) & (mouseMov["Time"] < 20)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 20) & (mouseMov["Time"] < 21)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 21) & (mouseMov["Time"] < 22)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 22) & (mouseMov["Time"] < 23)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 23) & (mouseMov["Time"] < 24)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 24) & (mouseMov["Time"] < 25)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 25) & (mouseMov["Time"] < 26)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 26) & (mouseMov["Time"] < 27)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 27) & (mouseMov["Time"] < 28)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 28) & (mouseMov["Time"] < 29)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 29) & (mouseMov["Time"] < 30)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 30) & (mouseMov["Time"] < 31)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 31) & (mouseMov["Time"] < 32)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 32) & (mouseMov["Time"] < 33)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 33) & (mouseMov["Time"] < 34)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 34) & (mouseMov["Time"] < 35)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 35) & (mouseMov["Time"] < 36)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 36) & (mouseMov["Time"] < 37)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 37) & (mouseMov["Time"] < 38)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 38) & (mouseMov["Time"] < 39)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 39) & (mouseMov["Time"] < 40)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 40) & (mouseMov["Time"] < 41)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 41) & (mouseMov["Time"] < 42)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 42) & (mouseMov["Time"] < 43)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 43) & (mouseMov["Time"] < 44)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 44) & (mouseMov["Time"] < 45)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 45) & (mouseMov["Time"] < 46)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 46) & (mouseMov["Time"] < 47)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 47) & (mouseMov["Time"] < 48)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 48) & (mouseMov["Time"] < 49)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 49) & (mouseMov["Time"] < 50)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 50) & (mouseMov["Time"] < 51)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 51) & (mouseMov["Time"] < 52)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 52) & (mouseMov["Time"] < 53)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 53) & (mouseMov["Time"] < 54)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 54) & (mouseMov["Time"] < 55)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 55) & (mouseMov["Time"] < 56)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 56) & (mouseMov["Time"] < 57)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 57) & (mouseMov["Time"] < 58)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 58) & (mouseMov["Time"] < 59)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 59) & (mouseMov["Time"] < 60)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 60) & (mouseMov["Time"] < 61)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 61) & (mouseMov["Time"] < 62)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 62) & (mouseMov["Time"] < 63)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 63) & (mouseMov["Time"] < 64)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 64) & (mouseMov["Time"] < 65)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 65) & (mouseMov["Time"] < 66)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 66) & (mouseMov["Time"] < 67)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 67) & (mouseMov["Time"] < 68)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 68) & (mouseMov["Time"] < 69)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 69) & (mouseMov["Time"] < 70)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 70) & (mouseMov["Time"] < 71)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 71) & (mouseMov["Time"] < 72)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 72) & (mouseMov["Time"] < 73)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 73) & (mouseMov["Time"] < 74)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 74) & (mouseMov["Time"] < 75)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 75) & (mouseMov["Time"] < 76)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 76) & (mouseMov["Time"] < 77)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 77) & (mouseMov["Time"] < 78)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 78) & (mouseMov["Time"] < 79)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 79) & (mouseMov["Time"] < 80)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 80) & (mouseMov["Time"] < 81)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 81) & (mouseMov["Time"] < 82)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 82) & (mouseMov["Time"] < 83)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 83) & (mouseMov["Time"] < 84)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 84) & (mouseMov["Time"] < 85)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 85) & (mouseMov["Time"] < 86)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 86) & (mouseMov["Time"] < 87)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 87) & (mouseMov["Time"] < 88)].sum(), mouseMov["Movement"][(mouseMov["Time"] > 88) & (mouseMov["Time"] < 89)].sum()])
	CumulativeMovement = np.array([mouseMov["Movement"][(mouseMov["Time"] < 1)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 2)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 3)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 4)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 5)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 6)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 7)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 8)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 9)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 10)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 11)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 12)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 13)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 14)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 15)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 16)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 17)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 18)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 19)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 20)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 21)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 22)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 23)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 24)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 25)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 26)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 27)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 28)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 29)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 30)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 31)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 32)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 33)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 34)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 35)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 36)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 37)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 38)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 39)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 40)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 41)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 42)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 43)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 44)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 45)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 46)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 47)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 48)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 49)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 50)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 51)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 52)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 53)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 54)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 55)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 56)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 57)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 58)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 59)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 60)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 61)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 62)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 63)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 64)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 65)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 66)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 67)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 68)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 69)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 70)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 71)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 72)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 73)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 74)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 75)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 76)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 77)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 78)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 79)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 80)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 81)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 82)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 83)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 84)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 85)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 86)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 87)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 88)].sum(), mouseMov["Movement"][(mouseMov["Time"] < 89)].sum()])
	TotPathlength = pd.DataFrame(TotPathlength)
	CumulativeMovement = pd.DataFrame(CumulativeMovement)
	Name = np.full((89), AnimalID)
	Name = pd.DataFrame(Name)
	Group = np.full((89), Treatment)
	Group = pd.DataFrame(Group)
	mouseMov = pd.concat([Name, Group, Hour, TotPathlength, CumulativeMovement], axis=1)
	mouseMov.columns = ["AnimalNumber", "Treatment", "Hour", "TotPathlength", "CumulativeMovement"]
	plt.figsize=(18, 6)
	plt.plot(mouseMov["Hour"], mouseMov["TotPathlength"], "r-")
	plt.title(AnimalID + " " + treatment + " Total Distance moved by Hour(Independent)")
	plt.xlabel("Hour", fontsize=18)
	plt.ylabel("Distance moved", fontsize=18)
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000, 22500, 25000])
	plt.savefig(directory0 + "Graphs/Individual mice/Movement/Independent/" + treatment + "/" + AnimalID + "IndependentMovement.jpg", oreintation="landscape")
	plt.clf()
	plt.figsize=(18, 6)
	plt.plot(mouseMov["Hour"], mouseMov["CumulativeMovement"], "r-")
	plt.title(AnimalID + " " + treatment + " Total Distance moved by Hour(Cumulative)")
	plt.xlabel("Hour", fontsize=18)
	plt.ylabel("Distance moved", fontsize=18)
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000])
	plt.savefig(directory0 + "Graphs/Individual mice/Movement/Cumulative/" + treatment + "/" + AnimalID + "CumulativeMovement.jpg", oreintation="landscape")
	plt.clf()
	mouseMov = pd.concat([mouseMov, mouse3], axis=1)
	mouseMov.to_csv(directory0 + "Data/Distance moved/" + treatment + "/" + AnimalID + "Movement.csv", index=False)
	del mouseMov
	del TotPathlength, CumulativeMovement
	del movementrownumbers
 
	mouseFeeding = mouse[["Recording time", "Hardware continuous"]]
	mouseFeeding.columns = ["Time", "Pellet Drops"]
	mouseFeeding = mouseFeeding[mouseFeeding["Pellet Drops"] == 1]
	mouseFeeding = mouseFeeding.reset_index()
	del mouseFeeding["index"]
	feedingrownumbers = int(len(mouseFeeding))
	mouseFeeding["Time"] = SecondsToHours(mouseFeeding["Time"], feedingrownumbers)
	PelletDrops = np.array([mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 1)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 1) & (mouseFeeding["Time"] < 2)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 2) & (mouseFeeding["Time"] < 3)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 3) & (mouseFeeding["Time"] < 4)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 4) & (mouseFeeding["Time"] < 5)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 5) & (mouseFeeding["Time"] < 6)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 6) & (mouseFeeding["Time"] < 7)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 7) & (mouseFeeding["Time"] < 8)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 8) & (mouseFeeding["Time"] < 9)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 9) & (mouseFeeding["Time"] < 10)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 10) & (mouseFeeding["Time"] < 11)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 11) & (mouseFeeding["Time"] < 12)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 12) & (mouseFeeding["Time"] < 13)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 13) & (mouseFeeding["Time"] < 14)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 14) & (mouseFeeding["Time"] < 15)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 15) & (mouseFeeding["Time"] < 16)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 16) & (mouseFeeding["Time"] < 17)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 17) & (mouseFeeding["Time"] < 18)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 18) & (mouseFeeding["Time"] < 19)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 19) & (mouseFeeding["Time"] < 20)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 20) & (mouseFeeding["Time"] < 21)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 21) & (mouseFeeding["Time"] < 22)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 22) & (mouseFeeding["Time"] < 23)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 23) & (mouseFeeding["Time"] < 24)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 24) & (mouseFeeding["Time"] < 25)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 25) & (mouseFeeding["Time"] < 26)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 26) & (mouseFeeding["Time"] < 27)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 27) & (mouseFeeding["Time"] < 28)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 28) & (mouseFeeding["Time"] < 29)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 29) & (mouseFeeding["Time"] < 30)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 30) & (mouseFeeding["Time"] < 31)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 31) & (mouseFeeding["Time"] < 32)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 32) & (mouseFeeding["Time"] < 33)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 33) & (mouseFeeding["Time"] < 34)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 34) & (mouseFeeding["Time"] < 35)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 35) & (mouseFeeding["Time"] < 36)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 36) & (mouseFeeding["Time"] < 37)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 37) & (mouseFeeding["Time"] < 38)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 38) & (mouseFeeding["Time"] < 39)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 39) & (mouseFeeding["Time"] < 40)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 40) & (mouseFeeding["Time"] < 41)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 41) & (mouseFeeding["Time"] < 42)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 42) & (mouseFeeding["Time"] < 43)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 43) & (mouseFeeding["Time"] < 44)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 44) & (mouseFeeding["Time"] < 45)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 45) & (mouseFeeding["Time"] < 46)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 46) & (mouseFeeding["Time"] < 47)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 47) & (mouseFeeding["Time"] < 48)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 48) & (mouseFeeding["Time"] < 49)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 49) & (mouseFeeding["Time"] < 50)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 50) & (mouseFeeding["Time"] < 51)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 51) & (mouseFeeding["Time"] < 52)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 52) & (mouseFeeding["Time"] < 53)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 53) & (mouseFeeding["Time"] < 54)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 54) & (mouseFeeding["Time"] < 55)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 55) & (mouseFeeding["Time"] < 56)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 56) & (mouseFeeding["Time"] < 57)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 57) & (mouseFeeding["Time"] < 58)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 58) & (mouseFeeding["Time"] < 59)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 59) & (mouseFeeding["Time"] < 60)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 60) & (mouseFeeding["Time"] < 61)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 61) & (mouseFeeding["Time"] < 62)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 62) & (mouseFeeding["Time"] < 63)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 63) & (mouseFeeding["Time"] < 64)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 64) & (mouseFeeding["Time"] < 65)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 65) & (mouseFeeding["Time"] < 66)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 66) & (mouseFeeding["Time"] < 67)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 67) & (mouseFeeding["Time"] < 68)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 68) & (mouseFeeding["Time"] < 69)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 69) & (mouseFeeding["Time"] < 70)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 70) & (mouseFeeding["Time"] < 71)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 71) & (mouseFeeding["Time"] < 72)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 72) & (mouseFeeding["Time"] < 73)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 73) & (mouseFeeding["Time"] < 74)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 74) & (mouseFeeding["Time"] < 75)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 75) & (mouseFeeding["Time"] < 76)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 76) & (mouseFeeding["Time"] < 77)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 77) & (mouseFeeding["Time"] < 78)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 78) & (mouseFeeding["Time"] < 79)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 79) & (mouseFeeding["Time"] < 80)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 80) & (mouseFeeding["Time"] < 81)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 81) & (mouseFeeding["Time"] < 82)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 82) & (mouseFeeding["Time"] < 83)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 83) & (mouseFeeding["Time"] < 84)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 84) & (mouseFeeding["Time"] < 85)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 85) & (mouseFeeding["Time"] < 86)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 86) & (mouseFeeding["Time"] < 87)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 87) & (mouseFeeding["Time"] < 88)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] > 88) & (mouseFeeding["Time"] < 89)].sum()])
	PelletDropsv2 = np.array([mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 1)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 2)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 3)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 4)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 5)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 6)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 7)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 8)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 9)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 10)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 11)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 12)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 13)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 14)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 15)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 16)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 17)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 18)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 19)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 20)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 21)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 22)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 23)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 24)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 25)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 26)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 27)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 28)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 29)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 30)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 31)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 32)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 33)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 34)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 35)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 36)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 37)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 38)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 39)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 40)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 41)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 42)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 43)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 44)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 45)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 46)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 47)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 48)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 49)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 50)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 51)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 52)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 53)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 54)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 55)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 56)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 57)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 58)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 59)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 60)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 61)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 62)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 63)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 64)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 65)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 66)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 67)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 68)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 69)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 70)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 71)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 72)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 73)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 74)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 75)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 76)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 77)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 78)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 79)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 80)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 81)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 82)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 83)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 84)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 85)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 86)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 87)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 88)].sum(), mouseFeeding["Pellet Drops"][(mouseFeeding["Time"] < 89)].sum()])
	PelletDrops = pd.DataFrame(PelletDrops)
	PelletDropsv2 = pd.DataFrame(PelletDropsv2)
	mouseFeeding = pd.concat([Name, Group, Hour, PelletDrops, PelletDropsv2], axis=1)
	mouseFeeding.columns = ["AnimalNumber", "Treatment", "Hour", "TotFeeding", "Rewards"]
	plt.figsize=(18, 6)
	plt.plot(mouseFeeding["Hour"], mouseFeeding["TotFeeding"], "r-")
	plt.title(AnimalID + " " + treatment + " Feeding by Hour(Independent)")
	plt.xlabel("Hour", fontsize=18)
	plt.ylabel("Pellet Drops", fontsize=18)
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
	plt.savefig(directory0 + "Graphs/Individual mice/Feeding/Independent/" + treatment + "/" + AnimalID + "IndependentFeeding.jpg", oreintation="landscape")
	plt.clf()
	plt.figsize=(18, 6)
	plt.plot(mouseFeeding["Hour"], mouseFeeding["Rewards"], "r-")
	plt.title(AnimalID + " " + treatment + " Feeding by Hour(Cumulative)")
	plt.xlabel("Hour", fontsize=18)
	plt.ylabel("Pellet drops", fontsize=18)
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
	plt.savefig(directory0 + "Graphs/Individual mice/Feeding/Cumulative/" + treatment + "/" + AnimalID + "CumulativeFeeding.jpg", oreintation="landscape")
	plt.clf()
	mouseFeeding = pd.concat([mouseFeeding, mouse3], axis=1)
	mouseFeeding.to_csv(directory0 + "Data/Feeding/" + treatment + "/" + AnimalID + "feedingresults.csv", index=False)
	del mouseFeeding
	del PelletDrops, PelletDropsv2
	del Name, Group
	del feedingrownumbers
 
 
	numberofentries = mouse["Include: Left Entrance D1"].sum() + mouse["Include: Mid Entrance D1"].sum() + mouse["Include: Right Entrance D1"].sum() + mouse["Include: Left Entrance D2"].sum() + mouse["Include: Mid Entrance D2"].sum() + mouse["Include: Right Entrance D2"].sum() + mouse["Include: Left Entrance Rev D1"].sum() + mouse["Include: Mid Entrance Rev D1"].sum() + mouse["Include: Right Entrance Rev D1"].sum() + mouse["Include: Left Entrance Rev D2"].sum() + mouse["Include: Mid Entrance Rev D2"].sum() + mouse["Include: Right Entrance Rev D2"].sum()
	numberofentries = int(numberofentries)
	mouseentries = mouse[["Recording time", "Include: Left Entrance D1", "Include: Mid Entrance D1", "Include: Right Entrance D1", "Include: Left Entrance D2", "Include: Mid Entrance D2", "Include: Right Entrance D2", "Include: Left Entrance Rev D1", "Include: Mid Entrance Rev D1", "Include: Right Entrance Rev D1", "Include: Left Entrance Rev D2", "Include: Mid Entrance Rev D2", "Include: Right Entrance Rev D2"]]
	mouseentries = mouseentries[(mouseentries["Include: Left Entrance D1"] == 1) | (mouseentries["Include: Mid Entrance D1"] == 1) | (mouseentries["Include: Right Entrance D1"] == 1) | (mouseentries["Include: Left Entrance D2"] == 1) | (mouseentries["Include: Mid Entrance D2"] == 1) | (mouseentries["Include: Right Entrance D2"] == 1) | (mouseentries["Include: Left Entrance Rev D1"] == 1) | (mouseentries["Include: Mid Entrance Rev D1"] == 1) | (mouseentries["Include: Right Entrance Rev D1"] == 1) | (mouseentries["Include: Left Entrance Rev D2"] == 1) | (mouseentries["Include: Mid Entrance Rev D2"] == 1) | (mouseentries["Include: Right Entrance Rev D2"] == 1)]
 
	IDnumberofentries = mouse["Include: Left Entrance D1"].sum() + mouse["Include: Mid Entrance D1"].sum() + mouse["Include: Right Entrance D1"].sum() + mouse["Include: Left Entrance D2"].sum() + mouse["Include: Mid Entrance D2"].sum() + mouse["Include: Right Entrance D2"].sum()
	IDnumberofentries = int(IDnumberofentries)
	Revnumberofentries = mouse["Include: Left Entrance Rev D1"].sum() + mouse["Include: Mid Entrance Rev D1"].sum() + mouse["Include: Right Entrance Rev D1"].sum() + mouse["Include: Left Entrance Rev D2"].sum() + mouse["Include: Mid Entrance Rev D2"].sum() + mouse["Include: Right Entrance Rev D2"].sum()
	Revnumberofentries = int(Revnumberofentries)
 
	FullEntryNumber = np.array(range(1, 6001))
	FullEntryNumber = pd.DataFrame(FullEntryNumber)
 
 
	mouseentriesD1 = mouseentries[["Recording time", "Include: Left Entrance D1", "Include: Mid Entrance D1", "Include: Right Entrance D1"]]
	mouseentriesD1 = mouseentriesD1[(mouseentriesD1["Recording time"] < 86400)]
	mouseentriesD1.columns = ["Time", "Left", "Middle", "Right"]
	mouseentriesD2 = mouseentries[["Recording time", "Include: Left Entrance D2", "Include: Mid Entrance D2", "Include: Right Entrance D2"]]
	mouseentriesD2 = mouseentriesD2[(mouseentriesD2["Recording time"] > 86400) & (mouseentriesD2["Recording time"] < 172800)]
	mouseentriesD2.columns = ["Time", "Left", "Middle", "Right"]
	framestomergeInitial = [mouseentriesD1, mouseentriesD2]
	mouseInitial = pd.concat(framestomergeInitial)
	mouseentriesD3 = mouseentries[["Recording time", "Include: Left Entrance Rev D1", "Include: Mid Entrance Rev D1", "Include: Right Entrance Rev D1"]]
	mouseentriesD3 = mouseentriesD3[(mouseentriesD3["Recording time"] > 172800) & (mouseentriesD3["Recording time"] < 259200)]
	mouseentriesD3.columns = ["Time", "Left", "Middle", "Right"]
	mouseentriesD4 = mouseentries[["Recording time", "Include: Left Entrance Rev D2", "Include: Mid Entrance Rev D2", "Include: Right Entrance Rev D2"]]
	mouseentriesD4 = mouseentriesD4[(mouseentriesD4["Recording time"] > 259200) & (mouseentriesD4["Recording time"] < 345600)]
	mouseentriesD4.columns = ["Time", "Left", "Middle", "Right"]
	framestomergeReversal = [mouseentriesD3, mouseentriesD4]
	mouseReversal = pd.concat(framestomergeReversal)
	del mouseentries, mouseentriesD1, mouseentriesD2, mouseentriesD3, mouseentriesD4
	del framestomergeInitial, framestomergeReversal
 
 
	mouseIndex = pd.concat([mouseInitial, mouseReversal])
	mouseIndex = mouseIndex.reset_index()
	del mouseIndex["index"]
	mouseIndex["Time"] = SecondsToHours(mouseIndex["Time"], numberofentries)
	Left = np.array([mouseIndex["Left"][(mouseIndex["Time"] < 1)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 1) & (mouseIndex["Time"] < 2)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 2) & (mouseIndex["Time"] < 3)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 3) & (mouseIndex["Time"] < 4)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 4) & (mouseIndex["Time"] < 5)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 5) & (mouseIndex["Time"] < 6)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 6) & (mouseIndex["Time"] < 7)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 7) & (mouseIndex["Time"] < 8)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 8) & (mouseIndex["Time"] < 9)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 9) & (mouseIndex["Time"] < 10)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 10) & (mouseIndex["Time"] < 11)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 11) & (mouseIndex["Time"] < 12)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 12) & (mouseIndex["Time"] < 13)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 13) & (mouseIndex["Time"] < 14)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 14) & (mouseIndex["Time"] < 15)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 15) & (mouseIndex["Time"] < 16)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 16) & (mouseIndex["Time"] < 17)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 17) & (mouseIndex["Time"] < 18)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 18) & (mouseIndex["Time"] < 19)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 19) & (mouseIndex["Time"] < 20)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 20) & (mouseIndex["Time"] < 21)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 21) & (mouseIndex["Time"] < 22)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 22) & (mouseIndex["Time"] < 23)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 23) & (mouseIndex["Time"] < 24)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 24) & (mouseIndex["Time"] < 25)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 25) & (mouseIndex["Time"] < 26)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 26) & (mouseIndex["Time"] < 27)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 27) & (mouseIndex["Time"] < 28)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 28) & (mouseIndex["Time"] < 29)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 29) & (mouseIndex["Time"] < 30)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 30) & (mouseIndex["Time"] < 31)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 31) & (mouseIndex["Time"] < 32)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 32) & (mouseIndex["Time"] < 33)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 33) & (mouseIndex["Time"] < 34)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 34) & (mouseIndex["Time"] < 35)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 35) & (mouseIndex["Time"] < 36)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 36) & (mouseIndex["Time"] < 37)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 37) & (mouseIndex["Time"] < 38)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 38) & (mouseIndex["Time"] < 39)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 39) & (mouseIndex["Time"] < 40)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 40) & (mouseIndex["Time"] < 41)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 41) & (mouseIndex["Time"] < 42)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 42) & (mouseIndex["Time"] < 43)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 43) & (mouseIndex["Time"] < 44)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 44) & (mouseIndex["Time"] < 45)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 45) & (mouseIndex["Time"] < 46)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 46) & (mouseIndex["Time"] < 47)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 47) & (mouseIndex["Time"] < 48)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 49)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 49) & (mouseIndex["Time"] < 50)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 50) & (mouseIndex["Time"] < 51)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 51) & (mouseIndex["Time"] < 52)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 52) & (mouseIndex["Time"] < 53)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 53) & (mouseIndex["Time"] < 54)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 54) & (mouseIndex["Time"] < 55)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 55) & (mouseIndex["Time"] < 56)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 56) & (mouseIndex["Time"] < 57)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 57) & (mouseIndex["Time"] < 58)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 58) & (mouseIndex["Time"] < 59)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 59) & (mouseIndex["Time"] < 60)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 60) & (mouseIndex["Time"] < 61)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 61) & (mouseIndex["Time"] < 62)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 62) & (mouseIndex["Time"] < 63)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 63) & (mouseIndex["Time"] < 64)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 64) & (mouseIndex["Time"] < 65)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 65) & (mouseIndex["Time"] < 66)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 66) & (mouseIndex["Time"] < 67)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 67) & (mouseIndex["Time"] < 68)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 68) & (mouseIndex["Time"] < 69)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 69) & (mouseIndex["Time"] < 70)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 70) & (mouseIndex["Time"] < 71)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 71) & (mouseIndex["Time"] < 72)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 72) & (mouseIndex["Time"] < 73)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 73) & (mouseIndex["Time"] < 74)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 74) & (mouseIndex["Time"] < 75)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 75) & (mouseIndex["Time"] < 76)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 76) & (mouseIndex["Time"] < 77)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 77) & (mouseIndex["Time"] < 78)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 78) & (mouseIndex["Time"] < 79)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 79) & (mouseIndex["Time"] < 80)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 80) & (mouseIndex["Time"] < 81)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 81) & (mouseIndex["Time"] < 82)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 82) & (mouseIndex["Time"] < 83)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 83) & (mouseIndex["Time"] < 84)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 84) & (mouseIndex["Time"] < 85)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 85) & (mouseIndex["Time"] < 86)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 86) & (mouseIndex["Time"] < 87)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 87) & (mouseIndex["Time"] < 88)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 88) & (mouseIndex["Time"] < 89)].sum()])
	Middle = np.array([mouseIndex["Middle"][(mouseIndex["Time"] < 1)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 1) & (mouseIndex["Time"] < 2)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 2) & (mouseIndex["Time"] < 3)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 3) & (mouseIndex["Time"] < 4)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 4) & (mouseIndex["Time"] < 5)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 5) & (mouseIndex["Time"] < 6)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 6) & (mouseIndex["Time"] < 7)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 7) & (mouseIndex["Time"] < 8)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 8) & (mouseIndex["Time"] < 9)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 9) & (mouseIndex["Time"] < 10)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 10) & (mouseIndex["Time"] < 11)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 11) & (mouseIndex["Time"] < 12)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 12) & (mouseIndex["Time"] < 13)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 13) & (mouseIndex["Time"] < 14)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 14) & (mouseIndex["Time"] < 15)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 15) & (mouseIndex["Time"] < 16)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 16) & (mouseIndex["Time"] < 17)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 17) & (mouseIndex["Time"] < 18)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 18) & (mouseIndex["Time"] < 19)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 19) & (mouseIndex["Time"] < 20)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 20) & (mouseIndex["Time"] < 21)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 21) & (mouseIndex["Time"] < 22)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 22) & (mouseIndex["Time"] < 23)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 23) & (mouseIndex["Time"] < 24)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 24) & (mouseIndex["Time"] < 25)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 25) & (mouseIndex["Time"] < 26)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 26) & (mouseIndex["Time"] < 27)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 27) & (mouseIndex["Time"] < 28)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 28) & (mouseIndex["Time"] < 29)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 29) & (mouseIndex["Time"] < 30)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 30) & (mouseIndex["Time"] < 31)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 31) & (mouseIndex["Time"] < 32)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 32) & (mouseIndex["Time"] < 33)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 33) & (mouseIndex["Time"] < 34)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 34) & (mouseIndex["Time"] < 35)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 35) & (mouseIndex["Time"] < 36)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 36) & (mouseIndex["Time"] < 37)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 37) & (mouseIndex["Time"] < 38)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 38) & (mouseIndex["Time"] < 39)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 39) & (mouseIndex["Time"] < 40)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 40) & (mouseIndex["Time"] < 41)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 41) & (mouseIndex["Time"] < 42)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 42) & (mouseIndex["Time"] < 43)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 43) & (mouseIndex["Time"] < 44)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 44) & (mouseIndex["Time"] < 45)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 45) & (mouseIndex["Time"] < 46)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 46) & (mouseIndex["Time"] < 47)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 47) & (mouseIndex["Time"] < 48)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 49)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 49) & (mouseIndex["Time"] < 50)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 50) & (mouseIndex["Time"] < 51)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 51) & (mouseIndex["Time"] < 52)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 52) & (mouseIndex["Time"] < 53)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 53) & (mouseIndex["Time"] < 54)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 54) & (mouseIndex["Time"] < 55)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 55) & (mouseIndex["Time"] < 56)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 56) & (mouseIndex["Time"] < 57)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 57) & (mouseIndex["Time"] < 58)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 58) & (mouseIndex["Time"] < 59)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 59) & (mouseIndex["Time"] < 60)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 60) & (mouseIndex["Time"] < 61)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 61) & (mouseIndex["Time"] < 62)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 62) & (mouseIndex["Time"] < 63)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 63) & (mouseIndex["Time"] < 64)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 64) & (mouseIndex["Time"] < 65)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 65) & (mouseIndex["Time"] < 66)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 66) & (mouseIndex["Time"] < 67)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 67) & (mouseIndex["Time"] < 68)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 68) & (mouseIndex["Time"] < 69)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 69) & (mouseIndex["Time"] < 70)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 70) & (mouseIndex["Time"] < 71)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 71) & (mouseIndex["Time"] < 72)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 72) & (mouseIndex["Time"] < 73)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 73) & (mouseIndex["Time"] < 74)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 74) & (mouseIndex["Time"] < 75)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 75) & (mouseIndex["Time"] < 76)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 76) & (mouseIndex["Time"] < 77)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 77) & (mouseIndex["Time"] < 78)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 78) & (mouseIndex["Time"] < 79)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 79) & (mouseIndex["Time"] < 80)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 80) & (mouseIndex["Time"] < 81)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 81) & (mouseIndex["Time"] < 82)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 82) & (mouseIndex["Time"] < 83)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 83) & (mouseIndex["Time"] < 84)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 84) & (mouseIndex["Time"] < 85)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 85) & (mouseIndex["Time"] < 86)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 86) & (mouseIndex["Time"] < 87)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 87) & (mouseIndex["Time"] < 88)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 88) & (mouseIndex["Time"] < 89)].sum()])
	Right = np.array([mouseIndex["Right"][(mouseIndex["Time"] < 1)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 1) & (mouseIndex["Time"] < 2)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 2) & (mouseIndex["Time"] < 3)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 3) & (mouseIndex["Time"] < 4)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 4) & (mouseIndex["Time"] < 5)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 5) & (mouseIndex["Time"] < 6)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 6) & (mouseIndex["Time"] < 7)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 7) & (mouseIndex["Time"] < 8)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 8) & (mouseIndex["Time"] < 9)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 9) & (mouseIndex["Time"] < 10)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 10) & (mouseIndex["Time"] < 11)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 11) & (mouseIndex["Time"] < 12)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 12) & (mouseIndex["Time"] < 13)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 13) & (mouseIndex["Time"] < 14)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 14) & (mouseIndex["Time"] < 15)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 15) & (mouseIndex["Time"] < 16)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 16) & (mouseIndex["Time"] < 17)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 17) & (mouseIndex["Time"] < 18)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 18) & (mouseIndex["Time"] < 19)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 19) & (mouseIndex["Time"] < 20)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 20) & (mouseIndex["Time"] < 21)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 21) & (mouseIndex["Time"] < 22)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 22) & (mouseIndex["Time"] < 23)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 23) & (mouseIndex["Time"] < 24)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 24) & (mouseIndex["Time"] < 25)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 25) & (mouseIndex["Time"] < 26)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 26) & (mouseIndex["Time"] < 27)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 27) & (mouseIndex["Time"] < 28)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 28) & (mouseIndex["Time"] < 29)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 29) & (mouseIndex["Time"] < 30)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 30) & (mouseIndex["Time"] < 31)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 31) & (mouseIndex["Time"] < 32)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 32) & (mouseIndex["Time"] < 33)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 33) & (mouseIndex["Time"] < 34)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 34) & (mouseIndex["Time"] < 35)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 35) & (mouseIndex["Time"] < 36)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 36) & (mouseIndex["Time"] < 37)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 37) & (mouseIndex["Time"] < 38)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 38) & (mouseIndex["Time"] < 39)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 39) & (mouseIndex["Time"] < 40)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 40) & (mouseIndex["Time"] < 41)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 41) & (mouseIndex["Time"] < 42)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 42) & (mouseIndex["Time"] < 43)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 43) & (mouseIndex["Time"] < 44)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 44) & (mouseIndex["Time"] < 45)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 45) & (mouseIndex["Time"] < 46)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 46) & (mouseIndex["Time"] < 47)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 47) & (mouseIndex["Time"] < 48)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 49)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 49) & (mouseIndex["Time"] < 50)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 50) & (mouseIndex["Time"] < 51)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 51) & (mouseIndex["Time"] < 52)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 52) & (mouseIndex["Time"] < 53)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 53) & (mouseIndex["Time"] < 54)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 54) & (mouseIndex["Time"] < 55)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 55) & (mouseIndex["Time"] < 56)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 56) & (mouseIndex["Time"] < 57)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 57) & (mouseIndex["Time"] < 58)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 58) & (mouseIndex["Time"] < 59)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 59) & (mouseIndex["Time"] < 60)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 60) & (mouseIndex["Time"] < 61)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 61) & (mouseIndex["Time"] < 62)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 62) & (mouseIndex["Time"] < 63)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 63) & (mouseIndex["Time"] < 64)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 64) & (mouseIndex["Time"] < 65)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 65) & (mouseIndex["Time"] < 66)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 66) & (mouseIndex["Time"] < 67)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 67) & (mouseIndex["Time"] < 68)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 68) & (mouseIndex["Time"] < 69)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 69) & (mouseIndex["Time"] < 70)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 70) & (mouseIndex["Time"] < 71)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 71) & (mouseIndex["Time"] < 72)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 72) & (mouseIndex["Time"] < 73)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 73) & (mouseIndex["Time"] < 74)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 74) & (mouseIndex["Time"] < 75)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 75) & (mouseIndex["Time"] < 76)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 76) & (mouseIndex["Time"] < 77)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 77) & (mouseIndex["Time"] < 78)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 78) & (mouseIndex["Time"] < 79)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 79) & (mouseIndex["Time"] < 80)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 80) & (mouseIndex["Time"] < 81)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 81) & (mouseIndex["Time"] < 82)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 82) & (mouseIndex["Time"] < 83)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 83) & (mouseIndex["Time"] < 84)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 84) & (mouseIndex["Time"] < 85)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 85) & (mouseIndex["Time"] < 86)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 86) & (mouseIndex["Time"] < 87)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 87) & (mouseIndex["Time"] < 88)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 88) & (mouseIndex["Time"] < 89)].sum()])
	CumulativeLeft = np.array([mouseIndex["Left"][(mouseIndex["Time"] < 1)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 2)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 3)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 4)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 5)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 6)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 7)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 8)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 9)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 10)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 11)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 12)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 13)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 14)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 15)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 16)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 17)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 18)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 19)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 20)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 21)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 22)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 23)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 24)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 25)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 26)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 27)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 28)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 29)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 30)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 31)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 32)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 33)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 34)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 35)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 36)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 37)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 38)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 39)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 40)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 41)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 42)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 43)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 44)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 45)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 46)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 47)].sum(), mouseIndex["Left"][(mouseIndex["Time"] < 48)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 49)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 50)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 51)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 52)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 53)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 54)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 55)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 56)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 57)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 58)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 59)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 60)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 61)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 62)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 63)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 64)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 65)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 66)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 67)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 68)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 69)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 70)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 71)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 72)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 73)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 74)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 75)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 76)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 77)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 78)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 79)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 80)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 81)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 82)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 83)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 84)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 85)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 86)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 87)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 88)].sum(), mouseIndex["Left"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 89)].sum()])
	CumulativeMiddle = np.array([mouseIndex["Middle"][(mouseIndex["Time"] < 1)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 2)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 3)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 4)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 5)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 6)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 7)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 8)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 9)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 10)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 11)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 12)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 13)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 14)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 15)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 16)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 17)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 18)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 19)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 20)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 21)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 22)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 23)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 24)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 25)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 26)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 27)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 28)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 29)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 30)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 31)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 32)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 33)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 34)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 35)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 36)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 37)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 38)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 39)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 40)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 41)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 42)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 43)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 44)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 45)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 46)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 47)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] < 48)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 49)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 50)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 51)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 52)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 53)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 54)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 55)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 56)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 57)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 58)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 59)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 60)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 61)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 62)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 63)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 64)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 65)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 66)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 67)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 68)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 69)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 70)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 71)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 72)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 73)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 74)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 75)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 76)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 77)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 78)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 79)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 80)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 81)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 82)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 83)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 84)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 85)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 86)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 87)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 88)].sum(), mouseIndex["Middle"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 89)].sum()])
	CumulativeRight = np.array([mouseIndex["Right"][(mouseIndex["Time"] < 1)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 2)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 3)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 4)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 5)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 6)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 7)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 8)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 9)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 10)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 11)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 12)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 13)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 14)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 15)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 16)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 17)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 18)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 19)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 20)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 21)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 22)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 23)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 24)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 25)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 26)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 27)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 28)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 29)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 30)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 31)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 32)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 33)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 34)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 35)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 36)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 37)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 38)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 39)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 40)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 41)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 42)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 43)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 44)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 45)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 46)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 47)].sum(), mouseIndex["Right"][(mouseIndex["Time"] < 48)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 49)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 50)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 51)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 52)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 53)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 54)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 55)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 56)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 57)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 58)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 59)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 60)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 61)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 62)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 63)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 64)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 65)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 66)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 67)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 68)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 69)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 70)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 71)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 72)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 73)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 74)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 75)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 76)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 77)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 78)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 79)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 80)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 81)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 82)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 83)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 84)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 85)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 86)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 87)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 88)].sum(), mouseIndex["Right"][(mouseIndex["Time"] > 48) & (mouseIndex["Time"] < 89)].sum()])
	LearningIndex = np.zeros(89)
	LearningIndex = IndexFunction(Left, Middle, Right)
	LearningIndex = pd.DataFrame(LearningIndex)
	CumulativeIndex = np.zeros(89)
	CumulativeIndex = IndexFunction(CumulativeLeft, CumulativeMiddle, CumulativeRight)
	CumulativeIndex = pd.DataFrame(CumulativeIndex)
	Left = pd.DataFrame(Left)
	Middle = pd.DataFrame(Middle)
	Right = pd.DataFrame(Right)
	mouseIndex = pd.concat([Hour, Left, Middle, Right], axis=1)
	mouseIndex.columns = ["Hour", "Left", "Middle", "Right"]
	del Left, Middle, Right
	Name = np.full((89), AnimalID)
	Name = pd.DataFrame(Name)
	Group = np.full((89), Treatment)
	Group = pd.DataFrame(Group)
	plt.figsize=(18, 6)
	plt.plot(mouseIndex["Hour"], mouseIndex["Left"], "r-")
	plt.plot(mouseIndex["Hour"], mouseIndex["Middle"], "b-")
	plt.plot(mouseIndex["Hour"], mouseIndex["Right"], "g-")
	plt.title(AnimalID + " " + treatment + " Entry Choice by Hour)")
	plt.xlabel("Hour", fontsize=18)
	plt.ylabel("# of entries", fontsize=18)
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 25, 50, 75, 100, 125, 150, 175, 200])
	plt.legend(["Left", "Middle", "Right"])
	plt.savefig(directory0 + "Graphs/Individual mice/Entry Choice/" + treatment + "/" + AnimalID + "EntryChoice.jpg", orientation="landscape")
	plt.clf()
	mouseIndex = pd.concat([Name, Group, mouseIndex, LearningIndex], axis=1)
	mouseIndex.columns = ["Name", "Group", "Hour", "Left", "Middle", "Right", "LearningIndex"]
	plt.figsize=(18, 6)
	plt.plot(mouseIndex["Hour"], mouseIndex["LearningIndex"], "r-")
	plt.title(AnimalID + " " + treatment + " (Correct entries - Incorrect entries) / Total entries)")
	plt.xlabel("Hour", fontsize=18)
	plt.ylabel("Learning Index", fontsize=18)
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([-1.0, -0.5, 0, 0.5, 1.0])
	plt.savefig(directory0 + "Graphs/Individual mice/Indexes/Independent/" + treatment + "/" + AnimalID + "IndependentIndex.jpg", orientation="landscape")
	plt.clf()
	CumulativeLeft = pd.DataFrame(CumulativeLeft)
	CumulativeMiddle = pd.DataFrame(CumulativeMiddle)
	CumulativeRight = pd.DataFrame(CumulativeRight)
	mouseCumulativeIndex = pd.concat([Hour, CumulativeLeft, CumulativeMiddle, CumulativeRight], axis=1)
	mouseCumulativeIndex.columns = ["Hour", "Left", "Middle", "Right"]
	del CumulativeLeft, CumulativeMiddle, CumulativeRight
	mouseCumulativeIndex = pd.concat([Name, Group, mouseCumulativeIndex, CumulativeIndex], axis=1)
	mouseCumulativeIndex.columns = ["Name", "Group", "Hour", "Left", "Middle", "Right", "CumulativeIndex"]
	plt.figsize=(18, 6)
	plt.plot(mouseCumulativeIndex["Hour"], mouseCumulativeIndex["CumulativeIndex"], "r-")
	plt.title(AnimalID + " " + treatment + " (Correct entries - Incorrect entries) / Total entries)")
	plt.xlabel("Hour", fontsize=18)
	plt.ylabel("Learning Index", fontsize=18)
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([-1.0, -0.5, 0, 0.5, 1.0])
	plt.savefig(directory0 + "Graphs/Individual mice/Indexes/Cumulative/" + treatment + "/" + AnimalID + "CumulativeIndex.jpg", orientation="landscape")
	plt.clf()
	mouseIndex = pd.concat([mouseIndex, mouse3], axis=1)
	mouseCumulativeIndex = pd.concat([mouseCumulativeIndex, mouse3], axis=1)
	mouseIndex.to_csv(directory0 + "Data/Indexes/Independent/" + treatment + "/" + AnimalID + "IndependentIndex.csv", index=False)
	mouseCumulativeIndex.to_csv(directory0 + "Data/Indexes/Cumulative/" + treatment + "/" + AnimalID + "CumulativeIndex.csv", index=False)
	del mouseIndex, LearningIndex
	del mouseCumulativeIndex, Hour, CumulativeIndex
	del mouse3

	sample = np.array(mouseInitial["Left"])
	Criterions = np.zeros(IDnumberofentries)
	EditedCriterion = np.zeros(IDnumberofentries)
	movingwindow(sample, IDnumberofentries, Criterions)
	ChangedCriterion(Criterions, IDnumberofentries, EditedCriterion)
	Time = np.array(mouseInitial["Time"])
	Time = pd.DataFrame(Time)
	Criterions = pd.DataFrame(Criterions)
	EditedCriterion = pd.DataFrame(EditedCriterion)
	EntryNumber = np.array(range(1, IDnumberofentries+1))
	EntryNumber = pd.DataFrame(EntryNumber)
	mouseInitial = pd.concat([Time, EntryNumber, Criterions, EditedCriterion], axis=1)
	mouseInitial.columns = ["Time", "EntryNumber", "Criterions", "CriterionMet"]
	IDETCSeventy = ETCSeventyfinder(mouseInitial["Criterions"], mouseInitial["EntryNumber"], IDnumberofentries)
	IDETCEighty = ETCEightyfinder(mouseInitial["Criterions"], mouseInitial["EntryNumber"], IDnumberofentries)
	IDETCNinety = ETCNinetyfinder(mouseInitial["Criterions"],  mouseInitial["EntryNumber"], IDnumberofentries)
	HourstoSeventy = HourstoCriterion(IDETCSeventy, mouseInitial["Time"], 1)
	HourstoEighty = HourstoCriterion(IDETCEighty, mouseInitial["Time"], 1)
	HourstoNinety = HourstoCriterion(IDETCNinety, mouseInitial["Time"], 1)
	IDSeventyQualifier = np.zeros(6000)
	Qualifier(IDSeventyQualifier, IDETCSeventy)
	IDSeventyQualifier = pd.DataFrame(IDSeventyQualifier)
	IDEightyQualifier = np.zeros(6000)
	Qualifier(IDEightyQualifier, IDETCEighty)
	IDEightyQualifier = pd.DataFrame(IDEightyQualifier)
	IDNinetyQualifier = np.zeros(6000)
	Qualifier(IDNinetyQualifier, IDETCNinety)
	IDNinetyQualifier = pd.DataFrame(IDNinetyQualifier)
	Name = np.full((6000), AnimalID)
	Name = pd.DataFrame(Name)
	Group = np.full((6000), Treatment)
	Group = pd.DataFrame(Group)
	mouseIDETCresults = pd.DataFrame([[AnimalID, Treatment, IDETCSeventy, IDETCEighty, IDETCNinety, HourstoSeventy, HourstoEighty, HourstoNinety]], columns=np.array(["AnimalID", "Treatment", "EntriestoSeventy", "EntriestoEighty", "EntriestoNinety", "HourstoSeventy", "HourstoEighty", "HourstoNinety"]))
	del HourstoSeventy, HourstoEighty, HourstoNinety
	mouseIDETCresults.to_csv(directory0 + "Data/Entries to Criterion/Initial Discrimination/" + treatment + "/" + AnimalID + "IDETCResults.csv", index=False)
	del mouseIDETCresults
	mouseInitialv2 = pd.concat([Name, Group, FullEntryNumber, IDSeventyQualifier, IDEightyQualifier, IDNinetyQualifier], axis=1)
	mouseInitialv2.columns = ["AnimalNumber", "Treatment", "EntryNumber", "SeventyQualifier", "EightyQualifier", "NinetyQualifier"]  
	del IDETCSeventy, IDETCEighty, IDETCNinety
	del IDSeventyQualifier, IDEightyQualifier, IDNinetyQualifier
	mouseInitialv2 = pd.concat([mouseInitialv2, mouse5], axis=1)
	mouseInitialv2.to_csv(directory0 + "Data/Initial Discrimination/" + treatment + "/" + AnimalID + "totalresults.csv", index=False)
	del sample, Criterions, EditedCriterion, Time, EntryNumber
	del mouseInitialv2
 
 
	sample = np.array(mouseReversal["Right"])
	Criterions = np.zeros(Revnumberofentries)
	EditedCriterion = np.zeros(Revnumberofentries)
	movingwindow(sample, Revnumberofentries, Criterions)
	ChangedCriterion(Criterions, Revnumberofentries, EditedCriterion)
	Time = np.array(mouseReversal["Time"])
	Time = pd.DataFrame(Time)
	Criterions = pd.DataFrame(Criterions)
	EditedCriterion = pd.DataFrame(EditedCriterion)
	EntryNumber = np.array(range(1, Revnumberofentries+1))
	EntryNumber = pd.DataFrame(EntryNumber)
	mouseReversal = pd.concat([Time, EntryNumber, Criterions, EditedCriterion], axis=1)
	mouseReversal.columns = ["Time", "EntryNumber", "Criterions", "CriterionMet"]
	RevETCSeventy = ETCSeventyfinder(mouseReversal["Criterions"], mouseReversal["EntryNumber"], Revnumberofentries)
	RevETCEighty = ETCEightyfinder(mouseReversal["Criterions"], mouseReversal["EntryNumber"], Revnumberofentries)
	RevETCNinety = ETCNinetyfinder(mouseReversal["Criterions"],  mouseReversal["EntryNumber"], Revnumberofentries)  
	HourstoSeventy = HourstoCriterion(RevETCSeventy, mouseReversal["Time"], 2)
	HourstoEighty = HourstoCriterion(RevETCEighty, mouseReversal["Time"], 2)
	HourstoNinety = HourstoCriterion(RevETCNinety, mouseReversal["Time"], 2)
	RevSeventyQualifier = np.zeros(6000)
	Qualifier(RevSeventyQualifier, RevETCSeventy)
	RevSeventyQualifier = pd.DataFrame(RevSeventyQualifier)
	RevEightyQualifier = np.zeros(6000)
	Qualifier(RevEightyQualifier, RevETCEighty)
	RevEightyQualifier = pd.DataFrame(RevEightyQualifier)
	RevNinetyQualifier = np.zeros(6000)
	Qualifier(RevNinetyQualifier, RevETCNinety)
	RevNinetyQualifier = pd.DataFrame(RevNinetyQualifier)
	mouseRevETCresults = pd.DataFrame([[AnimalID, Treatment, RevETCSeventy, RevETCEighty, RevETCNinety, HourstoSeventy, HourstoEighty, HourstoNinety]], columns=np.array(["AnimalID", "Treatment", "EntriestoSeventy", "EntriestoEighty", "EntriestoNinety", "HourstoSeventy", "HourstoEighty", "HourstoNinety"]))
	mouseRevETCresults.to_csv(directory0 + "Data/Entries to Criterion/Reversal/" + treatment + "/" + AnimalID + "RevETCresutls.csv", index=False)
	del mouseRevETCresults
	mouseReversalv2 = pd.concat([Name, Group, FullEntryNumber, RevSeventyQualifier, RevEightyQualifier, RevNinetyQualifier], axis=1) 
	mouseReversalv2.columns = ["AnimalNumber", "Treatment", "EntryNumber", "SeventyQualifier", "EightyQualifier", "NinetyQualifier"]
	del RevETCSeventy, RevETCEighty, RevETCNinety
	del RevSeventyQualifier, RevEightyQualifier, RevNinetyQualifier
	mouseReversalv2 = pd.concat([mouseReversalv2, mouse5], axis=1)
	mouseReversalv2.to_csv(directory0 + "Data/Reversal/" + treatment + "/" + AnimalID + "Reversal.csv", index=False)
	del mouse4, mouse5
	del sample, Criterions, EditedCriterion, Time, EntryNumber
	del mouseReversalv2
	del numberofentries, IDnumberofentries, Revnumberofentries
	del mouseInitial, mouseReversal
	del FullEntryNumber
	
	#Shelter = 0
	#Arrest  = 1
	#Moving  = 2
	#Using an l of 3
	
	mousePrepped = Prep(mouse)
	del mouse
	mouseAcc = RunningMedian(mousePrepped)	
	size = np.int32(len(mouseAcc))
	mouseAcc = mouseAcc[["Time", "X", "Y", "Distance moved", "InShelter"]]
	mouseAccArray = np.array(mouseAcc, dtype="float64")
	segmenttype = np.full((size, 1), 0, dtype="float64")
	mouseAccArray = np.concatenate((mouseAccArray, segmenttype), axis=1)
	#Run Result function
	mouseAccArray = Result(mouseAccArray, size)
	#Run Window Length function
	mouseAccArray = WindowLength(mouseAccArray, size)
	mouseAccI = pd.DataFrame(mouseAccArray)
	mouseAccI.columns = ["Time", "X", "Y", "Distance moved", "InShelter", "Segment Type"]
	del mouseAccArray
	frame = 1 / 15
	mouseAccI["Velocity"] = mouseAccI["Distance moved"] / frame
	mouseAccI["Velocity"][mouseAccI["Segment Type"] == 0] = 0
	mouseAccI["Velocity"][mouseAccI["Segment Type"] == 1] = 0
	#Run Activity
	mouseAccI = np.array(mouseAccI)
	mouseArray = Activity(mouseAccI, size)
	mouseFrame = pd.DataFrame(mouseArray)
	mouseFrame.columns = ["Distance moved", "Time moving", "HoursAfterStart", "Max Velocity", "Max Acceleration"]
	mouseFrame["HoursAfterStart"] = mouseFrame["HoursAfterStart"] / 3600
	mouseFrame = mouseFrame[mouseFrame["Distance moved"] > 0]
	mouseFrame.reset_index()
	mouseMov = mouseFrame
	mouseMov.to_csv(directory0 + "Data/Segmentation/Moving Segments/" + treatment + "/" + AnimalID + "movingsegments.csv", index=False)
	del mouseFrame
	#Run Frequency
	mouseMov["Distance moved"] = np.log2(mouseMov["Distance moved"])
	MovFreq = MovFrequency(mouseMov)
	MovFreq = MovFreq.sort_values(["Distance"], ascending=True)
	MovFreq = MovFreq.reset_index()
	MovFreq.to_csv(directory0 + "Data/Segmentation/Frequency/" + treatment + "/" + AnimalID + "MovementSegmentDistribution.csv", index=False)
	del MovFreq["index"]
	#Make Frequency graph
	plt.plot(MovFreq["Distance"], MovFreq["Frequency"])
	plt.title(AnimalID + "\nFrequency Distribution of Moving Segments \n(log2 intervals of 0.1) w61-59-57-57")	
	plt.xlabel("Log2 of Distance (cm)", fontsize=18)
	plt.xticks([-10, -5, 0, 5, 10])
	plt.yticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000])
	plt.ylabel("Frequency", fontsize=18)
	plt.savefig(directory0 + "Data/Segmentation/Graphs/Distribution/" + treatment + "/" + AnimalID + "MovementSegmentDistribution.jpg")
	plt.savefig(directory0 + "Graphs/Individual mice/Segmentation/" + treatment + "/" + AnimalID + "MovementSegmentDistribution.jpg")
	plt.clf()
	del mouseAcc, mouseMov, mouseAccI, MovFreq
	#Prep for Acceleration Analysis
	mouseMov1 = pd.read_csv(directory0 + "Data/Segmentation/Moving Segments/" + treatment + "/" + AnimalID + "movingsegments.csv")
	mouseMov2 = pd.read_csv(directory0 + "Data/Segmentation/Moving Segments/" + treatment + "/" + AnimalID + "movingsegments.csv")
	mouseAcc = Acceleration(mouseMov1, mouseMov2)
	mouseAcc.to_csv(directory0 + "Data/Segmentation/Acceleration/" + treatment + "/" + AnimalID + "Acceleration.csv", index=False)
	#Make Acceleration graph
	plt.plot(mouseAcc["Hour"], mouseAcc["Acceleration"], "green")
	plt.title(AnimalID + " " + treatment + " Max Acceleration")
	plt.xlabel("Hour")
	plt.ylabel("acceleration (cm/s²)")
	plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
	plt.yticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])
	plt.savefig(directory0 + "Data/Segmentation/Graphs/Acceleration/" + treatment + "/" + AnimalID + "Acc.jpg")
	plt.savefig(directory0 + "Graphs/Individual mice/Acceleration/" + treatment + "/" + AnimalID + "Acc.jpg")
	plt.clf()
	
	Figure(directory0 + "Graphs/Individual mice/", AnimalID, treatment)
	del mouseMov1, mouseMov2
	elapsed = (time.time()-start) / 60
	print(AnimalID + "imported in " + str(elapsed) + " minutes!")
 
os.chdir(inputdirectory)
inputs = os.listdir()

for z in inputs:
	PrepDirectory(z)

	
if __name__=='__main__':
	pool = mp.Pool(processes=3)
	pool.map_async(MouseImport, inputs)
	pool.close()
	pool.join()

