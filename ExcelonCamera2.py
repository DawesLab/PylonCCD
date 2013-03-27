# we're going to model the data coming from an Excelon Camera at 1340x400 pixels. This is to get familiar with data from the quantum array detection experiments.
# coding=utf-8
from pylab import *
from scipy import *
import BeamOptics as bopt
from numpy import random, real, imag
import Qfunction as qf
import pyfftw

NX = 1024 #select an FFT-friendly subset of the array
NY = 400
pitch = 20e-6 # 20 micron CCD pitch in meters
px, py = ogrid[0:NX,0:NY] # pixel index
center = [NX/2, NY/2] # center of the CCD sensor

#physical coordinates, referenced from 0,0 (center of CCD), in meters
xmin = -(NX/2)*pitch
xmax = (NX/2)*pitch
ymin = -(NY/2)*pitch
ymax = (NY/2)*pitch 
x,y = ogrid[xmin:xmax:pitch, ymin:ymax:pitch]

k = 2*pi/780e-9 # in radians per meter
theta = 0.005 #radian measure of beam angle
k1 = [0,0,k]
k2 = [k*sin(theta),0,k*cos(theta)]
pos = array([x,y])
amp = 380

darkcts = 0.0 # no idea what is reasonable here, just tinkering
# the ccd specifies 2-3 electrons per pixel per hour

# seems best way to model (classical) detector is with partial loss (2%) and added noise (dark counts)

original = pyfftw.n_byte_align_empty(1024,16, dtype=complex128)
output = pyfftw.n_byte_align_empty(1024,16, dtype=complex128)

fft_forward = pyfftw.FFTW(original, output, flags=('FFTW_PATIENT',))

values = []
for i in range(5000): #this is the loop to parallelize
    print i
    total = bopt.plane_wave_beam(x,y,0,amp,k1) + exp(1j*1)*bopt.plane_wave_beam(x,y,0,0.001*amp,k2) 

    intensity = total * total.conjugate() #+ darkcts*(random.random([max(shape(x)),max(shape(y))]) + 1j*random.random([max(shape(x)),max(shape(y))])) # add dark noise and QE
    original[:] = intensity[:,200]
    fft_forward.execute()
    K = fftshift(output) # complex intensity after FFT2
    values.append(K[643]/1e5)

# pixel of interest in FFT is 643 (this is 131 pixels away from the center @ 512)
# 131 pixels corresponds to the off-axis component of the wave:
# ∆K is 2π / (20e-6 * 1024) = 306.796 rad/m
# 306.796 * 131 is 40190 rad/m which is k * sin(0.005) where k = 2π/780e-9 = 8055365 rad/m
# TADA!

qfuncoutput = qf.qfuncimage(real(values),imag(values),30)
show()
