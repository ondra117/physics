from osc import OSC
from analytic import get_analytic
from euler import get_euler
from beckward_euler import get_beckward_euler
from rk4 import get_rk4
import matplotlib.pyplot as plt

osc = OSC(1, 1, 0)

t_end = 1000
dt = 0.5
t_cut = int(990 // dt)

analytic_t, analytic_x = get_analytic(osc, dt, t_end)

euler_t, euler_x = get_euler(osc, dt, t_end)

beckward_euler_t, beckward_euler_x = get_beckward_euler(osc, dt, t_end)

rk4_t, rk4_x = get_rk4(osc, dt, t_end)

fig, ax = plt.subplots(figsize=(16, 8))

ax.plot(analytic_t[t_cut:], analytic_x[t_cut:], "-", label="analytic")
ax.plot(euler_t[t_cut:], euler_x[t_cut:], "-o", label="euler")
ax.plot(
    beckward_euler_t[t_cut:], beckward_euler_x[t_cut:], "-o", label="beckward_euler"
)
ax.plot(rk4_t[t_cut:], rk4_x[t_cut:], "-o", label="kr4")

ax.axhline(0, color="gray", lw=0.8)
ax.set_ybound(-3, 3)
ax.set_xlabel("čas  t")
ax.set_ylabel("poloha  x(t)")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
