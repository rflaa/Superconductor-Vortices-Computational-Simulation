import numpy as np
import matplotlib.pyplot as plt

#Valores dados
m = 1.0
k = 1.0
dt = 0.1
T = 20

#Condições iniciais
t = np.arange(0,T,dt)
x = np.zeros(len(t))
x[0] = 1.0
v0 = 0.0

#Função
a = (-k/m)*x[0]
x[1] = v0*dt + a*((dt**2)/2)

for n in range(1,len(t)-1):
    a = (-k/m)*x[n]
    x[n+1] = 2*x[n] - x[n-1] + a*dt**2

#Plot
plt.plot(t,x)
plt.xlabel("Tempo")
plt.ylabel("Posição")
plt.grid(True)
plt.show()
