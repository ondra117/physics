$$
(r, \phi)\\
m_0\\
m_1
$$
$$
x + iy = z = re^{i\phi}\\
\dot{z} = \dot{r}e^{i\phi} + ir\dot{\phi}e^{i\phi}\\
|\dot{z}|^2 = \dot{z}\bar{\dot{z}} = (\dot{r}e^{i\phi} + ir\dot{\phi}e^{i\phi})(\dot{r}e^{-i\phi} - ir\dot{\phi}e^{-i\phi}) = \dot{r}^2 + r^2\dot{\phi}^2\\
T = \frac{1}{2}m_1(\dot{r}^2 + r^2\dot{\phi}^2)\\
V = \int G\frac{m_0m_1}{r^2}\ dr = -G\frac{m_0m_1}{r}\\
L = T - V = \frac{1}{2}m_1(\dot{r}^2 + r^2\dot{\phi}^2) + G\frac{m_0m_1}{r}
$$
$$
\frac{\partial L}{\partial r} = m_1r\dot{\phi}^2 - G\frac{m_0m_1}{r^2}\\
\frac{\partial L}{\partial \dot{r}} = m_1\dot{r}\\
\frac{d}{dt}\frac{\partial L}{\partial \dot{r}} = \frac{d}{dt}m_1\dot{r} = m_1\ddot{r}\\
\frac{d}{dt}\frac{\partial L}{\partial \dot{r}}-\frac{\partial L}{\partial r}= m_1\ddot{r} - m_1r\dot{\phi}^2 + G\frac{m_0m_1}{r^2}\\
m_1\ddot{r} - m_1r\dot{\phi}^2 + G\frac{m_0m_1}{r^2} = 0\\
\ddot{r} - r\dot{\phi}^2 + G\frac{m_0}{r^2} = 0
$$
$$
\frac{\partial L}{\partial \phi} = 0\\
\frac{\partial L}{\partial \dot{\phi}} = m_1r^2\dot{\phi}\\
\frac{d}{dt}\frac{\partial L}{\partial \dot{\phi}} = \frac{d}{dt}m_1r^2\dot{\phi}\\
\frac{d}{dt}\frac{\partial L}{\partial \dot{\phi}}-\frac{\partial L}{\partial \phi}=\frac{d}{dt}m_1r^2\dot{\phi}\\
\frac{d}{dt}m_1r^2\dot{\phi} = 0\\
m_1r^2\dot{\phi} = konst = \ell\\
\dot{\phi} = \frac{\ell}{m_1r^2}
$$
$$
\ddot{r} = r\dot{\phi}^2 - G\frac{m_0}{r^2}\\
\ddot{r} = \frac{\ell^2}{m_1^2r^3} - G\frac{m_0}{r^2}\\
$$
$$
\ddot{r} = \frac{\ell^2}{m_1^2r^3} - G\frac{m_0}{r^2}\\
\dot{\phi} = \frac{\ell}{m_1r^2}
$$
$$
m_1\ddot{r} = \frac{\ell^2}{m_1r^3} - G\frac{m_0m_1}{r^2} = \frac{d}{dr}\left(G\frac{m_0m_1}{r} - \frac{\ell^2}{2m_1r^2}\right)\\
V_{eff}(r) = G\frac{m_0m_1}{r} - \frac{\ell^2}{2m_1r^2}
$$