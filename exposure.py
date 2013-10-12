# coding: utf-8
# we're going to model the data coming from an Excelon Camera
# at 1340x400 pixels. This is to get familiar with data from
# the quantum array detection experiments.
# from IPython.parallel import require
# import BeamOptics as bopt
# @require(bopt)


def exposure(NX=1340, NY=400, pitch=20e-6,
             wavelength=780e-9, theta=0.005, amp=100, phase=0, trim=6):

    from scipy import pi, sin, cos, exp, conjugate, ogrid
    from numpy import random, real, imag, array, absolute, log, log10
    from numpy.fft import fft, fftshift
    from BeamOptics import plane_wave_beam
    import matplotlib.pyplot as plt

    px, py = ogrid[0:NX, 0:NY]  # pixel index
    # center = [NX/2, NY/2]  # center of the CCD sensor

    #physical coordinates, referenced from 0,0 (center of CCD)
    xmin = -(NX/2)*pitch
    xmax = (NX/2)*pitch
    ymin = -(NY/2)*pitch
    ymax = (NY/2)*pitch
    x, y = ogrid[xmin:xmax:pitch, ymin:ymax:pitch]

    k = 2*pi/wavelength
    k1 = [0, 0, k]
    k2 = [k*sin(theta), 0, k*cos(theta)]
    # pos = array([x, y])

    # darkcts = 0.0  # no idea what is reasonable here, just tinkering
    # seems best way to model detector is with partial loss (2%) and
    # added noise (dark counts)

    total = plane_wave_beam(x, y, 0, amp, k1) + \
        exp(1j*phase)*plane_wave_beam(x, y, 0, 1e-5*amp, k2)

    noise = random.random(total.shape)  # add some detector noise?
    # really not sure how best to add noise, but this gives the FFT
    # a realistic look.

    intensity = total * total.conjugate() + 2*noise # 0-2 counts per pixel
                #+
                #darkcts*(random.random([max(shape(x)),max(shape(y))]) +
                #1j*random.random([max(shape(x)),max(shape(y))]))
                #add dark noise and 

    # Calculate the relevant pixels:
    deltaK = 2*pi/(20e-6 * (1340-trim))
    Kx = k*sin(theta)
    pixel = Kx / deltaK
    print pixel + (1340-trim)/2.0

    # print intensity[0,200]
    # trim the last few elements before taking the FFT:
    # print "sum: ", log10(intensity[:-trim, 200].sum())
    # print "xN: ", log10(intensity[:-trim, 200] * (1340-trim))
    # complex intensity after FFT2, trim last few elements:
    K = fftshift(fft(intensity[:-trim, 200]))
    # print K[512] used to verify that the sum is equal to DC
    plt.plot(log10(absolute(K)))  # power spectrum
    plt.show()
    return K

    # Can find relative amplitude of sideband by dividing fourier amplitude
    # F(side) / F(DC) is equal to the amplitude ratio SB/DC.

# pixel of interest in FFT is 816.667 (this is 166.667 pixels away from
# the center @ 650) 166.667 pixels corresponds to the off-axis component
# of the wave: ∆K is 2π / (20e-6 * 1300) = 241.660973353061 rad/m
# 241.660973353061 * 166.667 is 40276.90 rad/m which is k * sin(0.005)
# where k = 2π/780e-9 = 8055365 rad/m TADA!

if __name__ == '__main__':
    print exposure()
