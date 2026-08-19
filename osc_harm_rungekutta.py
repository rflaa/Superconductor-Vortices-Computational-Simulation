import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

m = 1.0
k = 1.0

x0 = 1.0
v0 = 0.0

t0 = 0.0
tf = 20.0
dt = 0.1

def oscilador(t, y, m, k):
    x = y[0]
    v = y[1]
    dxdt = v
    dvdt = -(k/m)*x

    return [dxdt, dvdt]

sol = solve_ivp(
    oscilador,
    [t0,tf],
    [x0,v0],
    args=(m,k),
    method='RK45',
    t_eval=np.arange(t0,tf,dt),
    dense_output=True
)

t = sol.t
x = sol.y[0]
v = sol.y[1]

plt.plot(t, x)

plt.xlabel("Tempo")
plt.ylabel("Posição")

plt.grid()
plt.show()