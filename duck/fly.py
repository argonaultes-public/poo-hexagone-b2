from abc import ABC, abstractmethod

class FlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        pass

class FlyInSpace(FlyBehavior):

    def fly(self):
        print('fly in space')


class FlyNone(FlyBehavior):

    def fly(self):
        print('unable to fly')