def Factorial(n):
    if n!=int(n):
        print('Ingrese un entero')
    else:
        s=1
        for i in range(2,n+1):
            s=s*i
        return s
      
def Binomial(n,k):
    return (Factorial(n))/(Factorial(k)*Factorial(n-k))
  
def Pascal(n):
    for i in range(0,n+1):
        n=[]
        n.append(i)
        for j in range(0,i+1):
            
            n.append(Binomial(i,j))
        
        print(*n, sep=" ")
        
def Pascal(n):
    
    open("Pasca-n.txt", "w") #Sobreescribe sobre el archivo ya creado
    
    #Este documento de texto se crea en la misma carpeta donde esta el codigo
    #Esta primera linea con el fin de que cuando se vuelva a utilizar la función generar un nuevo triangulo de pascal
    #y borrar el anterior
    
    s=n #Variable que permitira hacer los espacios a la hora de escribir el triangulo en el archivo.txt
    
    for i in range(0,n+1):
        l=[]
        
        for k in range(0,s+1):

            with open('Pascal-n.txt', 'a') as f:
                f.write(' ') 
    
        for j in range(0,i+1):
            
           
            with open('Pascal-n.txt', 'a') as f:
                f.write(str(Binomial(i,j))) 
           
            with open('Pascal-n.txt', 'a') as f:
                f.write(' ') 
        
        with open('Pascal-n.txt', 'a') as f:
            f.write('\n') 
            
        s=n-(i+1)
