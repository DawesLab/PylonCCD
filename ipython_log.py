# IPython log file

get_ipython().magic(u'run ExcelonCamera.py')
get_ipython().magic(u'run ExcelonCamera.py')
plot(abs(fftshift(fft(intensity[:,200]))))
plot(log(abs(fftshift(fft(intensity[:,200])))))
arange(-512,511)
arange(-512,512)
freqscale = 306.796 * arange(-512,512)
shape(freqscale)
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
freqscale = 306.796 * arange(-512,512) * 0.001
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
freqscale = 306.796 * arange(-512,512) * 1e-6
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
freqscale = 306.796 * arange(-512,512) * 1e-3
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
xlabel("k_s (rad/mm)")
xlabel("$k_x$ (rad/mm)")
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
xlabel("$k_x$ (rad/mm)")
ylabel("Log(amplitude)")
fig = figure()
fig.subplots_adjust(bottom=0.2)
ax1 = fig.add_subplot(111)
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
xlabel("$k_x$ (rad/mm)")
ylabel("Log(amplitude)")
font = {'family' : 'normal', 'weight': 'bold', 'size': 22}
matplotlib.rc('font', **font)
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
matplotlib.matplotlib_fname()
get_ipython().magic(u'log start')
get_ipython().magic(u'logon')
get_ipython().magic(u'logstart')
exit()