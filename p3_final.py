import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

g = 6.67
gg = -11
G = g*10**(gg) #n*m/kg
mt = 5.972
mtt = 24
Mt = mt*10**mtt #kg
ml = 7.36
mll = 22
Ml = ml*10**mll #kg
mff = 4
mfff = 6*10
Mf = mfff**mff #kg
xll = 384.4
xlll = 10**3
xl = xll*xlll #distancia da lua ate a terra AL
yl = 0    #eixo y entre a terra e a lua na horizontal
def orbita(solucao, tempo):
    vx = solucao[0]
    vy = solucao[1]
    x = solucao[2]
    y = solucao[3]
    ft_0 = (G*Mt*Mf)
    ft_1 = (x**2+y**2)
    ft_2 = ft_0/ft_1
    fl_0 = (G*Ml*Mf)
    fl_1 = (xl-x)**2 + (yl-y)**2
    fl_2 = fl_0/(fl_1)    
    cos0t_0 = math.sqrt(ft_1)
    cos0t = x/cos0t_0
    sen0t_0 = math.sqrt(ft_1)
    sen0t = y/sen0t_0
    cos0l = (xl-x)/math.sqrt(fl_1)
    sen0l = (yl-y)/math.sqrt(fl_1)
    dxdt = vx
    dvxdt = (fl_2*cos0l - ft_2*cos0t)/Mf
    dydt = vy
    dvydt = (fl_2*sen0l - ft_2*sen0t)/Mf
    return dvxdt,dvydt,dxdt,dydt
#ci = [0, 0 , xl/2, xl/2]
ci = [0,2.2, 15,0]    
tempo = np.arange(0, 0.547, 0.00001)
resultado = odeint(orbita, ci, tempo)
plt.plot(resultado[:, 2], resultado[:, 3])
plt.grid(True)
plt.show()