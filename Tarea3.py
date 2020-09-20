#!/usr/bin/env python
# coding: utf-8

# In[2]:


import MasaResorte
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


omega=[5,4,3,2,1]

gamma=[4,3,2,1,0.5]

y_0=[0,1,2,3,4]

v_0=[1,0,1,0,1]

n=20 # Integración de las ecuaciones

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


# In[4]:


#Velocidad vs tiempo

plt.figure(figsize=(15,10))  

for i in range(0,5):
    a=MasaResorte.Oscilador(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_vel(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$V(m/s)$',size=15)
    
plt.title("Solución de la velocidad oscilador armonico",size=20) 


# In[5]:


#Oscilador amortiguado (caso de subamortiguamiento)

plt.figure(figsize=(15,10))  

n=10 # Integración de las ecuaciones

for i in range(0,5):
    a=MasaResorte.OsciladorAmortiguado(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_posA(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$y(m)$',size=15)
    
plt.title("Solución de la posición oscilador amortiguado",size=20)


# In[7]:


#Oscilador amortiguado (caso de subamortiguamiento)

plt.figure(figsize=(15,10))  

n=10 # Integración de las ecuaciones

for i in range(0,5):
    a=MasaResorte.OsciladorAmortiguado(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_velA(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$V(m/s)$',size=15)
    
plt.title("Solución de la velocidad del oscilador amortiguado",size=20)


# In[ ]:




