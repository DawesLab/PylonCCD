# coding: utf-8
# modified exposure.py in order to find best FFT length for narrow peaks


def manyffts(NX=1300, NY=400, pitch=20e-6,
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

    for trim in [1, 2, 3, 4, 5, 6, 7, 8]:
        K = fft(intensity[:-trim, 200])
        plt.plot(10*log(absolute(fftshift(K))), label=trim)  # power spectrum
        # plt.plot(absolute(K[166-10:166+10]), label=trim)  # power spectrum

    plt.legend(loc="upper left")
    plt.show()
    return K

# pixel of interest in FFT is 816.667 (this is 166.667 pixels away from
# the center @ 650) 166.667 pixels corresponds to the off-axis component
# of the wave: ∆K is 2π / (20e-6 * 1300) = 241.660973353061 rad/m
# 241.660973353061 * 166.667 is 40276.90 rad/m which is k * sin(0.005)
# where k = 2π/780e-9 = 8055365 rad/m TADA!

if __name__ == '__main__':
    print manyffts()
