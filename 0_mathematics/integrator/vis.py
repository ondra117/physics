from osc import OSC
from ana import get_ana
import matplotlib.pyplot as plt

osc = OSC(1, 1, 0)

t_end = 20
dt = 0.01

ana_t, ana_x = get_ana(osc, dt, t_end)

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(ana_t, ana_x)

ax.axhline(0, color="gray", lw=0.8)
ax.set_xlabel("čas  t")
ax.set_ylabel("poloha  x(t)")
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
