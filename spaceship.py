class Spaceship:
    model = 'hat'
    passengers = []

    def __init__(self, name : str = 'default'):
        self.name = name
        #self.passengers = []

    def __str__(self):
        return f'{self.name} ({self.model}): {self.passengers}'
    
if __name__ == '__main__':
    x = Spaceship('x')
    x.model = 'x'
    x.passengers.append('p1')
    print(x)

    y = Spaceship('y')
    x.passengers.append('p2')
    y.model = 'y'
    print(y)
    z = Spaceship('z')
    print(z)
    print(y)
    print(x)
    x.passengers = []

    x.passengers.remove('p1')
    x.passengers.remove('p2')

    print(z)
    print(y)
    print(x)
