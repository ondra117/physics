$$
m_0, m_1\\
l_0, l_1\\
\theta_0, \theta_1
$$
$$
x_0 + iy_0 = z_0 = -il_0e^{i\theta_0}\\
x_1 + iy_1 = z_1 = -il_1e^{i\theta_1} + z_0
$$
$$
\dot{z_0} = -il_0e^{i\theta_0}i\dot{\theta_0} = l_0\dot{\theta_0}e^{i\theta_0}\\
\dot{z_1} = -il_1e^{i\theta_1}i\dot{\theta_1}+\dot{z_0} = l_1\dot{\theta_1}e^{i\theta_1} + l_0\dot{\theta_0}e^{i\theta_0}
$$
$$
|\dot{z_0}|^2 = l_0\dot{\theta_0}e^{i\theta_0}l_0\dot{\theta_0}e^{-i\theta_0} = l_0^2\theta_0^2\\
|\dot{z_1}|^2 = (l_1\dot{\theta_1}e^{i\theta_1} + l_0\dot{\theta_0}e^{i\theta_0})(l_1\dot{\theta_1}e^{-i\theta_1} + l_0\dot{\theta_0}e^{-i\theta_0}) = l_1^2\dot{\theta_1}^2 + l_0^2\dot{\theta_0}^2 + 2l_0\dot{\theta_0}l_1\dot{\theta_1}\cos(\theta_0 - \theta_1)\\
T = \frac{1}{2}m_0\dot{z_0}^2+\frac{1}{2}m_1\dot{z_1}^2 = \frac{1}{2}m_0l_0^2\dot{\theta_0}^2+\frac{1}{2}m_1(l_1^2\dot{\theta_1}^2 + l_0^2\dot{\theta_0}^2 + 2l_0\dot{\theta_0}l_1\dot{\theta_1}\cos(\theta_0 - \theta_1)) = \frac{1}{2}(m_0 + m_1)l_0^2\dot{\theta_0}^2 + \frac{1}{2}m_1l_1^2\dot{\theta_1}^2 + m_1l_0l_1\dot{\theta_0}\dot{\theta_1}\cos(\theta_0 - \theta_1)\\
$$
$$
y_0 = \Im(z_0) = \Im(-il_0e^{i\theta_0}) = l_0\Im(-i(\cos(\theta) + i\sin(\theta))) = l_0\Im(-i\cos(\theta) + \sin(\theta)) = -l_0cos(\theta_0)\\
y_1 = \Im(z_1) = \Im(-il_1e^{i\theta_1} + z_0) = -l_0cos(\theta_0) -l_1cos(\theta_1)\\
V = g(m_0y_0 + m_1y_1) = g(m_0(-l_0cos(\theta_0)) + m_1(-l_0cos(\theta_0) -l_1cos(\theta_1))) = -g(m_0l_0cos(\theta_0) + m_1l_0cos(\theta_0) + m_1l_1cos(\theta_1)) = -g(m_0 + m_1)l_0\cos(\theta_0) - gm_1l_1cos(\theta_1)
$$
$$
L = \frac{1}{2}(m_0 + m_1)l_0^2\dot{\theta_0}^2 + \frac{1}{2}m_1l_1^2\dot{\theta_1}^2 + m_1l_0l_1\dot{\theta_0}\dot{\theta_1}\cos(\theta_0 - \theta_1) + g(m_0 + m_1)l_0\cos(\theta_0) + gm_1l_1\cos(\theta_1)
$$
$$
\frac{d}{dt}\frac{dL}{d\dot{\theta_0}}-\frac{dL}{d\theta_0}=0\\
\frac{d}{dt}\frac{dL}{d\dot{\theta_1}}-\frac{dL}{d\theta_1}=0
$$
$$
\frac{dL}{d\dot{\theta_0}} = (m_0 + m_1)l_0^2\dot{\theta_0} + m_1l_0l_1\dot{\theta_1}\cos(\theta_0 - \theta_1)\\
\frac{dL}{d\theta_0} = -m_1l_0l_1\dot{\theta_0}\dot{\theta_1}\sin(\theta_0 - \theta_1) - g(m_0 + m_1)l_0\sin(\theta_0)\\
\frac{d}{dt}\frac{dL}{d\dot{\theta_0}} = \frac{d}{dt}(m_0 + m_1)l_0^2\dot{\theta_0} + m_1l_0l_1\dot{\theta_1}\cos(\theta_0 - \theta_1) = (m_0 + m_1)l_0^2\ddot{\theta_0} + m_1l_0l_1(\ddot{\theta_1}\cos(\theta_0 - \theta_1) - \dot{\theta_1}\sin(\theta_0 - \theta_1)(\dot{\theta_0} - \dot{\theta_1}))\\
\frac{d}{dt}\frac{dL}{d\dot{\theta_0}}-\frac{dL}{d\theta_0} = (m_0 + m_1)l_0^2\ddot{\theta_0} + m_1l_0l_1(\ddot{\theta_1}\cos(\theta_0 - \theta_1) - \dot{\theta_1}\sin(\theta_0 - \theta_1)(\dot{\theta_0} - \dot{\theta_1})) + m_1l_0l_1\dot{\theta_0}\dot{\theta_1}\sin(\theta_0 - \theta_1) + g(m_0 + m_1)l_0\sin(\theta_0) = (m_0 + m_1)l_0^2\ddot{\theta_0} + m_1l_0l_1\ddot{\theta_1}\cos(\theta_0 - \theta_1) + m_1l_0l_1\dot{\theta_1}^2\sin(\theta_0 - \theta_1) + g(m_0 + m_1)l_0\sin(\theta_0)\\
(m_0 + m_1)l_0^2\ddot{\theta_0} + m_1l_0l_1\ddot{\theta_1}\cos(\theta_0 - \theta_1) + m_1l_0l_1\dot{\theta_1}^2\sin(\theta_0 - \theta_1) + g(m_0 + m_1)l_0\sin(\theta_0) = 0\\
(m_0 + m_1)l_0\ddot{\theta_0} + m_1l_1\ddot{\theta_1}\cos(\theta_0 - \theta_1) + m_1l_1\dot{\theta_1}^2\sin(\theta_0 - \theta_1) + g(m_0 + m_1)\sin(\theta_0) = 0
$$
$$
\frac{dL}{d\dot{\theta_1}} = m_1l_1^2\dot{\theta_1} + m_1l_0l_1\dot{\theta_0}\cos(\theta_0 - \theta_1)\\
\frac{dL}{d\theta_1} = m_1l_0l_1\dot{\theta_0}\dot{\theta_1}\sin(\theta_0 - \theta_1) - gm_1l_1\sin(\theta_1)\\
\frac{d}{dt}\frac{dL}{d\dot{\theta_1}} = \frac{d}{dt}m_1l_1^2\dot{\theta_1} + m_1l_0l_1\dot{\theta_0}\cos(\theta_0 - \theta_1) = m_1l_1^2\ddot{\theta_1} + m_1l_0l_1(\ddot{\theta_0}\cos(\theta_0 - \theta_1) - \dot{\theta_0}\sin(\theta_0 - \theta_1)(\dot{\theta_0} - \dot{\theta_1}))\\
\frac{d}{dt}\frac{dL}{d\dot{\theta_1}}-\frac{dL}{d\theta_1} = m_1l_1^2\ddot{\theta_1} + m_1l_0l_1(\ddot{\theta_0}\cos(\theta_0 - \theta_1) - \dot{\theta_0}\sin(\theta_0 - \theta_1)(\dot{\theta_0} - \dot{\theta_1})) - m_1l_0l_1\dot{\theta_0}\dot{\theta_1}\sin(\theta_0 - \theta_1) + gm_1l_1\sin(\theta_1) = m_1l_1^2\ddot{\theta_1} + m_1l_0l_1\ddot{\theta_0}\cos(\theta_0 - \theta_1) - m_1l_0l_1\dot{\theta_0}^2\sin(\theta_0 - \theta_1) + m_1l_0l_1\dot{\theta_0}\dot{\theta_1}\sin(\theta_0 - \theta_1) - m_1l_0l_1\dot{\theta_0}\dot{\theta_1}\sin(\theta_0 - \theta_1) + gm_1l_1\sin(\theta_1) = m_1l_1^2\ddot{\theta_1} + m_1l_0l_1\ddot{\theta_0}\cos(\theta_0 - \theta_1) - m_1l_0l_1\dot{\theta_0}^2\sin(\theta_0 - \theta_1) + gm_1l_1\sin(\theta_1)\\
m_1l_1^2\ddot{\theta_1} + m_1l_0l_1\ddot{\theta_0}\cos(\theta_0 - \theta_1) - m_1l_0l_1\dot{\theta_0}^2\sin(\theta_0 - \theta_1) + gm_1l_1\sin(\theta_1) = 0\\
m_1l_1\ddot{\theta_1} + m_1l_0\ddot{\theta_0}\cos(\theta_0 - \theta_1) - m_1l_0\dot{\theta_0}^2\sin(\theta_0 - \theta_1) + gm_1\sin(\theta_1) = 0
$$
$$
(m_0 + m_1)l_0\ddot{\theta_0} + m_1l_1\ddot{\theta_1}\cos(\theta_0 - \theta_1) + m_1l_1\dot{\theta_1}^2\sin(\theta_0 - \theta_1) + g(m_0 + m_1)\sin(\theta_0) = 0\\
m_1l_1\ddot{\theta_1} + m_1l_0\ddot{\theta_0}\cos(\theta_0 - \theta_1) - m_1l_0\dot{\theta_0}^2\sin(\theta_0 - \theta_1) + gm_1\sin(\theta_1) = 0
$$
$$
\begin{pmatrix}
(m_0 + m_1)l_0 & m_1l_1\cos(\theta_0 - \theta_1) \\
m_1l_0\cos(\theta_0 - \theta_1) & m_1l_1
\end{pmatrix}
\begin{pmatrix}
\ddot{\theta_0} \\
\ddot{\theta_1}
\end{pmatrix}
=
\begin{pmatrix}
-m_1l_1\dot{\theta_1}^2\sin(\theta_0 - \theta_1) - g(m_0 + m_1)\sin(\theta_0) \\
m_1l_0\dot{\theta_0}^2\sin(\theta_0 - \theta_1) - gm_1\sin(\theta_1)
\end{pmatrix}\\
$$