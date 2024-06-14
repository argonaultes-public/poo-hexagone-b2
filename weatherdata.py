from random import randrange, randint
from abc import abstractmethod, ABC

class Display:
    
    @abstractmethod
    def update_display(self, temperature, pressure, humidity):
        pass

class Observer(ABC):
    
    @abstractmethod
    def notify(self, subject):
        pass

class Subject:
    def __init__(self):
        self.__observers = []

    def register_observer(self, observer : Observer):
        self.__observers.append(observer)

    def unregister_observer(self, observercls):
        self.__observers = [observer for observer in self.__observers if not isinstance(observer, observercls)]

    def notifiy_observers(self):
        for observer in self.__observers:
            observer.notify(self)

class DisplayTemp(Display, Observer):
    def update_display(self, temperature, pressure, humidity):
        print(f'temperature: {temperature}')

    def notify(self, subject):
        print(f'temperature: {subject.temperature}')

class DisplayPressure(Display, Observer):
    def update_display(self, temperature, pressure, humidity):
        print(f'pressure: {pressure}')

    def notify(self, subject):
        print(f'pressure: {subject.pressure}')

class DisplayHumidity(Display, Observer):
    def update_display(self, temperature, pressure, humidity):
        print(f'humidity: {humidity}')

    def notify(self, subject):
        print(f'humidity: {subject.humidity}')

class DisplayLolCat(Display, Observer):
    def update_display(self, temperature, pressure, humidity):
        print(f'Lol Cat: {temperature} vs {pressure}')

    def notify(self, subject):
        print(f'lol cat: {subject.pressure} vs {subject.temperature}')


class WeatherData(Subject):

    def __init__(self):
        super().__init__()
        self.register_observer(DisplayHumidity())
        self.register_observer(DisplayPressure())
        self.register_observer(DisplayTemp())
        self.__temperature, self.__pressure, self.__humidity = 0, 0, 0


    @property
    def temperature(self):
        return self.__temperature

    @property
    def pressure(self):
        return self.__pressure

    @property
    def humidity(self):
        return self.__humidity

    def __get_temperature(self):
        return randrange(-20, 50)

    def __get_pressure(self):
        return randint(800, 1100)

    def __get_humidity(self):
        return randrange(0, 100)

    def measurements_changed(self):

        # collect measures
        self.__temperature = self.__get_temperature()
        self.__pressure = self.__get_pressure()
        self.__humidity = self.__get_humidity()

        self.notifiy_observers()

if __name__ == '__main__':
    w = WeatherData()
    print('==================')
    w.measurements_changed()
    print('==================')
    w.register_observer(DisplayLolCat())
    w.unregister_observer(DisplayHumidity)
    w.measurements_changed()