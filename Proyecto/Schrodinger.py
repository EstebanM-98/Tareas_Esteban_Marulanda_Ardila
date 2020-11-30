#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scl
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

#Clase

class WaveFunction:
    
    def __init__(self,f,x,m,hbar): #Constructor
        
        self.domin=x
        self.m=m
        self.potential=f(x)
        self.hbar=hbar
        self.h = self.domin[1]-self.domin[0] )
        self.Mdd = 1./(self.h*self.h)*(np.diag(np.ones(len(self.domin)-1),-1) -2* np.diag(np.ones(len(self.domin)),0) + np.diag(np.ones(len(self.domin)-1),1))
        self.H = -(hbar*hbar)/(2.0*m)*self.Mdd + np.diag(self.potential) 
        self.E, self.psiT = np.linalg.eigh(self.H) 
        self.psi = np.transpose(self.psiT)   
        
    def plot(self): #Grafico del potencial
        return plt.plot(self.domin,self.potential)
    
    def Energy(self,n): #Autovalores
        E=[]
        for i in range(n):
            E.append(self.E[i])
            
        return np.array(E) #Devuelve los primeros n autovalores
    
    def solution(self,n,b): #Primeras n autofunciones
        N=len(self.domin)
        plt.figure(figsize=(10,7))
        plt.xlim(-b,b)
        plt.xlabel('$x$',fontsize=15)
        plt.ylabel('$\psi_{n}(x)$',fontsize=15)
    
        for i in range(n):
            if self.E[i]>0:                 # Only plot the bound states. The scattering states are not reliably computed.
                if self.psi[i][int(N/2)] < 0:   # Flip the wavefunctions if it is negative at large x, so plots are more consistent.
                    plt.plot(self.domin,-self.psi[i]/np.sqrt(self.h),label="$E_{}$={:>8.3f}".format(i,self.E[i]))
                else:
                    plt.plot(self.domin,self.psi[i]/np.sqrt(self.h),label="$E_{}$={:>8.3f}".format(i,self.E[i]))
    
    def Density(self,n,b): #Devuelve un gráfico con las primeras n densidades de probabilidad
        N=len(self.domin)
        plt.figure(figsize=(10,7))
        plt.xlim(-b,b)
        plt.xlabel('$x$',fontsize=15)
        plt.ylabel('$|\psi(x)_{n}|^{2}$',fontsize=15)
        for i in range(n):
            if self.E[i]>0:                 
                  plt.plot(self.domin,abs(self.psi[i]/np.sqrt(self.h))**2,label="$E_{}$={:>8.3f}".format(i,self.E[i]))
                    
    
    def Density_CT(self,t,b): #Recibe tiempo e intervalo de graficación
        y=0

        for j in range(0,4):
            y+=self.psi[j]*np.exp(-1j*self.E[j]*t)
        plt.xlim(-b,b)
        plt.title('Modulo cuadrado de combinación lineal de funciones de onda')
        plt.xlabel('$x$')
        plt.ylabel('$|\psi(x,t_{0})|$')
        plt.plot(self.domin,0.5*abs(y)**2,label='$|\sum_{i=1}^{4}c_{n}\psi_{n}(x,t_{0})e^{-iE_{n}t_{0}/ \hbar}|^{2}$')
        plt.legend()

    def Combinacion_Ani(self,b,a): #Animación de la parte real de la combinación lineal.
        
        fig = plt.figure()
        ax = plt.axes(xlim=(-b, b), ylim=(-a, a))
        line, = ax.plot([], [], lw=3)

        def init():
            line.set_data([], [])
            return line,
        def animate(i):
            y=0
            for j in range(0,4):
                y+=self.psi[j]*np.cos(self.E[j]*i)
            line.set_data(self.domin, 0.5*y)
            return line,

        anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=40, blit=True)


        anim.save('Combinación_Ani.gif', writer='imagemagick')
    
    
    
    def Density_CTAni(self,b,a):
        
        fig = plt.figure()
        ax = plt.axes(xlim=(-b, b), ylim=(-a, a))
        line, = ax.plot([], [], lw=3)

        def init():
            line.set_data([], [])
            return line,
        def animate(i):
            y=0
            for j in range(0,4):
                y+=self.psi[j]*np.exp(-1j*self.E[j]*i)
                line.set_data(self.domin, 0.5*abs(y)**2)
            return line,

        anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=40, blit=True)


        anim.save('Density_CTAni.gif', writer='imagemagick')

        
        

        
        
        
    
        
        


# In[ ]:




