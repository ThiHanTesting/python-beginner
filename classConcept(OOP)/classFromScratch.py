class Car : 
    def __init__(self,name='lol',wheels='4') : 
        self.name = name
        self.wheels = wheels
    
    def drive(self) : 
        print(f'{self.name} with {self.wheels} is driving')

Lambo = Car('Toyota',6)
print(Lambo.name)
Lambo.drive()

marcedes = Car('Marcedes',6)
marcedes.drive()