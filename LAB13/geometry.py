class Point:

    def __init__(self, x: float, y: float):
        """
        Constructor of points
        :param x: x-axis coordinate
        :type x: float
        :param y: y-axis coordinate
        :type y: float

        :return: object
        """
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, p1, p2):
        """
        Define a rectangle
        :param p1: First construction point
        :type p1: Point
        :param p2: Second construction point
        :type p2: Point

        :return: object
        """
        self.p1 = p1
        self.p2 = p2

    def length_of_sides(self):
        """
        Calculate the lengths of sides
        :returns:
            lx - the length of side on x axes
            ly - the length of side on y axes
        """
        lx = abs(self.p1.x - self.p2.x)
        ly = abs(self.p1.y - self.p2.y)
        return lx, ly

    def rectangle_area(self):
        """
        Calculate the area of a rectangle.
        :return: The area
        """
        area = abs((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))
        return area

    def rectangle_perimeter(self):
        """
        Calculate the perimeter of a rectangle.
        :return: The perimeter
        """
        prm = abs((self.p1.x - self.p2.x) + (self.p1.y - self.p2.y)) * 2
        return prm
