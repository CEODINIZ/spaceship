import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
def orbita(solucao, tempo):
    vx = solucao[0]
    vy = solucao[1]
    x = solucao[2]
    y = solucao[3]
    
    ft = (G*Mt*Mf)/(x**2 + y**2)
    fl = (G*Ml*Mf)/((xl-x)**2 + (yl-y)**2)
    cos0t = x/(math.sqrt(x**2 + y**2))
    sen0t = y/(math.sqrt(x**2 + y**2))
    cos0l = (xl-x)/(math.sqrt((xl-x)**2+ (yl-y)**2))
    sen0l = (yl-y)/(math.sqrt((xl-x)**2 + (yl-y)**2))
    dxdt = vx
    dvxdt = (fl*cos0l - ft*cos0t)/Mf
    dydt = vy
    dvydt = (fl*sen0l - ft*sen0t)/Mf
    return dvxdt,dvydt,dxdt,dydt


G = 6.67*10**(-11)
Mt = 5.972*10**24
Ml = 7.36*10**22
Mf = 6*10**4
xl = 384.4*10**3 #distancia da lua ate a terra 
yl = 0    #eixo y entre a terra e a lua na horizontal
#G = 1
#Mt=10
#Ml=10
#Mf=0.1
#xl=10
#yl=0
#ci = [0,2.2, 15,0]
ci = [0, 0 , xl/2, xl/2] #ponto generico na metade xl/2
tempo = np.arange(0, 200, 1)
resultado = odeint(orbita, ci, tempo)
plt.plot(resultado[:, 2], resultado[:, 3])
plt.grid(True)
plt.show()