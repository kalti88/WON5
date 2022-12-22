class Point:

    def __init__(self, x: float, y: float):
        """Constructor of points"""
        self.x = x
        self.y = y

    def get_distance(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return distance


class Circle(Point):

    def __init__(self, x, y, raza: float):
        super().__init__(x, y)
        self.raza = raza

    def get_area(self):
        import math
        area = (self.raza ** 2) * math.pi
        return area

    def get_distance(self):
        distance = abs(super().get_distance() - self.raza)
        return distance

