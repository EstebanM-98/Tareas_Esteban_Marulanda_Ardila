#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

import math as m

class VectorCartesiano: 
    
    def __init__(self, x0=0,y0=0,z0=0): #Constructor
        self.x=float(x0) #Atributo tipo float en x
        self.y=float(y0) #Atributo tipo float en y 
        self.z=float(z0) #Atributo tipo float en z
        
        self.vector=[self.x,self.y,self.z]
        self.magnitud= (self.x**2+self.y**2+self.z**2)**0.5 #Atributo magnitud
    
    def __add__(self, other) :  #Método suma
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self,other): #Método resta        
        '''Sobrecarga del operador resta'''
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):  #Producto interno
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    def __getitem__(self,index) : #Método []
        return self.vector[index]
    
    def __eq__(self, other): #Método ==
        return  (self.x==other.x and self.y==other.y  and self.z==other.z)
    
    
    def Cruz(self,other): #Producto cruz
        return VectorCartesiano(self.y*other.z-self.z*other.y,self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)
    
    
    def cart_sph(self):
        
        self.r_=(self.x**2 + self.y**2+ self.z**2)**0.5
        self.theta=np.arccos(self.z/self.r_) 
        self.phi=m.atan2(self.y,self.x)
      
                                
        print (f"[{self.r_ }, {self.theta} , {self.phi}]")
    
    
    def Print(self):
        '''Imprime el vector'''
        print(f"[{self.x},{self.y},{self.z}]")
        

class VectorPolar(VectorCartesiano):
    
    def __init__(self,r,theta,phi):
        
        if r<0 or  theta>np.pi or theta<0 or phi>np.pi*2 or phi<0: print('ingrese un valor adecuado ')
        else:
            self.r=float(r) #Atributo tipo float en x
            self.theta=float(theta) #Atributo tipo float en y 
            self.phi=float(phi) #Atributo tipo float en z
            x_=self.r*np.sin(self.theta)*np.cos(self.phi)
            y_=self.r*np.sin(self.theta)*np.sin(self.phi)
            z_=self.r*np.cos(self.theta)
            VectorCartesiano.__init__(self,x_,y_,z_)
            

            #Hereda VectorCartesiano
    
        
        
            

        

    

