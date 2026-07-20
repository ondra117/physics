import numpy as np
import matplotlib.pyplot as plt

N = 1000
L = 1
DT = 0.001
V = 0.0004 / DT
Z = 10


DX = L / N

xs = np.linspace(0, L, N)
data = np.zeros((2, N))

# data[1, 500:600] += 0.01 * np.sin(np.linspace(0, 1, 100) * np.pi * 2)

data[0, :] += 0.01 * np.exp(-((xs-0.3)/0.07)**2) * np.cos(2*np.pi*(xs-0.3)/0.06)

data[0, :] += 0.02 * np.exp(-((xs-0.7)/0.035)**2) * np.cos(20*np.pi*(xs-0.7)/0.06)


def update(inp):
    x, x_old = inp
    
    # xddx = (x[:-2] - 2 * x[1:-1] + x[2:]) / (DX ** 2) # d^2x/dx^2 = x_i-1 - 2x_i + x_i+1

    k = 2*np.pi*np.fft.fftfreq(N, d=DX)
    xddx = np.fft.ifft(-(k**2) * np.fft.fft(x)).real
    
    x_new = np.zeros_like(x)
    x_new = 2 * x - x_old + (V * DT)**2 * xddx
    x_new[:100] = 0

    return np.array([x_new, x])

while True:
    for _ in range(round(Z)):
        data = update(data)
        # data = rk4(data, DT, update)

    plt.clf()
    plt.plot(xs, data[0])
    plt.ylim(-1, 1)
    plt.pause(0.001)