from ..duck.duck import MallardDuck, Duck
from ..goose.goose import Goose, GooseAsDuck

class DuckSimulator:

    def __init__(self):
        self.__ducks = []

    def enroll_duck(self, duck : Duck):
        if isinstance(duck, Duck):
            self.__ducks.append(duck)
        else:
            raise TypeError('virus detected')

    def simulate(self):
        for duck in self.__ducks:
            for _ in range(2):
                duck.fly()
            duck.quack()
            for _ in range(3):
                duck.fly()


if __name__ == '__main__':
    sim = DuckSimulator()
    sim.enroll_duck(MallardDuck())
    sim.enroll_duck(GooseAsDuck(Goose()))
    sim.simulate()