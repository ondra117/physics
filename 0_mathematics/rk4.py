def rk4(inp, dt, f):
    k1 = f(inp)
    k2 = f(inp + dt / 2 * k1)
    k3 = f(inp + dt / 2 * k2)
    k4 = f(inp + dt * k3)
    return inp + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)