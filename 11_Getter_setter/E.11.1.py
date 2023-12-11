# Parašyti klasę "Namas", kuri turėtų savybę "plotas" ir "verte".
# Padaryti taip, kad savybė "verte" koreguojama tik įvedus skaičių.
# Programoje naudoti dekoratorių @property.

class Home:
    def __init__(self, area, value):
        self.area = area
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            print('Value must be positive!')
        else:
            self.__value = new_value

    def __str__(self):
        return f'Area: {self.area} \nValue: {self.__value}'


cabin = Home('20m^2', 30)
print(cabin)
cabin.value = 666
print(cabin)
