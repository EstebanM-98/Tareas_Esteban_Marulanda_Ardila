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
        
        return plt.plot(self.t,self.vel,color,label=ecuacion)

    
    def plot_posA(self,color,ecuacion):
        
        return plt.plot(self.t,self.posA,color,label=ecuacion)
    
    def plot_velA(self,color,ecuacion):
        
        return plt.plot(self.t,self.velA,color,label=ecuacion) 
    

class OsciladorAmortiguado(Oscilador):
    def __init__(self,omega,gamma,y_0,v_0,t_final):
        Oscilador.__init__(self,omega,gamma,y_0,v_0,t_final)
    
