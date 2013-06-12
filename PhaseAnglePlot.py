import numpy as np
import matplotlib.pyplot as plt

def phasePlot(array): #Plots phase angle change over the data set
	fig = plt.figure()
	plt.xlabel("Sample Index")
	plt.ylabel("Phase Angle")
	plt.plot(np.angle(array))
	
	return fig