$$
(r, \phi)\\
m_0\\
m_1
$$
$$
x + iy = z = re^{i\phi}\\
\dot{z} = \dot{r}e^{i\phi} + ir\dot{\phi}e^{i\phi}\\
|\dot{z}|^2 = \dot{z}\bar{\dot{z}} = (\dot{r}e^{i\phi} + ir\dot{\phi}e^{i\phi})(\dot{r}e^{-i\phi} - ir\dot{\phi}e^{-i\phi}) = \dot{r}^2 + r^2\dot{\phi}^2\\
T = \frac{1}{2}m_1(\dot{r}^2 + r^2\dot{\phi}^2)
$$
$$
L = \frac{1}{2}m_1(\dot{r}^2 + r^2\dot{\phi}^2) - V(r)
$$
$$
\frac{\partial L}{\partial \phi} = 0\\
\frac{\partial L}{\partial \dot{\phi}} = m_1r^2\dot{\phi}\\
\frac{d}{dt}\frac{\partial L}{\partial \dot{\phi}} = \frac{d}{dt}m_1r^2\dot{\phi}\\
\frac{d}{dt}\frac{\partial L}{\partial \dot{\phi}}-\frac{\partial L}{\partial \phi} = \frac{d}{dt}m_1r^2\dot{\phi}\\
\frac{d}{dt}m_1r^2\dot{\phi} = 0\\
m_1r^2\dot{\phi} = konst\\
\dot{\phi} = konst\\
\ddot{\phi} = 0
$$
$$
E = T + V = H = \dot{q}\frac{\partial L}{\partial \dot{q}}-L\\
\frac{dH}{dt} = \ddot{q}\frac{\partial L}{\partial \dot{q}}+\dot{q}\frac{d}{dt}\frac{\partial L}{\partial \dot{q}}-\dot{q}\frac{\partial L}{\partial q}-\ddot{q}\frac{\partial L}{\partial \dot{q}}-\frac{\partial L}{\partial t} = \dot{q}\frac{d}{dt}\frac{\partial L}{\partial \dot{q}}-\dot{q}\frac{\partial L}{\partial q}-\frac{\partial L}{\partial t} = \dot{q}\left(\frac{d}{dt}\frac{\partial L}{\partial \dot{q}}-\frac{\partial L}{\partial q}\right)-\frac{\partial L}{\partial t} = -\frac{\partial L}{\partial t}= 0\\
\frac{dH}{dt} = 0\\
H = konst = E
$$