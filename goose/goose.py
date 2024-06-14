
from ..duck.duck import Duck

class Goose:
    
    def goose_is_flying(self):
        print('goose is flying')

    def honk(self):
        print('honk honk!')

# Adapter
class GooseAsDuck(Duck):

    def __init__(self, goose : Goose):
        super().__init__('white', )
        self.__goose = goose

    def fly(self):
        self.__goose.goose_is_flying()
    
    def quack(self):
        self.__goose.honk()

    def display(self):
        return 'a goose is better than a duck'