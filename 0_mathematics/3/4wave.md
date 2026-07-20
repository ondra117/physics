# Řetez kuliček
hmotnost M

pružina tukost K

klidova delka A

$f(n, t) = \Delta x$

## prava pruzina
$$
k(f(n+1, t) - f(n, t)) = F_p
$$
## leva pruzina
$$
k(f(n, t) - f(n-1, t)) = F_l
$$
## celkově
$$
F = F_p - F_l = K(f(n+1, t) - f(n, t)) - K(f(n, t) - f(n-1, t)) = K(f(n+1, t) - f(n, t) - f(n, t) + f(n-1, t)) = K(f(n+1, t) - 2f(n, t) + f(n-1, t))\\
K(f(n+1, t) - 2f(n, t) + f(n-1, t)) = F = Ma = M\frac{\partial^2 f(n, t)}{{\partial t}^2}\\
K(f(n+1, t) - 2f(n, t) + f(n-1, t)) = M\frac{\partial^2 f(n, t)}{{\partial t}^2}\\
f(n+1, t) - 2f(n, t) + f(n-1, t) = \frac{M}{K}\frac{\partial^2 f(n, t)}{{\partial t}^2}
$$
# f(n, t) -> f(x, t), A -> 0
$$
f(x+A, t) - 2f(x, t) + f(x-A, t) = \frac{M}{K}\frac{\partial^2 f}{{\partial t}^2}\\
f(x+A, t) - 2f(x, t) + f(x-A, t) = \frac{MA}{C}\frac{\partial^2 f}{{\partial t}^2}\\
f(x+A, t) - 2f(x, t) + f(x-A, t) = \frac{\rho A^2}{C}\frac{\partial^2 f}{{\partial t}^2}\\
\frac{f(x+A, t) - 2f(x, t) + f(x-A, t)}{A} = \frac{\rho A}{C}\frac{\partial^2 f}{{\partial t}^2}\\
\frac{f(x+A, t) - f(x, t)}{A} - \frac{f(x, t) -f(x-A, t)}{A} = \frac{\rho A}{C}\frac{\partial^2 f}{{\partial t}^2}\\
\frac{\partial f}{\partial x}(x) - \frac{\partial f}{\partial x}(x-A) = \frac{\rho A}{C}\frac{\partial^2 f}{{\partial t}^2}\\
\frac{\frac{\partial f}{\partial x}(x) - \frac{\partial f}{\partial x}(x-A)}{A} = \frac{\rho}{C}\frac{\partial^2 f}{{\partial t}^2}\\
\frac{\partial^2 f}{{\partial x}^2} = \frac{\rho}{C}\frac{\partial^2 f}{{\partial t}^2}\\
\frac{\partial^2 f}{{\partial x}^2} = \frac{1}{v^2}\frac{\partial^2 f}{{\partial t}^2}\\
\nabla^2f = \frac{1}{v^2}\frac{\partial^2 f}{{\partial t}^2}\\
$$
$$
\frac{\partial^2 f}{{\partial t}^2} = v^2\nabla^2f
$$