# coding: utf-8
# we're going to model the data coming from an Excelon Camera
# at 1340x400 pixels. This is to get familiar with data from
# the quantum array detection experiments.
# from IPython.parallel import require
# import BeamOptics as bopt
# @require(bopt)


def exposure(NX=1024, NY=400, pitch=20e-6,
             wavelength=780e-9, theta=0.005, amp=100, phase=0):

    from scipy import pi, sin, cos, exp, conjugate, ogrid
    from numpy import random, real, imag, array, absolute, log
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
        exp(1j*phase)*plane_wave_beam(x, y, 0, 1e-12*amp, k2)

    intensity = total * total.conjugate()
                #+
                #darkcts*(random.random([max(shape(x)),max(shape(y))]) +
                #1j*random.random([max(shape(x)),max(shape(y))]))
                #add dark noise and QE
    print log(intensity[:, 200].sum())
    K = fftshift(fft(intensity[:, 200]))  # complex intensity after FFT2
    # print K[512] used to verify that the sum is equal to DC
    plt.plot(10*log(absolute(K)))  # power spectrum
    plt.show()
    return K[643]

# pixel of interest in FFT is 643 (this is 131 pixels away from
# the center @ 512) 131 pixels corresponds to the off-axis component
# of the wave: ∆K is 2π / (20e-6 * 1024) = 306.796 rad/m
# 306.796 * 131 is 40190 rad/m which is k * sin(0.005)
# where k = 2π/780e-9 = 8055365 rad/m TADA!

if __name__ == '__main__':
    print exposure()
