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
import cv2
import peak_finder as pf

##--------------------------------------------------------------------##
## Returns a numpy array of the complex numbers associated with the   ##
## selected mode. In practice, return will be appended to an external ##
## array with mode values from other .csv files                       ##
##--------------------------------------------------------------------##

#import *.csv into python memory
def complexcsv(filename, mode = 0, binsize = 10):
	temp = np.genfromtxt(filename, skip_header = 1, delimiter = ',').astype(np.complex)
	return temp[...,mode] + temp[...,mode+1]*1j

	
#takes mode-filtered complex fft data (e.g. from openyml()) and returns a histogram
def plotMode(modearray, mode, binsize = 10):
	qfig = Qfunc.qfuncimage(modearray[2*mode:2*mode+2], binsize)
	return qfig

	
#takes an unfiltered fft array and returns the peak indices (modes)
def findPeakModes(fftarray, smoothing = 7, finderwin = 20):
	absdata = absfft(fftarray)
	datashape = np.shape(absdata)
	smoothing = 2*smoothing + 1 #smoothing must be an odd number

	temparray = np.average(absdata, axis = 0)
	print np.shape(temparray)
	smoothdata = pf._smooth(temparray, window_len = smoothing)


	return pf.peakdetect(smoothdata, lookahead = finderwin)[0]
	

#opens raw yml file and returns matrix with fft values for specified region
def openyml(filename, mode = -1):
	if mode == -1: #for mode set to -1, return image data in a numpy array instead of fft data
		imagedata = np.array([])
		imagedata = cv2.cv.Load(filename, name = 'image')
		return imagedata
	
	else: #for a valid mode number, find the matching column and return subsequent values
		realfft = cv2.cv.Load(filename, name = 'fft-real')
		imagfft = cv2.cv.Load(filename, name = 'fft-imag')
		modeindex = mode
		
#--------------------
#the code here is for if only select modes were recorded in the array and thus the mode index and mode are not the same
#		modeindex = np.argwhere(realfft[0, :] == mode)[0,0] #finds the array index of the desired mode in the imported file
#		if modeindex != np.argwhere(imagfft[0, :] == mode)[0,0] #should be same as modeindexreal, but you never know....
#			return -1 #returns error for modeindex mismatch
#--------------------
		
		#initialize and set first row of output array
		fftdata = np.array([[realfft[0, modeindex],imagfft[0, modeindex]]])
		datashape = np.shape(realfft)
		for i in range(1, datashape[0]): #places real/imag pairs in successive rows
			fftdata = np.append(fftdata, [[realfft[i, modeindex], imagfft[i, modeindex]]], axis = 0)
			
		return fftdata

#creates an array with absolute fft values from a complex array of any even-width shape
def absfft(fftarray):
	fftshape = np.shape(fftarray)
	output = np.zeros([fftshape[0], fftshape[1]/2]) #initialize array of proper size
	for col in range (0, fftshape[1]/2):
		for row in range (0, fftshape[0]):
			absval = np.sqrt(fftarray[row, 2*col]**2 + fftarray[row, 2*col+1]**2) #find abs of 
			output[row, col] = absval
	return output