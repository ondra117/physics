# Prázdný vesmír
$$
\nabla\cdot E = 0\\
\nabla\cdot B = 0\\
\nabla \times E = -\frac{\partial B}{\partial t}\\
\nabla \times B = \mu_0\varepsilon_0\frac{\partial E}{\partial t}
$$
$$
\nabla \times E = -\frac{\partial B}{\partial t}\\
\nabla \times (\nabla \times E) = \nabla \times-\frac{\partial B}{\partial t}\\
\nabla \times (\nabla \times E) = -\frac{\partial}{\partial t}(\nabla \times B)\\
\nabla \times (\nabla \times E) = -\frac{\partial}{\partial t}\mu_0\varepsilon_0\frac{\partial E}{\partial t}\\
\nabla \times (\nabla \times E) = -\mu_0\varepsilon_0\frac{\partial^2 E}{{\partial t}^2}\\
\nabla(\nabla \cdot E) - \nabla^2E = -\mu_0\varepsilon_0\frac{\partial^2 E}{{\partial t}^2}\\
- \nabla^2E = -\mu_0\varepsilon_0\frac{\partial^2 E}{{\partial t}^2}\\
\nabla^2E = \mu_0\varepsilon_0\frac{\partial^2 E}{{\partial t}^2}\\
$$
## srovnani s vlnovou rovnici
$$
\nabla^2f = \frac{1}{v^2}\frac{\partial^2 f}{{\partial t}^2}\\
f = E\\
\frac{1}{v^2} = \mu_0\varepsilon_0
v^2 = \frac{1}{\mu_0\varepsilon_0}\\
v = \frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$
$$
\frac{1}{\sqrt{\mu_0\varepsilon_0}} = c
$$
# Roviná vlna v x -> f(x, t)
$$
\frac{\partial}{\partial y} = \frac{\partial}{\partial z} = 0\\
\nabla\cdot E = \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z} = 0\\
\frac{\partial E_x}{\partial x} = 0
$$
## elektrické pole nemíří po směru letu
$$
E = (0, E_y(x, t), 0)\\
\nabla \times E = -\frac{\partial B}{\partial t}\\
\left(\frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z}, \frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x}, \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\right) = -\frac{\partial B}{\partial t}\\
\left(0, 0, \frac{\partial E_y}{\partial x}\right) = -\frac{\partial B}{\partial t}\\
\frac{\partial B_x}{\partial t} = 0 \Rightarrow B_x = 0\\
\frac{\partial B_y}{\partial t} = 0 \Rightarrow B_y = 0\\
\frac{\partial B_z}{\partial t} = -\frac{\partial E_y}{\partial x}\\
$$
## pokud vlna letí směrem x a elektrické pole kmitá směrem y magnetické kmitá směrem z
$$
B = (0, 0, B_z(x, t))\\
\nabla \times B = \mu_0\varepsilon_0\frac{\partial E}{\partial t}\\
\left(\frac{\partial B_z}{\partial y} - \frac{\partial B_y}{\partial z}, \frac{\partial B_x}{\partial z} - \frac{\partial B_z}{\partial x}, \frac{\partial B_y}{\partial x} - \frac{\partial B_x}{\partial y}\right) = \mu_0\varepsilon_0\frac{\partial E}{\partial t}\\
\left(0, - \frac{\partial B_z}{\partial x}, 0\right) = \mu_0\varepsilon_0\frac{\partial E}{\partial t}\\
\mu_0\varepsilon_0\frac{\partial E_x}{\partial t} = 0 \Rightarrow E_x = 0\\
\mu_0\varepsilon_0\frac{\partial E_z}{\partial t} = 0 \Rightarrow E_x = 0\\
\mu_0\varepsilon_0\frac{\partial E_y}{\partial t} = - \frac{\partial B_z}{\partial x}\\
\frac{\partial E_y}{\partial t} = - \frac{1}{\mu_0\varepsilon_0}\frac{\partial B_z}{\partial x}\\
\frac{\partial E_y}{\partial t} = - c^2\frac{\partial B_z}{\partial x}\\
$$
## z jak jsme předpokládali
$$
\frac{\partial B_z}{\partial t} = -\frac{\partial E_y}{\partial x}\\
\frac{\partial E_y}{\partial t} = - c^2\frac{\partial B_z}{\partial x}\\
$$
$$
E_y(x, t) = E_0\sin(kx - wt)\\
\frac{\partial B_z}{\partial t} = -\frac{\partial E_y}{\partial x} = -E_0k\cos(kx - wt)\\
\frac{\partial B_z}{\partial t} = -E_0k\cos(kx - wt)\\
w\frac{\partial B_z}{\partial t} = -E_0kw\cos(kx - wt)\\
wB_z(x, t) = \int-E_0kw\cos(kx - wt)\ dt\\
wB_z(x, t) = -E_0k\sin(kx - wt)\\
B_z(x, t) = E_0\frac{k}{w}\sin(kx - wt)\\
$$
$$
\frac{\partial E_y}{\partial t} = - c^2\frac{\partial B_z}{\partial x} = -c^2E_0\frac{k^2}{w}\cos(kx - wt)\\
\frac{\partial E_y}{\partial t} = -c^2E_0\frac{k^2}{w}\cos(kx - wt)\\
E_y(x, t) = c^2E_0\frac{k^2}{w^2}\sin(kx - wt)\\
$$
$$
E_y(x, t) = E_y(x, t)\\
1 = c^2\frac{k^2}{w^2}\\
\frac{w^2}{k^2} = c^2\\
\frac{w}{k} = c\\
$$
$$
E_y(x, t) = E_0\sin(kx - kct)\\
B_z(x, t) = E_0\frac{1}{c}\sin(kx - kct)\\
$$