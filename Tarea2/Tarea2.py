#!/usr/bin/env python
# coding: utf-8

# In[1]:


import vector
import numpy as np

import math as m


# In[2]:


a=vector.VectorCartesiano(1.5,0,2.4)
b=vector.VectorCartesiano(0,2,9)
c=vector.VectorCartesiano(4.2,0.05,0)

#Parte 1

print('el vector a en esfericas  es:',a.cart_sph())

print('el vector b en esfericas es:',b.cart_sph())

print('el vector c en esfericas es:',c.cart_sph())


# In[3]:


#Parte 2

print('el producto interno entre a y b es:',a*b)
print('el producto interno entre a y b es:',a*c)
print('el producto interno entre a y b es:',b*c)


# In[4]:


#Parte 3
print("el producto cruz entre a y b es:")
a.Cruz(b).Print()

print("el producto cruz entre a y c es:")
a.Cruz(c).Print()

print("el producto cruz entre b y c es:")
b.Cruz(c).Print()


# In[5]:


#ángulo entre a y b

print('el ángulo entre a y b es:',m.acos((a*b)/(a.magnitud*b.magnitud))*180/np.pi,'°')
print('el ángulo entre a y c es:',m.acos((a*c)/(a.magnitud*c.magnitud))*180/np.pi,'°')
print('el ángulo entre b y c es:',m.acos((b*c)/(b.magnitud*c.magnitud))*180/np.pi,'°')


# In[ ]:





# In[24]:


#Verificación del atributo heredado magnitud

vector_esfericas=vector.VectorPolar(3,np.pi/2,np.pi/2) #Vector en esfericas cuya magnitud debería ser 3, ya que en cartesianas este vector representa (0,3,0)
vector_esfericas1=vector.VectorPolar(2,np.pi/2,0) ##Vector en esfericas cuya magnitud debería ser 4, ya que r=4,ya que en cartesianas este vector representa (2,0,0)
print(vector_esfericas.magnitud) #Verificación
print(vector_esfericas1.magnitud) #Verificación1


# In[25]:


#Verificación métodos
#Metodo []
print('r en coordenas esfericas del primer vector es ,',vector_esfericas[0])

print('theta en coordenas esfericas del primer vector es ,',vector_esfericas[1])

print('phi en coordenas esfericas del primer vector es ,',vector_esfericas[2])


# In[ ]:





# In[26]:


#Método ==
vector_esfericas1==vector_esfericas


# In[27]:


#Método Print()
vector_esfericas.Print()
vector_esfericas1.Print()


# In[28]:


#Metodo producto escalar entre los dos vectores definidos, debería de ser 0

vector_esfericas1*vector_esfericas 


# In[29]:


#Método Suma

print('r,theta y phi de la suma de los dos vectores es respectivamente:',vector_esfericas+vector_esfericas1) #Sobre carga suma, y suma los vectores en cartesianas, por eso el resultado esta en cartesianas


# In[31]:


#Método resta

print('r,theta y phi de la suma de los dos vectores es respectivamente:',vector_esfericas-vector_esfericas1) #Sobre carga suma, y suma los vectores en cartesianas, por eso el resultado esta en cartesianas


# In[32]:


#Método Cruz, debería de dar un vector en theta=pi

print('r,theta y phi del producto cruz entre los dos vectores en esfericas es respectivamente:',vector_esfericas.Cruz(vector_esfericas1))


# In[ ]:




