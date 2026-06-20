from osc import OSC
import numpy as np


def get_ana(osc: OSC, dt: float, t_end: float):
    t = np.linspace(0, t_end, int(t_end / dt))
    return t, list(map(osc.ana_x, t))
