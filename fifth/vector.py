class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if type(other) == int:
            return Vector(self.x * other, self.y * other)
        else:
            exit('ValueError')

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** (1 / 2))

    def __str__(self):
        return '({}; {})'.format(self.x, self.y)


v1 = Vector(-2, 5)
v2 = Vector(0, 0)
v_sum = v1 + v2
print(len(v_sum))
