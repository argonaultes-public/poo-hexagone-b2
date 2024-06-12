from abc import ABC, abstractmethod
from fly import FlyBehavior, FlyNone, FlyInSpace
from quack import QuackBehavior, QuackMuet, QuackTresFort

class Duck(ABC):

    def __init__(self, color, flybehavior : FlyBehavior = FlyNone(), quackbehavior : QuackBehavior = QuackMuet()):
        self.__color = color
        self.__flybehavior = flybehavior
        self.__quackbehavior = quackbehavior

    @property
    def color(self):
        return self.__color

    def fly(self):
        self.__flybehavior.fly()

    def quack(self):
        self.__quackbehavior.quack()

    @property
    def flybehavior(self):
        return self.__flybehavior

    @flybehavior.setter
    def flybehavior(self, value : FlyBehavior):
        self.__flybehavior = value

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
    donald.quack()
    picsou = CanardBleu()
    print(picsou.display())
    picsou.fly()
    # set FlyInSpace to picsou
    picsou.flybehavior = FlyInSpace()
    picsou.quack()
    # try to fly again and check picsou is flying in space
    picsou.fly()

