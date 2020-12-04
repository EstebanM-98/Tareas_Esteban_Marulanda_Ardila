#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Librerias

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scl
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

#Clase

class WaveFunction:
    
    def __init__(self,f,x,m): #Constructor
        
        self.domin=x  #Dominio
        self.m=m #Masa
        self.potential=f(x) #Potencial
        self.hbar=1. #Constante de Planck
        self.h = self.domin[1]-self.domin[0] #Paso, se pone de tal forma que cubra todo el intervalo
        self.SD = 1./(self.h**2)*(np.diag(np.ones(len(self.domin)-1),-1) -2* np.diag(np.ones(len(self.domin)),0) + np.diag(np.ones(len(self.domin)-1),1)) #Matriz de segunda derivada
        self.H = -(self.hbar**2)/(2.0*m)*self.SD + np.diag(self.potential)  #Hamiltoniano
        self.E, self.psiS = np.linalg.eigh(self.H)  #Solución autovalores y autovectores
        self.psi = np.transpose(self.psiS)  #Transpone la linea anterior
        
    
    def Energy(self,n): #Autovalores
        E=[]
        for i in range(n):
            E.append(self.E[i])
            
        return np.array(E) #Devuelve los primeros n autovalores
    
    def solution(self,n,b): # Grafica las primeras n autofunciones
        
        N=len(self.domin)
        
        # Crea grafico 
        
        plt.figure(figsize=(10,7))
        
        plt.xlim(-b,b)
        
        plt.xlabel('$x$',fontsize=15)
        
        plt.ylabel('$\psi_{n}(x)$',fontsize=15)
    
        for i in range(n):
            if self.E[i]>0:                 
                if self.psi[i][int(N/2)] < 0: #Esta condición multiplica por menos a las soluciones que estan invertidas respecto a las analiticas,
                #Esto puede pasar debido a que linalg retorna los autovectores con signo arbitrario
                
                    plt.plot(self.domin,-self.psi[i]/np.sqrt(self.h),label="$E_{}$={:>8.3f}".format(i,self.E[i]))
                    
                else:
                    plt.plot(self.domin,self.psi[i]/np.sqrt(self.h),label="$E_{}$={:>8.3f}".format(i,self.E[i]))
    
    def Density(self,n,b): #Devuelve un gráfico con las primeras n densidades de probabilidad
        
        N=len(self.domin)
        
        # Crea grafico 
            
        plt.figure(figsize=(10,7))
        
        plt.xlim(-b,b)
        
        plt.xlabel('$x$',fontsize=15)
        
        plt.ylabel('$|\psi(x)_{n}|^{2}$',fontsize=15)
        
        for i in range(n):
            if self.E[i]>0:                 
                  plt.plot(self.domin,abs(self.psi[i]/np.sqrt(self.h))**2,label="$E_{}$={:>8.3f}".format(i,self.E[i]))
                    
    
    def Density_CT(self,t,b): #Recibe tiempo e intervalo de graficaciónl, para graficar la combinación lineal pedida
        y=0

        for j in range(0,4):
            y+=self.psi[j]*np.exp(-1j*self.E[j]*t)
            
        plt.figure(figsize=(10,7))
            
        plt.xlim(-b,b)
        
        plt.title('Modulo cuadrado de combinación lineal de funciones de onda',fontsize=16)
        
        plt.xlabel('$x$')
        
        plt.ylabel('$|\psi(x,t_{0})|^{2}$')
        
        plt.plot(self.domin,0.5*abs(y)**2,label='$|\sum_{i=1}^{4}c_{n}\psi_{n}(x,t_{0})e^{-iE_{n}t_{0}/ \hbar}|^{2}$')
        
        plt.legend()

    def Combinacion_Ani(self,b,a): #Animación de la parte real de la combinación lineal.
        
        # Crea grafico 
        
        fig = plt.figure()
        
        ax = plt.axes(xlim=(-b, b), ylim=(-a, a))
        
        plt.title('Evolución temporal de la función de onda para el oscilador armonico')
        
        plt.xlabel('$x$')
        
        plt.ylabel('$\Psi(x,t)$')
        

        
        line, = ax.plot([], [], lw=3)

        def init():
            line.set_data([], [])
            return line,
        def animate(i):
            y=0
            for j in range(0,4):
                y+=self.psi[j]*np.cos(self.E[j]*i)
                
            line.set_data(self.domin, 0.5*y)
            line.set_label('$\sum_{i=1}^{4}c_{n}\psi_{n}(x,t_{0})e^{-iE_{n}t_{0}/ \hbar}$')
            ax.legend()

            return line,

        anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=40, blit=True)
        #Guarda gif

        anim.save('Combinacion_Ani3.gif', writer='imagemagick')
    
    
    
    def Density_CTAni(self,b,a):
        
        #Crea grafico
        fig = plt.figure()
        ax = plt.axes(xlim=(-b, b), ylim=(-a, a))
        line, = ax.plot([], [], lw=3)
        
        plt.title('Evolución temporal de la densidad de probabilidad para el oscilador armonico')
        
        plt.xlabel('$x$')
        
        plt.ylabel('$|\Psi(x,t)|^{2}$')

        def init():
            line.set_data([], [])
            return line,
        def animate(i):
            y=0
            for j in range(0,4):
                y+=self.psi[j]*np.exp(-1j*self.E[j]*i)
                line.set_data(self.domin, 0.5*abs(y)**2)
                
            line.set_data(self.domin, 0.5*y)
            
            line.set_label('$|\sum_{i=1}^{4}c_{n}\psi_{n}(x,t_{0})e^{-iE_{n}t_{0}/ \hbar}|^{2}$')
            
            ax.legend()    
                
            return line,

        anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=40, blit=True)

        #Crea gif

        anim.save('Density_CTAni3.gif', writer='imagemagick')

        
        

        
        
        
    
        
        


# In[ ]:




