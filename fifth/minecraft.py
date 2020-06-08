class BaseObject:
    def __init__(self, x, y, z):
        self.coordinates = (x, y, z)

    def get_coordinates(self):
        return self.coordinates


class Block(BaseObject):
    def shatter(self):
        self.coordinates = (None, None, None)


class Entity(BaseObject):
    def move(self, x, y, z):
        self.coordinates = (x, y, z)


class Thing(BaseObject):
    pass


stone = Block(10, 34, 45)
boat = Entity(23, 53, 63)

print(stone.get_coordinates())
print(boat.get_coordinates())
boat.move(26, 23, 63)
print(boat.get_coordinates())