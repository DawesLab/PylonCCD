# IPython log file

import cv2
test_data = cv2.cv.Load("test.yml",name="image")
get_ipython().magic(u'logstart')
test_data.shape()
shape(test_data)
get_ipython().magic(u'pylab')
import pylab
from numpy import *
shape(test_data)
test_data[:,5]
test_data[5,:]
test_data[5,750]
transform = fft.fft(test_data[5,:])
transform.shape()
shape(transform)
transform
transform.max()
transform.min()
test_data.sum()
test_data[5,:].sum()
sum(test_data[5,:])
print "the sum of the elements is equal to the max component"
transform[0]
transform[0,:]
shape(transform)
transform
transform[0,0]
exit()
