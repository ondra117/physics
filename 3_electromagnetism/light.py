import numpy as np
import matplotlib.pyplot as plt

k = 1
A = 1

dt = 0.000000001

c = 299_792_458
t = 0

x = np.linspace(0, 4*np.pi, 400)

fig = plt.figure(figsize=(11, 5))
ax = fig.add_subplot(111, projection='3d')

while True:
    t += dt
    E = A * np.sin(k * x + k * c * t)
    B = A / c * np.sin(k * x + k * c * t)
    plt.cla()
    for i in range(0, len(x), 16):
        ax.quiver(x[i], 0, 0, 0, 0, E[i], color='#534AB7', arrow_length_ratio=0.3)
        ax.quiver(x[i], 0, 0, 0, B[i], 0, color='#D85A30', arrow_length_ratio=0.3)
    ax.plot(x, 0, E, color='#534AB7', lw=0.5, label='B (podel z)')
    ax.plot(x, B, 0, color='#D85A30', lw=0.5, label='E (podel y)')
    ax.plot(x, 0, 0, color='gray', lw=1, ls='--')
    plt.pause(1 / 60)