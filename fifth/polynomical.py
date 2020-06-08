class Polynomial:
    def __init__(self, values):
        self.values = values.copy()
        self.size = len(values)

    def __add__(self, other):
        new_values = []
        for i in range(max(self.size, other.size)):
            new_values.append(0)
            if self.size > i:
                new_values[i] += self.values[i]
            if other.size > i:
                new_values[i] += other.values[i]
        return Polynomial(new_values)

    def __call__(self, other):
        sum = int()
        for i in range(self.size):
            sum += self.values[i] * (other ** i)
        return sum


a = [1, 2, 3]
print(id(a))
poly = Polynomial(a)
poly2 = Polynomial([10, 4, 5, 2, 4, 6])
a.append(4)
poly1 = poly + poly2
print(poly(0))
print(poly(1))
print(poly(2))
print(id(poly.values), poly.values)



