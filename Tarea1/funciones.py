def Factorial(n): #Función que general el factorial de un número n
    if n!=int(n) or n<0:  #Condición para solo aceptar entero positivos
        print('Ingrese un entero')
    else:
        s=1
        for i in range(2,n+1): 
            s=s*i
        return s #Retorna el factorial de n
      
def Binomial(n,k): #Función que calcula la combinatoria entre un número n y uno k 
    return (Factorial(n))/(Factorial(k)*Factorial(n-k))
  

def Pascal(n):
    
    open("Pasca-n.txt", "w") #Sobreescribe sobre el archivo ya creado
    
    #Este documento de texto se crea en la misma carpeta donde esta el codigo
    #Esta primera linea con el fin de que cuando se vuelva a utilizar la función generar un nuevo triangulo de pascal
    #y borrar el anterior
    
    s=n #Variable que permitira hacer los espacios a la hora de escribir el triangulo en el archivo.txt
    
    for i in range(0,n+1):
       
        with open('Pascal-n.txt', 'a') as f: 
            f.write('n='+str(i)) #Añade al documento txt el número de la linea n
        
        for k in range(0,s+1):

            with open('Pascal-n.txt', 'a') as f:
                f.write(' ')  #Añade al documento txt cierta cantidad de espacios antes de introducir los números del triangulo, para que este quede simetrico.
    
        for j in range(0,i+1):
            
           
            with open('Pascal-n.txt', 'a') as f:
                f.write(str(Binomial(i,j))) )  #Añade al documento txt en la linea i el coeficiente j correspondiente a esta
           
            with open('Pascal-n.txt', 'a') as f:
                f.write(' ')  #Añade un espacio entre cada número de cierta linea
        
        with open('Pascal-n.txt', 'a') as f:
            f.write('\n') #Salto de linea en el documento txt
            
        s=n-(i+1) #Condición necesario para añadir espacios antes de comenzar a escribir los coeficientes de las lineas.
