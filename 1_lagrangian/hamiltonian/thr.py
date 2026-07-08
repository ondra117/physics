import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "0_mathematics"))

import numpy as np

from rk4 import rk4

G = 1

class Thr:
    def __init__(self, m, x, y, p=None):
        self.m = m
        self.z = x + 1j * y
        self.p = p if p is not None else np.zeros_like(self.z)
    
    def get_v(self):
        return np.array([self.z, self.p])
    
    def f(self, inp):
        z, p = inp
        m = self.m
        
        dz = p / m

        r = z[:, None] - z[None]
        dist = np.abs(r)
        np.fill_diagonal(dist, np.inf)

        dp = -G * np.sum(
            self.m[:, None] * self.m[None] * r / 
            dist ** 3, 
            axis=1
        )
        return np.array([dz, dp])
    
    def next(self, inp, dt):
        return rk4(inp, dt, self.f)
    
    def get_xy(self, inp):
        z, _ = inp
        return np.array([z.real, z.imag])