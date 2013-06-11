import numpy as np
import matplotlib as plt

def phasePlot(array,) #Plots phase angle change over the data set
	x = np.real(array)
	y = np.imag(array)
	
	fig = plt.figure()
	plt.xlabel("Sample Index")
	plt.ylabel("Phase Angle")
	plt.plot(atan2(y,x))
	
	return fig