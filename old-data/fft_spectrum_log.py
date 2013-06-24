# IPython log file

get_ipython().magic(u'logstart fft_spectrum_log.py')
get_ipython().magic(u'run ExcelonCamera.py')
freqscale = 309.796 * arange(-512,512) * 1e-3
fig = figure()
gca().xaxis.set_major_locator(MaxNLocator(6))
plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
xlabel("$k_x$ (rad/mm)")
ylabel("Log(amplitude)")
savefig("spectrum_small.png")
get_ipython().system(u'open spectrum_small.png')
savefig("spectrum_small2.png")
exit()
