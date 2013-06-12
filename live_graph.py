import numpy as np
import matplotlib.pyplot as plt

plt.ion()
fig = plt.figure()
#x = np.random.randn(512,512)
#plt.imshow(abs(np.fft.fftshift(np.fft.fft(x,axis=1),axes=1)))
for i in range(50):
	x = np.random.randn(128,256)
	plt.imshow(abs(np.fft.fftshift(np.fft.fft(x,axis=1),axes=1)))
	fig.canvas.draw()

print "done"
