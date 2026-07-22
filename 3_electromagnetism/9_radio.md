$$
\nabla\cdot E = \frac{\rho}{\varepsilon_0}\\
\nabla\cdot B = 0\\
\nabla \times E = -\frac{\partial B}{\partial t}\\
\nabla \times B =  \mu_0J + \mu_0\varepsilon_0\frac{\partial E}{\partial t}
$$
$$
J = \sigma E + J(x, y, t)\\
\nabla \times B =  \mu_0\sigma E + J(x, y, t) + \mu_0\varepsilon_0\frac{\partial E}{\partial t}
$$
$$
\nabla \times E = -\frac{\partial B}{\partial t}\\
\frac{\partial B}{\partial t} = -\nabla \times E\\
$$
$$
\nabla \times B =  \mu_0\sigma E + J(x, y, t) + \mu_0\varepsilon_0\frac{\partial E}{\partial t}\\
\mu_0\sigma E + J(x, y, t) + \mu_0\varepsilon_0\frac{\partial E}{\partial t} = \nabla \times B\\
\mu_0\varepsilon_0\frac{\partial E}{\partial t} = \nabla \times B - \mu_0\sigma E + J(x, y, t)\\
\frac{\partial E}{\partial t} = c^2\nabla \times B - \frac{\sigma E + J(x, y, t)}{\varepsilon_0}\\
$$
# Máme
$$
\frac{\partial B}{\partial t} = -\nabla \times E\\
\frac{\partial E}{\partial t} = c^2\nabla \times B - \frac{\sigma E + J(x, y, t)}{\varepsilon_0}\\
$$
## -> ODE
$$
\frac{\partial }{\partial z} = 0\\

\frac{\partial B_x}{\partial t} = -\frac{\partial E_z}{\partial y} + \frac{\partial E_y}{\partial z}\\
\frac{\partial B_x}{\partial t} = -\frac{\partial E_z}{\partial y}\\

\frac{\partial B_y}{\partial t} = -\frac{\partial E_x}{\partial z} + \frac{\partial E_z}{\partial x}\\
\frac{\partial B_y}{\partial t} = \frac{\partial E_z}{\partial x}\\

\frac{\partial B_z}{\partial t} =  \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}
$$
$$
\frac{\partial E_x}{\partial t} = c^2\left(\frac{\partial B_z}{\partial y} - \frac{\partial B_y}{\partial z}\right) - \frac{\sigma E_x + J_x(x, y, t)}{\varepsilon_0}\\
\frac{\partial E_x}{\partial t} = c^2\frac{\partial B_z}{\partial y} - \frac{\sigma E_x + J_x(x, y, t)}{\varepsilon_0}\\

\frac{\partial E_y}{\partial t} = c^2\left(\frac{\partial B_x}{\partial z} - \frac{\partial B_z}{\partial x}\right) - \frac{\sigma E_y + J_y(x, y, t)}{\varepsilon_0}\\
\frac{\partial E_y}{\partial t} = -c^2\frac{\partial B_z}{\partial x} - \frac{\sigma E_y + J_y(x, y, t)}{\varepsilon_0}\\

\frac{\partial E_z}{\partial t} = c^2\left(\frac{\partial B_y}{\partial x} - \frac{\partial B_x}{\partial y}\right) - \frac{\sigma E_z + J_z(x, y, t)}{\varepsilon_0}\\
$$
# ODE v pocatku je vse 0 krok J_x a J_y, tedy nemusime resit to co na nich neni zavyslé
$$
\frac{\partial B_z}{\partial t} =  \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\\
\frac{\partial E_x}{\partial t} = c^2\frac{\partial B_z}{\partial y} - \frac{\sigma E_x + J_x(x, y, t)}{\varepsilon_0}\\
\frac{\partial E_y}{\partial t} = -c^2\frac{\partial B_z}{\partial x} - \frac{\sigma E_y + J_y(x, y, t)}{\varepsilon_0}\\
$$