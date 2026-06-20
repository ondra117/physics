import numpy as np


class OSC:
    def __init__(self, w: float, x_0: float | None = None, dx_0: float | None = None):
        self.w = w
        self.x_0 = x_0
        self.dx_0 = dx_0
        self.A = None
        self.B = None

        if x_0 is not None and dx_0 is not None:
            self.B = x_0 / 2 + 1j * dx_0 / (2 * w)
            self.A = x_0 - self.B

    def analytic(self, t):
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

        assert self.x_0 is not None and self.dx_0 is not None, "ERROR: Mising x_0, dx_0"
        return np.real(
            self.A * np.exp(1j * self.w * t) + self.B * np.exp(-1j * self.w * t)
        )

    def f(self, inp):
        """
        x'' = -w^2x

        v' = -w^2x
        x' = v
        """
        x, v = inp
        return np.array([v, -(self.w**2) * x])

    def euler(self, inp, dt):
        """
        v(t + dt) = v(t) + dt * v'
        x(t + dt) = x(t) + dt * x'
        """

        x, v = inp
        dx, dv = self.f(inp)

        new_v = v + dt * dv
        new_x = x + dt * dx
        return np.array([new_x, new_v])

    def beckward_euler(self, inp, dt):
        """
        x'' = -w^2x

        v' = -w^2x
        x' = v

        v(t + dt) = v(t) + dt * v'(x(t + dt))
        x(t + dt) = x(t) + dt * x'(v(t + dt))
        v(t + dt) = v(t) + dt * -w^2x(t + dt)
        x(t + dt) = x(t) + dt * v(t + dt)

        v(t + dt) = v(t) + dt * -w^2(x(t) + dt * v(t + dt))
        v(t + dt) = v(t) - dt * w^2 * x(t) - dt^2 * w^2 * v(t + dt)
        v(t + dt) + dt^2 * w^2 * v(t + dt) = v(t) - dt * w^2 * x(t)
        v(t + dt) * (1 + dt^2 * w^2) = v(t) - dt * w^2 * x(t)
        v(t + dt) = (v(t) - dt * w^2 * x(t)) / (1 + dt^2 * w^2)

        v(t + dt) = (v(t) - dt * w^2 * x(t)) / (1 + dt^2 * w^2)
        x(t + dt) = x(t) + dt * v(t + dt)
        """

        x, v = inp

        new_v = (v - dt * self.w**2 * x) / (1 + dt**2 * self.w**2)
        new_x = x + dt * new_v

        return np.array([new_x, new_v])

    def rk4(self, inp, dt):
        k1 = self.f(inp)
        k2 = self.f(inp + dt / 2 * k1)
        k3 = self.f(inp + dt / 2 * k2)
        k4 = self.f(inp + dt * k3)
        return inp + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
