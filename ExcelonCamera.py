# we're going to model the data coming from an Excelon Camera at 1340x400 pixels. This is to get familiar with data from the quantum array detection experiments.

from pylab import *
from scipy import *
import BeamOptics as bopt
from numpy import random

NX = 1340
NY = 400
pitch = 20e-6 # 20 micron CCD pitch
px, py = ogrid[0:NX,0:NY] #pixel index
center = [NX/2, NY/2] # center of the CCD sensor

#physical coordinates, referenced from 0,0 (center of CCD)
xmin = -(NX/2)*pitch
xmax = (NX/2)*pitch
ymin = -(NY/2)*pitch
ymax = (NY/2)*pitch 
x,y = ogrid[xmin:xmax:pitch, ymin:ymax:pitch]

k1 = [0,0]
k2 = [80,0]
pos = array([x,y])
amp = 1.0

# gaussian_beam(x,y,z,E0,z0,w0,k)
total = bopt.gaussian_beam(x,y,0,1.0,0.01,0.005,[5e4,0,8e8]) + bopt.gaussian_beam(x,y,0,1.0e-8,0.01,0.005,[0,0,8e8]) + 1.0*random.random((1340,400))
intensity = total*total.conjugate()

f=figure()
subplot(1,3,1)
imshow(abs(intensity))

subplot(1,3,2)
kplot = imshow(log(fftshift(abs(fft2(intensity)))))
kplot.set_interpolation('nearest')

subplot(1,3,3)
newx = arange(NX)
plot(log(abs(fftshift(fft2(intensity))))[:,200],newx,".")
show()


