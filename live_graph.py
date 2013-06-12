import numpy as np
import matplotlib.pyplot as plt

plt.ion()
fig = plt.figure()
x = np.random.randn(16,1024) + np.sin(np.arange(1024))
ydata = abs(np.fft.fftshift(np.fft.fft(x[8,:])))
line, = plt.plot(ydata)
for i in range(50):
	x = np.random.randn(16,1024) + np.sin(np.arange(1024))
	ydata = abs(np.fft.fftshift(np.fft.fft(x[8,:])))
	line.set_ydata(ydata)
	plt.draw()

print "done"
