class Home:
    def __init__(self, area, value):
        self._area = area
        self._value = value

    @property
    def area(self):
        return self._area

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, (int, float)) and new_value > 0:
            self._value = new_value
        else:
            raise ValueError('Must be a positive number')

    def __str__(self):
        return f'Area: {self._area} \nValue: {self._value}'


cabin = Home('20m^2', 30)
print(cabin)
cabin.value = 666
print(cabin)

try:
    cabin.value = 2000
except ValueError as e:
    print(e)