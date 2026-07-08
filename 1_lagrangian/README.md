$$
L=T-V
$$
$$
S=\int_{t_0}^{t_1}L\ dt
$$
$$
x_\epsilon(t)=x(t)+\epsilon\eta(t)
$$
$$
\dot{x_\epsilon}(t)=\dot{x}(t)+\epsilon\dot{\eta}(t)
$$
$$
\eta(t_0) = \eta(t_1) = 0
$$
$$
S(\epsilon)=\int_{t_0}^{t_1}L(x+\epsilon\eta,\dot{x}+\epsilon\dot{\eta},t)\ dt
$$
$$
\frac{dS}{d\epsilon}=\int_{t_0}^{t_1}\frac{d}{d\epsilon}L(x+\epsilon\eta,\dot{x}+\epsilon\dot{\eta},t)\ dt
$$
$$
\frac{dS}{d\epsilon}=\int_{t_0}^{t_1}\frac{dL}{dx}\frac{d(x+\epsilon\eta)}{d\epsilon}+\frac{dL}{d\dot{x}}\frac{d(\dot{x}+\epsilon\dot{\eta})}{d\epsilon}\ dt
$$
$$
\frac{dS}{d\epsilon}=\int_{t_0}^{t_1}\frac{dL}{dx}\eta+\frac{dL}{d\dot{x}}\dot{\eta}\ dt
$$
$$
\int_{t_0}^{t_1}\frac{dL}{d\dot{x}}\dot{\eta}\ dt = \left[\frac{dL}{d\dot{x}}\eta\right]_{t_0}^{t_1}-\int_{t_0}^{t_1}\frac{d}{dt}\frac{dL}{d\dot{x}}\eta\ dt = -\int_{t_0}^{t_1}\frac{d}{dt}\frac{dL}{d\dot{x}}\eta\ dt\\
$$
$$
\frac{dS}{d\epsilon}=\int_{t_0}^{t_1}\frac{dL}{dx}\eta-\frac{d}{dt}\frac{dL}{d\dot{x}}\eta\ dt
$$
$$
\frac{dS}{d\epsilon}=\int_{t_0}^{t_1}\left(\frac{dL}{dx}-\frac{d}{dt}\frac{dL}{d\dot{x}}\right)\eta\ dt
$$
$$
0=\int_{t_0}^{t_1}\left(\frac{dL}{dx}-\frac{d}{dt}\frac{dL}{d\dot{x}}\right)\eta\ dt
$$
$$
0=\frac{dL}{dx}-\frac{d}{dt}\frac{dL}{d\dot{x}}
$$
$$
\frac{d}{dt}\frac{dL}{d\dot{x}}-\frac{dL}{dx}=0
$$