from random import randrange, randint

class DisplayTemp:

    def display_temp(self, temperature):
        print(f'temperature: {temperature}')

class DisplayPressure:

    def display_pressure(self, pressure):
        print(f'pressure: {pressure}')

class DisplayHumidity:

    def display_humidity(self, humidity):
        print(f'humidity: {humidity}')


class WeatherData:

    def __init__(self):
        self.__display_temp = DisplayTemp()
        self.__display_pressure = DisplayPressure()
        self.__display_humidity = DisplayHumidity()

    def get_temperature(self):
        return randrange(-20, 50)

    def get_pressure(self):
        return randint(800, 1100)

    def get_humidity(self):
        return randrange(0, 100)

    def measurements_changed(self):

        # collect measures
        temperature = self.get_temperature()
        pressure = self.get_pressure()
        humidity = self.get_humidity()

        # trigger display
        self.__display_humidity.display_humidity(humidity)
        self.__display_temp.display_temp(temperature)
        self.__display_pressure.display_pressure(pressure)


if __name__ == '__main__':
    w = WeatherData()
    w.measurements_changed()
    w.measurements_changed()