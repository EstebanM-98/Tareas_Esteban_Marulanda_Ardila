#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# In[128]:


class Oscilador:
    
    def __init__(self,omega,gamma,y_0,v_0,t_final): # Frecuencia w_{0}, factor de amortiguamiento gamma, posición inicial,
        #  velocidad inicial, tiempo final de integración de las ecuaciones.
        
        #Atributos tipo float de los parametros
        
        self.omega=float(omega)**2
        
        self.y_0=float(y_0)
        
        self.v_0=float(v_0)
        
        self.t_final=float(t_final)
        
        self.gamma=2*float(gamma)
        
        self.t=t=np.linspace(0,self.t_final,1000)
        
        
        
        def armonico(y,t):
            return np.array([y[1],-self.omega*y[0]])
            
        #Se debe cumplir que gamma<omega_{0}
        
        def amortiguado(y,t):
            return np.array([y[1],-self.omega*y[0]-self.gamma*y[1]])
        
        sol_armonico=odeint(armonico, np.array([self.y_0,self.v_0]), t)
        
        sol_amortiguado=odeint(amortiguado, np.array([self.y_0,self.v_0]), t)
        
        
        
        self.pos=sol_armonico[:,0]
        self.vel=sol_armonico[:,1]
        
        self.posA=sol_amortiguado[:,0]
        self.velA=sol_amortiguado[:,1]
        
    def plot_pos(self,color,ecuacion):
         
        return plt.plot(self.t,self.pos,color,label=ecuacion)
    
    def plot_vel(self,color,ecuacion):
        
        return plt.plot(self.pos,self.vel,color,label=ecuacion)

    
    def plot_posA(self,color,ecuacion):
        
        return plt.plot(self.t,self.posA,color,label=ecuacion)
    
    def plot_velA(self,color,ecuacion):
        
        return plt.plot(self.posA,self.velA,color,label=ecuacion) 
    

class OsciladorAmortiguado(Oscilador):
    def __init__(self,omega,gamma,y_0,v_0,t_final):
        Oscilador.__init__(self,omega,gamma,y_0,v_0,t_final)
    
    
    
    
    
        


       


# In[129]:


omega=[5,4,3,2,1]

gamma=[4,3,2,1,0.5]

y_0=[0,1,2,3,4]

v_0=[1,0,1,0,1]

n=20 # Integración de las ecuaciones

color=['--r','--b','--g','--k','--y']

ecuacion=['$y´´+25y=0$','$y´´+16y=0$','$y´´+9y=0$','$y´´+4y=0$','$y´´+y=0$']

plt.figure(figsize=(15,10))  

for i in range(0,5):
    a=Oscilador(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_pos(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$y(m)$',size=15)
    
plt.title("Solución de la posición oscilador armonico",size=20) 


# In[130]:


#Velocidad vs tiempo

plt.figure(figsize=(15,10))  

for i in range(0,5):
    a=Oscilador(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_vel(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$V(m/s)$',size=15)
    
plt.title("Solución de la velocidad oscilador armonico",size=20) 


# In[134]:


#Oscilador amortiguado (caso de subamortiguamiento)

plt.figure(figsize=(15,10))  

n=10 # Integración de las ecuaciones

for i in range(0,5):
    a=OsciladorAmortiguado(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_posA(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$y(m)$',size=15)
    
plt.title("Solución de la posición oscilador amortiguado",size=20)


# In[135]:


#Oscilador amortiguado (caso de subamortiguamiento)

plt.figure(figsize=(15,10))  

n=10 # Integración de las ecuaciones

for i in range(0,5):
    a=OsciladorAmortiguado(omega[i],gamma[i],y_0[i],v_0[i],n)
    
    a.plot_velA(color[i],ecuacion[i])
    
    plt.legend()
    
    plt.xlabel('$t(s)$',size=15)
    
    plt.ylabel('$y(m)$',size=15)
    
plt.title("Solución de la posición oscilador amortiguado",size=20)


# In[ ]:





# In[ ]:




