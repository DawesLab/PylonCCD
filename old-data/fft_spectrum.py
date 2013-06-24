plot(freqscale,log(abs(fftshift(fft(intensity[:,200])))))
xlabel("$k_x$ (rad/mm)")
ylabel("Log(amplitude)")
