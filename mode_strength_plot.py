#############################################
##                                         ##
## Imports .csv files of FFT's, finds peak ##
## values, and histogram strength of peak  ##
## modes.                                  ##
##                                         ##
#############################################


import csv
import numpy as np
import Qfunction as Qfunc
import yaml

#----------------------------------------------------------------------#
## Returns a numpy array of the complex numbers associated with the   ##
## selected mode. In practice, return will be appended to an external ##
## array with mode values from other .csv files                       ##
#----------------------------------------------------------------------#
def complexcsv(filename, mode = 0, binsize = 10): #import *.csv into python memory
	temp = np.genfromtxt(filename, skip_header = 1, delimiter = ',').astype(np.complex)
	return temp[...,mode] + temp[...,mode+1]*1j
	
def plotMode(mode = 0):
	binsize = 10
	qfig = Qfunc.qfuncimage(fftarray[2*mode:2*mode+2], binsize)
	return qfig

def findPeakMode(fftarray):
	##Possibly incorporate peak_finder here
	return 0
	
	
def openyml(filename): #opens raw yml file and returns matrix with fft values
	with codecs.open(filename, 'r', encoding='utf8') as file:
		yml_dict = yaml.safe_load(file)
		print type(yml_dict)