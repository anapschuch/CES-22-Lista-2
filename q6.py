# Objetivo: adicionar o método slope_from_origin na classe  Point
# que retorna a inclinação da reta que liga a origem com o ponto.


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin"""
        self.x = x
        self.y = y

    def slope_from_origin(self):
        """ Returns the slope of the line joining
        the origin to the point"""
        if self.x != 0:
            return self.y / self.x
        else:
            print("Error")

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


print(Point(4, 10).slope_from_origin())

# O método falha quando a coordenada x do ponto é nula
