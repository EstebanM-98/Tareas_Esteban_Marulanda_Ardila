import funciones

# En la calculadora aparece que el factorial de 5 es 120
f=120
if funciones.Factorial(5)==f:
  print('True')
else:
  print('False')
    
#En la cálculadora, 20 combinado 15 es 15504
b=15504
if funciones.Binomial(20,15)==b:
  print('True')
else:
  print('False')
    
#La función Pascal(n) se puede testear yendo al documento txt creado y verificando con los coeficientes de n=2 (muy conocido)
funciones.Pascal(2)
