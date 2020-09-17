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

print('el vector a en esfericas  es:')
a.cart_sph().Print()
print('el vector b en esfericas es:')
b.cart_sph().Print()
print('el vector c en esfericas es:')
c.cart_sph().Print()


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





# In[20]:


#Verificación del atributo heredado magnitud

vector_esfericas=vector.VectorPolar(1,np.pi/2,np.pi/2) #Vector en cartesianas (0,1,0) cuya magnitud es 1
vector_esfericas1=vector.VectorPolar(1,np.pi,0) #Vector en cartesianas (0,0,-1)
vector_esfericas.magnitud #Verificación


# In[15]:


#Verificación métodos
#Metodo []
vector_esfericas1[2]


# In[16]:


#Método ==
vector_esfericas1==vector_esfericas


# In[21]:


#Método Print()
vector_esfericas.Print()


# In[22]:


#Metodo producto escalar 

vector_esfericas1*vector_esfericas


# In[ ]:





# In[ ]:





