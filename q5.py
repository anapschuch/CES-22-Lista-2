# Objetivo: adicionar o método reflect_x à classe Point
# que retorna um novo Point, que é a reflexão em relação
# ao eixo x do ponto original


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin"""
        self.x = x
        self.y = y

    def reflect_x(self):
        """ Returns a new point, which is the reflection of
        the point about the x-axis"""
        return Point(self.x, -self.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


new_point = Point(3, 5).reflect_x()

print(new_point)
