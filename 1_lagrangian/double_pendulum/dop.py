import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "0_mathematics"))

import numpy as np

from rk4 import rk4


class DOP:
    def __init__(self, m0, l0, th0, m1, l1, th1, g=9.81, dth0=0, dth1=0):
        self.m0 = m0
        self.l0 = l0
        self.th0 = th0
        self.m1 = m1
        self.l1 = l1
        self.th1 = th1
        self.g = g
        self.dth0 = dth0
        self.dth1 = dth1

    def get_v(self):
        return np.array([self.th0, self.th1, self.dth0, self.dth1])

    def f(self, inp):
        th0, th1, dth0, dth1 = inp
        m0, l0, m1, l1, g = self.m0, self.l0, self.m1, self.l1, self.g

        d = th0 - th1

        m = np.array(
            [[(m0 + m1) * l0, m1 * l1 * np.cos(d)], [m1 * l0 * np.cos(d), m1 * l1]]
        )

        b = np.array(
            [
                -m1 * l1 * dth1**2 * np.sin(d) - g * (m0 + m1) * np.sin(th0),
                m1 * l0 * dth0**2 * np.sin(d) - g * m1 * np.sin(th1),
            ]
        )

        ddth0, ddth1 = np.linalg.solve(m, b)

        return np.array([dth0, dth1, ddth0, ddth1])

    def next(self, inp, dt):
        return rk4(inp, dt, self.f)

    def get_xy(self, inp):
        th0, th1, _, _ = inp
        z0 = -1j * self.l0 * np.exp(1j * th0)
        z1 = -1j * self.l1 * np.exp(1j * th1) + z0
        return np.array([z0.real, z0.imag, z1.real, z1.imag])
