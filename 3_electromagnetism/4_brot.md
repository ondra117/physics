$$
B = \frac{\mu_0}{2\pi r}I\\
I = \int_S J\ dA
$$
# Curkulace po kružnici R
$$
\oint_S B\ dl = \frac{\mu_0}{2\pi R}I \cdot 2\pi R = \mu_0I\\
\int_S\nabla \times B\ dA = \oint_S B\ dl = \mu_0I = \mu_0\int_S J\ dA = \int_S \mu_0J\ dA\\
\int_S\nabla \times B\ dA = \int_S\mu_0J\ dA\\
\nabla \times B = \mu_0J
$$
# Oprava chyby
$$
\nabla \cdot (\nabla \times F) = 0
$$
$$
\nabla \times B = \mu_0J\\
\nabla \cdot (\nabla \times B) = \nabla \cdot \mu_0J\\
0 = \mu_0\nabla \cdot J\\
0 = \nabla \cdot J
$$
## neplati u kondenzatoru
$$
\nabla \cdot J \neq 0
$$
# Řešení
## co tece mezi plochy kondenzatoru
$$
\oint_S E\ dA = \frac{Q}{\varepsilon_0}\\
I = \frac{dQ}{dt}
$$
$$
EA = \frac{Q}{\varepsilon_0}\\
Q = \varepsilon_0EA\\
I = \frac{dQ}{dt} = \frac{d\varepsilon_0EA}{dt} = \varepsilon_0A\frac{dE}{dt}\\
I = \varepsilon_0A\frac{dE}{dt}
$$
## zmena elektrickeho pole se da intepretovat jako proud a to i ve vzduchu
# Oprava
$$
B = \frac{\mu_0}{2\pi r}\left(I+\varepsilon_0\frac{dE}{dt}\right)\\
I = \int_S J\ dA
$$
$$
\oint_S B\ dl = \frac{\mu_0}{2\pi R}\left(I+\varepsilon_0\frac{dE}{dt}\right) \cdot 2\pi R = \mu_0\left(I+\varepsilon_0\frac{dE}{dt}\right)\\
\int_S\nabla \times B\ dA = \oint_S B\ dl = \mu_0\left(I+\varepsilon_0\frac{dE}{dt}\right) = \mu_0\left(\int_S J\ dA + \varepsilon_0\frac{d}{dt}\int_SE\ dA\right) = \mu_0\left(\int_S J\ dA + \int_S\varepsilon_0\frac{\partial E}{\partial t}\ dA\right) = \mu_0\int_S J + \varepsilon_0\frac{\partial E}{\partial t}\ dA = \int_S \mu_0J + \mu_0\varepsilon_0\frac{\partial E}{\partial t}\ dA\\
\int_S\nabla \times B\ dA = \int_S \mu_0J + \mu_0\varepsilon_0\frac{\partial E}{\partial t}\ dA\\
\nabla \times B =  \mu_0J + \mu_0\varepsilon_0\frac{\partial E}{\partial t}
$$