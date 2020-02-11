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
treatment = str(sys.argv[2])
directory0 = maindirectory + investigator + "/"

directory1 = directory0 + "Data/Segmentation/Frequency/" + treatment + "/"

now = datetime.datetime.now()
month = str(now.month)
day = str(now.day)
year = str(now.year)
today = month + "-" + day + "-" + year


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

	
data = CreateCohort(directory1)
data.to_csv(directory0 + "Spreadsheets/" + treatment + "frequency" + today + ".csv")