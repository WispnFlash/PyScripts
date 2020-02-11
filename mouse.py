import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys


maindirectory = "G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/"
investigator = str(sys.argv[1])
treatment = str(sys.argv[2])
directory0 = maindirectory + investigator + "/"
directory1 = directory0 + "Data/Distance moved/" + treatment + "/"

class Strain():
	strainname = "A strain name"
	def __init__(self, strainname):
		self.strainname = strainname

class Mouse(Strain):
	name = "An Animal ID"
	treatment = "A treatment group"
	investigator = "An Investigator"
	def __init__(self, name, treatment, investigator):
		self.name = name
		self.treatment = treatment
		self.investigator = investigator
	def PersonalInfo(self):
		print(self.name)
		print(self.treatment)
		print(self.investigator)





		
os.chdir(directory1)
animals = os.listdir()		
		
data = pd.read_csv(animals[0])
mouse = Mouse(data["AnimalNumber"][0], data["Treatment"][0], investigator)
mouse.PersonalInfo()
mouse.strainname = "C57BL/6"
print(mouse.strainname)