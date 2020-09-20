#!/usr/bin/env python
# coding: utf-8

# In[1]:


import MasaResorte
import numpy as np
import matplotlib.pyplot as plt


# In[2]:



omega=[5,4,3,2,1] #5 diferentes frecuencias para solucionar la ecuación

gamma=[4,3,2,1,0.5] #5 diferentes constantes de amortiguamiento para solucionar la ecuación

y_0=[0,1,2,3,4] #Condiciones iniciales para la posición

v_0=[1,0,1,0,1] #Condiciones iniciales para la velocidad

n=20 # Tiempo final para la Integración de las ecuaciones

color=['--r','--b','--g','--k','--y']

ecuacion=['$y´´+25y=0$','$y´´+16y=0$','$y´´+9y=0$','$y´´+4y=0$','$y´´+y=0$']

plt.figure(figsize=(15,10))  

for i in range(0,5):
    
    a=MasaResorte.Oscilador(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_pos(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$y(m)$',size=15)
    
plt.title("Solución de la posición oscilador armonico",size=20) 


# En este gráfico se evidencia lo que ya se conoce respecto a un oscilador armonico, independientemente de su frecuencia o condiciones iniciales, la posición de este realiza un movimiento periodico con amplitud constante en el tiempo.

# In[3]:


#Velocidad vs tiempo

plt.figure(figsize=(15,10))  

for i in range(0,5):
    a=MasaResorte.Oscilador(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_vel(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$y(m)$',size=15)
    
    plt.ylabel('$V(m/s)$',size=15)
    
plt.title("Espacio de fase del oscilador armonico ",size=20) 


# Este gráfico muestra que para los diferentes parametros, el espacio de fase de un osciladores armonico es una elipse, cuyos eje menor y mayor dependen de los parametros iniciales dados al oscilador armonico. Por otro lado, que las trayectorias en el espacio de fase sean cerradas evidencia lo que ya se dijo en la anterior gráfica, el movimiento es periodico.

# In[8]:


#Oscilador amortiguado (caso de subamortiguamiento)

plt.figure(figsize=(15,10))  

n=10 # Integración de las ecuaciones.

ecuacion=['$y´´+2*4y´+25y=0$','$y´´+2*3y´+16y=0$','$y´´+2*2y´+9y=0$','$y´´+2*1y´+4y=0$','$y´´+2*0.5y´+y=0$']

for i in range(0,5):
    a=MasaResorte.OsciladorAmortiguado(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_posA(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$y(m)$',size=15)
    
plt.title("Solución de la posición oscilador amortiguado",size=20)


# A diferencia del oscilador armonico, el factor de amortiguamiento ($\Gamma$) hace que oscilador se detenga (o 'pierda' la suficiente energía como para no evidenciar un momiento apreciable). De la solución para los 5 conjuntos de parametros los graficos muestran, que dependiendo de $\Gamma$ la amortiguación es mayor o menor, esto es la amplitud del oscilador decrece más rapido en el tiempo.

# In[9]:


#Oscilador amortiguado (caso de subamortiguamiento)

plt.figure(figsize=(15,10))  

n=20 # Integración de las ecuaciones

for i in range(0,5):
    a=MasaResorte.OsciladorAmortiguado(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_velA(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$y(m)$',size=15)
    
    plt.ylabel('$V(m/s)$',size=15)
    
plt.title("Espacio de fase del oscilador amortiguado",size=20)


# Como se discutio antes, el oscilador amortiguado tiene la caracteristica, de que su amplitud decrezca en el tiempo, en este gráfico del espacio de fase las trayectorias para los diferentes parametros tienden todas a un mismo punto, esto  es el reposo, por eso todas tienden a $V=0$.

# In[ ]:




