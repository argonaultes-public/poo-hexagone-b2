class Quackologist:

    def __init__(self, name):
        self.__name = name
        self.__counter = 0

    def update(self):
        self.__counter += 1

    @property
    def counter(self):
        return self.__counter

    def __repr__(self):
        return f'{self.__name}: {self.__counter}'

