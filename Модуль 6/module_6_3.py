class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def horse_power(self):
        return self.horse_power


class Nissan(Vehicle, Car):
    price = 1500000
    vehicle_type = 'civil_car'
    horse_power = 500


nissan = Nissan()
print('Vehicle stype: ', nissan.vehicle_type)
print('Price: ', nissan.price)
