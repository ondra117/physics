$$
p = \frac{\partial L}{\partial \dot{q}}\\
H = p\dot{q} - L
$$
$$
dH = \frac{\partial H}{\partial q}dq + \frac{\partial H}{\partial p}dp\\
dH = dp\dot{q} + pd\dot{q} - \frac{\partial L}{\partial q}dq - \frac{\partial L}{\partial \dot{q}}d\dot{q} = dp\dot{q} + pd\dot{q} - \frac{\partial L}{\partial q}dq - pd\dot{q} = dp\dot{q} - \frac{\partial L}{\partial q}dq\\
\frac{\partial H}{\partial q}dq + \frac{\partial H}{\partial p}dp = dp\dot{q} - \frac{\partial L}{\partial q}dq\\
\left(\frac{\partial H}{\partial q} + \frac{\partial L}{\partial q}\right)dq + \left(\frac{\partial H}{\partial p} - \dot{q}\right)dp = 0\\
\dot{q} = \frac{\partial H}{\partial p}\\
\frac{\partial L}{\partial q} = -\frac{\partial H}{\partial q}\\
\frac{\partial L}{\partial q} = \frac{d}{dt}\frac{\partial L}{\partial \dot{q}} = \frac{d}{dt}p = \dot{p}
$$
$$
\dot{q} = \frac{\partial H}{\partial p}\\
\dot{p} = -\frac{\partial H}{\partial q}
$$