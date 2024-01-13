import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 1, 1000)
A = [1.4, 0.35, 0.15, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04] # Амплитуды
f = [11.1, 33.2, 55.3, 77.4, 99.5, 121.6, 143.8, 165.9, 188.0, 210.1] # Частоты
signal = [0] * 10
signal[0] = A[0] * np.sin(2 * np.pi * f[0] * time)
signal[1] = A[1] * np.sin(2 * np.pi * f[1] * time)
signal[2] = A[2] * np.sin(2 * np.pi * f[2] * time)
signal[3] = A[3] * np.sin(2 * np.pi * f[3] * time)
signal[4] = A[4] * np.sin(2 * np.pi * f[4] * time)
signal[5] = A[5] * np.sin(2 * np.pi * f[5] * time)
signal[6] = A[6] * np.sin(2 * np.pi * f[6] * time)
signal[7] = A[7] * np.sin(2 * np.pi * f[7] * time)
signal[8] = A[8] * np.sin(2 * np.pi * f[8] * time)
signal[9] = A[9] * np.sin(2 * np.pi * f[9] * time)
signal = sum(signal)

spectrum = np.fft.fft(signal) / len(signal) * 2
freq = np.fft.fftfreq(len(signal), 1 / len(signal))

plt.figure(figsize=(10, 8))
plt.subplot(4, 1, 1)
plt.plot(time, signal)

plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.title('Временная диаграмма сигнала')
plt.grid(True, color='lightgray')

plt.subplot(4, 1, (2, 4))
plt.plot(freq, np.abs(spectrum))
plt.xlim(0, f[9] * 1.5)
plt.xlabel('Частота')
plt.ylabel('Магнитуда (спектральная мощность)')
plt.title('Спектр сигнала')

plt.tight_layout()
plt.grid(True, color='lightgray')

plt.show()