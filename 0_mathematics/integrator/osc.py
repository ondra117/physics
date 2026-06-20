import numpy as np
from dataclasses import dataclass


class OSC:
    def __init__(self, w: float, x_0: float | None = None, dx_0: float | None = None):
        self.w = w
        self.A = None
        self.B = None

        if x_0 is not None and dx_0 is not None:
            self.B = x_0 / 2 + 1j * dx_0 / (2 * w)
            self.A = x_0 - self.B

    def ana_x(self, t):
        """
        x''   = -w^2x
        x(0)  = x_0
        x'(0) = dx_0

        x(t) = e^(lt)

        x'' + w^2x = 0
        l^2e^(lt) + w^2e^(lr) = 0
        l^2 + w^2 = 0
        l^2 = -w^2
        l = ±iw
        x(t) = Ae^(iwt) + Be^(-iwt)

        x(0) = A + B
        x'(0) = iw(A - B)
        x(0) - B = A
        x'(0) = iw(x(0) - 2B)
        -ix'(0)/w = x(0) - 2B
        2B = x(0) + ix'(0)/w
        B = x(0)/2 + ix'(0)/2w

        B = x_0/2 + idx_0/2w
        A = x_0 - B
        """

        assert self.A is not None and self.B is not None, "ERROR: Mising x_0, dx_0"
        return np.real(
            self.A * np.exp(1j * self.w * t) + self.B * np.exp(-1j * self.w * t)
        )
