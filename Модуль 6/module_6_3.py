class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def horse_power(self):
        return self.horse_power


class Nissan(Vehicle, Car):
    price = 1500000
    vehicle_type = 'civil_car'

    def __init__(self, horse_power):
        self.horse_power = horse_power


nissan = Nissan(500)
print('Vehicle type: ', Nissan.vehicle_type)
print('Price: ', Nissan.price)
