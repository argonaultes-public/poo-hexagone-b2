from abc import ABC, abstractmethod

class QuackBehavior(ABC):

    @abstractmethod
    def quack(self):
        pass

class QuackTresFort(QuackBehavior):

    def quack(self):
        print('Quack tres fort')

class QuackMuet(QuackBehavior):

    def quack(self):
        print('Quack muet')

