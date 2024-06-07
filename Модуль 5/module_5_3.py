class Building:
    def __init__(self, number_of_floors, building_type):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors


h1 = Building(1, 'Shop')
h2 = Building(1, 'Shop')
h3 = Building(5, 'House')
print(h1 == h2)
print(h2 == h3)
