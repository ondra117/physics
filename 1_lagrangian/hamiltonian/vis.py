import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from thr import Thr

m  = np.array([1.0, 1.0, 1.0])
x  = np.array([-0.97000436,  0.97000436, 0.0])
y  = np.array([ 0.24308753, -0.24308753, 0.0])
vx = np.array([-0.46620368, -0.46620368, 0.93240737])
vy = np.array([-0.43236573, -0.43236573, 0.86473146])
vx[2] *= 1.15
vy[2] *= 1.15
vx -= vx.mean()
vy -= vy.mean()
p  = (vx + 1j*vy) * m

thr = Thr(m, x, y, p)

dt = 0.002
steps_per_frame = 20
trail_len = 300

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

bodies, = ax.plot([], [], "o", ms=8)
trails = [
    ax.plot([], [], lw=1, alpha=0.6)[0]
    for _ in range(len(m))
]

def states():
    v = thr.get_v()

    tx = [[] for _ in range(len(m))]
    ty = [[] for _ in range(len(m))]

    while True:
        for _ in range(steps_per_frame):
            v = thr.next(v, dt)

        xy = thr.get_xy(v)
        x = xy[0]
        y = xy[1]

        for i in range(len(m)):
            tx[i].append(x[i])
            ty[i].append(y[i])

            if len(tx[i]) > trail_len:
                tx[i].pop(0)
                ty[i].pop(0)

        yield x, y, tx, ty

def update(frame):
    x, y, tx, ty = frame

    bodies.set_data(x, y)

    for i in range(len(m)):
        trails[i].set_data(tx[i], ty[i])

    return (bodies, *trails)

ani = FuncAnimation(
    fig,
    update,
    frames=states,
    interval=20,
    blit=True,
    cache_frame_data=False,
)

plt.show()