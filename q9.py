# O objetivo dessa questão é conhecer a order de hierarquia
# em python. Para isso, avaliaremos os MROs. As classes foram
# utilizadas do exemplo de polígonos regulares.


class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:

    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))


class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** 0.5 * self.side ** 2)


class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side


class A(RegularHexagon):
    pass


class B(Square, RegularHexagon):
    pass


class C(RegularHexagon, Square):
    pass


class D(RegularHexagon, Plotter):
    pass


class E(RegularPolygon, Shape):
    pass

a = A(10)
print("\nClass A: \n", a.__class__.__mro__)

b = B(10)
print("\nClass B: \n", b.__class__.__mro__)

c = C(10)
print("\nClass C: \n", c.__class__.__mro__)

d = D(10)
print("\nClass D: \n", d.__class__.__mro__)

e = E(10)
print("\nClass E: \n", e.__class__.__mro__)