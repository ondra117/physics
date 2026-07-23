import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dop import DOP

dop = DOP(m0=1, l0=1, th0=2.5, m1=1, l1=1, th1=2.5)
dt = 0.005
steps_per_frame = 5
trail_len = 400

fig, ax = plt.subplots(figsize=(6, 6))
L = dop.l0 + dop.l1
ax.set_xlim(-1.15 * L, 1.15 * L)
ax.set_ylim(-1.15 * L, 1.15 * L)
ax.set_aspect("equal")
ax.axis("off")

(line,) = ax.plot([], [], "o-", lw=2, color="#2E5A88", markersize=9)
(trace,) = ax.plot([], [], "-", lw=1, color="#D85A30", alpha=0.6)


def states():
    v = dop.get_v()  # stav žije tady, žádné global
    tx, ty = [], []
    while True:
        for _ in range(steps_per_frame):
            v = dop.next(v, dt)
        x0, y0, x1, y1 = dop.get_xy(v)
        tx.append(x1)
        ty.append(y1)
        if len(tx) > trail_len:
            tx.pop(0)
            ty.pop(0)
        yield x0, y0, x1, y1, list(tx), list(ty)


def update(frame):
    x0, y0, x1, y1, tx, ty = frame
    line.set_data([0, x0, x1], [0, y0, y1])
    trace.set_data(tx, ty)
    return line, trace


ani = FuncAnimation(
    fig, update, frames=states, interval=20, blit=True, cache_frame_data=False
)
plt.show()
