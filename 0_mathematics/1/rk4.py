from osc import OSC
import numpy as np


def get_rk4(osc: OSC, dt: float, t_end: float):
    t = [0]
    x = [np.array([osc.x_0, osc.dx_0])]

    while t[-1] < t_end:
        t.append(t[-1] + dt)
        x.append(osc.rk4(x[-1], dt))

    return t, np.array(x)[:, 0]
