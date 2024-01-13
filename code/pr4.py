import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

f = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
A = [3, 2, 1, 1, 2, 1, 1, 1, 1, 1]
modulating_signal = np.zeros(1000)
for i in zip(A, f):
    modulating_signal += i[0] * np.sin(2 * np.pi * i[1] * t)

freq_carrier = 45
carrier_signal = 1 * np.sin(2 * np.pi * freq_carrier * t)
m = 0.9
max_value = max(max(modulating_signal), -min(modulating_signal))
output_signal = (1 + m * modulating_signal / max_value) * carrier_signal

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, carrier_signal)
plt.title('Несущий сигнал')

plt.subplot(3, 1, 2)
plt.plot(t, modulating_signal)
plt.title('Модулирующий сигнал')

plt.subplot(3, 1, 3)
plt.plot(t, output_signal)
plt.title('Сигнал на выходе (амплитудно-модулированный сигнал)')

plt.tight_layout()
plt.show()