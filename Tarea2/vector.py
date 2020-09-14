class VectorCartesiano: 
    
    def __init__(self, x0=0,y0=0,z0=0):
        self.x=float(x0)
        self.y=float(y0)
        self.z=float(z0)
        self.vector=[self.x,self.y,self.z]
        self.magnitud= (self.x**2+self.y**2+self.z**2)**0.5
    
    def __add__(self, other) : 
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self,other):        
        '''Sobrecarga del operador resta'''
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    def __getitem__(self,index) :
        return self.vector[index]
    
    def __eq__(self, other):
        return  (self.x==other.x and self.y==other.y  and self.z==other.z)
    
    def Cruz(self,other):
        return VectorCartesiano(self.y*other.z-self.z*other.y,self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)
    
    def Print(self):
        '''Imprime el vector'''
        print(f"[{self.x},{self.y},{self.z}]")
        
    
# class VectorPolar(VectorCartesiano):
