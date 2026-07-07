from osc import OSC
import numpy as np


def get_analytic(osc: OSC, dt: float, t_end: float):
    t = np.linspace(0, t_end, int(t_end / dt), endpoint=False)
    return t, list(map(osc.analytic, t))
