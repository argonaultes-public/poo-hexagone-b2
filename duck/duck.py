from abc import ABC, abstractmethod
from .fly import FlyBehavior, FlyNone, FlyInSpace
from .quack import QuackBehavior, QuackMuet, QuackTresFort

class Duck(ABC):

    def __init__(self, color, flybehavior : FlyBehavior = FlyNone(), quackbehavior : QuackBehavior = QuackMuet(), quacologists = []):
        self.__color = color
        self.__flybehavior = flybehavior
        self.__quackbehavior = quackbehavior
        self.__quackologists = quacologists

    @property
    def quacologists(self):
        return self.__quackologists

    def register_quackologist(self, quackologist):
        self.__quackologists.append(quackologist)

    def notify_quackologists(self):
        for quackologist in self.__quackologists:
            quackologist.update()

    @property
    def color(self):
        return self.__color

    def fly(self):
        self.__flybehavior.fly()

    def quack(self):
        self.notify_quackologists()
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

class CountFlyDuck(Duck):

    def __init__(self, duck : Duck):
        super().__init__(duck.color, quacologists=duck.quacologists)
        self.__duck = duck
        self.__fly_counter = 0

    def fly(self):
        self.__fly_counter += 1
        self.__duck.fly()

    def quack(self):
        self.__duck.quack()
    
    @property
    def counter(self):
        return f'{self.__fly_counter} {self.__duck.counter}'

    def display(self):
        return self.__duck.display()

class CountQuackDuck(Duck):

    def __init__(self, duck : Duck):
        super().__init__(duck.color, quacologists=duck.quacologists)
        self.__duck = duck
        self.__quack_counter = 0

    def quack(self):
        self.__quack_counter += 1
        self.__duck.quack()

    def fly(self):
        self.__duck.fly()
    
    @property
    def counter(self):
        return f'{self.__quack_counter}'

    def display(self):
        return self.__duck.display()

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

