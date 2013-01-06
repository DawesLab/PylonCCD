# we're going to model the data coming from an Excelon Camera at 1340x400 pixels. This is to get familiar with data from the quantum array detection experiments.

from pylab import *
from scipy import *
import BeamOptics as bopt
from numpy import random, real, imag
import Qfunction as qf

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

k = 2*pi/780e-9
theta = 0.005 #radian measure of beam angle
k1 = [0,0,k]
k2 = [k*sin(theta),0,k*cos(theta)]
pos = array([x,y])
amp = 10.0

darkcts = 0.001 # no idea what is reasonable here, just tinkering
# seems best way to model detector is with partial loss (2%) and added noise (dark counts)

# gaussian_beam(x,y,z,E0,z0,w0,k)
#total = bopt.gaussian_beam(x,y,0,1.0,0.01,0.005,k2) + bopt.gaussian_beam(x,y,0,0.0,0.01,0.005,k2)
#total = bopt.gaussian_beam(x,y,0,10,0.02,0.005,k2) 
#total = bopt.plane_wave_beam(x,y,0,amp,k2) + bopt.plane_wave_beam(x,y,0,0.1,k1)
values = []
for i in range(1000):
	print i
	total = bopt.plane_wave_beam(x,y,0,amp,k1) + bopt.plane_wave_beam(x,y,0,1e-5,k2) 
	intensity = total * total.conjugate() + darkcts*random.random([max(shape(x)),max(shape(y))]) # add dark noise and QE
	K = fftshift(fft2(intensity)) # complex intensity after FFT2
	values.append(K[842,200]/1e3)

# pixel of interest in FFT is 842

# f=figure()
# subplot(1,3,1)
# imshow(abs(intensity))

# subplot(1,3,2)
# kplot = imshow(log(fftshift(abs(fft2(intensity)))))
# kplot.set_interpolation('nearest')

# subplot(1,3,3)
# newx = arange(NX)
# plot(log(abs(fftshift(fft2(intensity))))[:,200],newx,".",ms=3)
# show()

qfuncoutput = qf.qfuncimage(real(values),imag(values),10)
show()
