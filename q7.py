# Objetivo: criar o método get_line_to(Point) na classe Point
# que retorna o coeficiente da reta que liga os dois pontos.


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin"""
        self.x = x
        self.y = y

    def get_line_to(self, second_point):
        """ Returns the coefficients of
        the line joining the two points """
        a = (second_point.y - self.y)/(second_point.x - self.x)
        b = self.y - a*self.x
        return (a,b)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


print(Point(4, 11).get_line_to(Point(6, 15)))
print(Point(2, 2).get_line_to(Point(0, 0)))
