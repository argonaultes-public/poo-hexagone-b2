from abc import ABC, abstractmethod
from fly import FlyBehavior, FlyNone, FlyInSpace

class Duck(ABC):

    def __init__(self, color, flybehavior : FlyBehavior = FlyNone()):
        self.__color = color
        self.__flybehavior = flybehavior

    @property
    def color(self):
        return self.__color

    def fly(self):
        self.__flybehavior.fly()

    def quack(self):
        pass

    @abstractmethod
    def display(self):
        pass

class MallardDuck(Duck):

    def __init__(self):
        super().__init__('red', flybehavior=FlyInSpace())
    
    def display(self) -> str:
        return f'### {self.__class__.__name__} is {self.color}'


class CanardBleu(Duck):

    def __init__(self):
        super().__init__('blue')

    def display(self) -> str:
        return f'*** {self.__class__.__name__} is {self.color}'



if __name__ == '__main__':
    donald = MallardDuck()
    print(donald.display())
    donald.fly()
    picsou = CanardBleu()
    print(picsou.display())
    picsou.fly()
    # set FlyInSpace to picsou
    # try to fly again and check picsou is flying in space

