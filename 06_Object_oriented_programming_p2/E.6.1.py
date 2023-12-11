class Car():

    def __init__(self, year, model, fuel_type):
        self.year = year
        self.model = model
        self.fuel_type = fuel_type


    def go(self):
        print('Going')

    def stop(self):
        print('Stopped')

    def refuel(self):
        print('Fuel tank is full')


class ElectricCar(Car):

    def refuel(self):
        print('Battery is charged')

    def self_drive(self):
        print('Self-driving')


volvo = Car(2000, 'V50', 'diesel')
volvo.go()
volvo.stop()
volvo.refuel()

tesla = ElectricCar(2020, 'S', 'electric')
tesla.go()
tesla.stop()
tesla.refuel()
tesla.self_drive()

