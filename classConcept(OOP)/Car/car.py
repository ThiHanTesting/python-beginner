class Car : 
    sterringWheel = 1   #class level attribute
    def __init__(self,name='lol',wheels='4') : 
        self.name = name
        self.wheels = wheels
    
    def drive(self) : 
        print(f'{self.name} with {self.wheels} is driving')

    @classmethod
    def common(cls) : 
        print(f'all car is only {cls.sterringWheel} sterring wheel .')


# Lambo = Car('Toyota',6)
# print(Lambo.name)
# Lambo.drive()

# marcedes = Car('Marcedes',6)
# marcedes.drive()

# class level attribute and method
# print(Car.sterringWheel)
# Car.common()

# Lamborr = Car()
# Lamborr.common()
