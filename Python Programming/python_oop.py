class House:
    '''
    This is a stub for a class representing a House in oop
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self, rate):
        print(self.num_rooms)
        cost = rate * self.num_rooms
        return cost


house = House()
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)
