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


class Circle(Point):

    def __init__(self, x, y, raza: float):
        """
        Constructor of Circle
        :param x: x-axis coordinate
        :type x: float
        :param y: y-axis coordinate
        :type y: float
        :param raza: Circle radius value
        :type raza: float

        :return: object
        """
        super().__init__(x, y)
        self.raza = raza


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
        return sorted([lx, ly])

    def rectangle_area(self):
        """
        Calculate the area of a rectangle.
        :return: The area
        :rtype: float
        """
        return abs((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))

    def rectangle_perimeter(self):
        """
        Calculate the perimeter of a rectangle.
        :return: The perimeter
        :rtype: float
        """
        return (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y)) * 2

    def check_point_in_rectangle(self, p):
        """
        Verify if the point is inside the rectangle
        :param p: The point to verify
        :type p: Point
        :return: True or False
        :rtype: Boolean
        """
        minx = min(self.p1.x, self.p2.x)
        maxx = max(self.p1.x, self.p2.x)
        miny = min(self.p1.y, self.p2.y)
        maxy = max(self.p1.y, self.p2.y)

        return minx <= p.x <= maxx and miny <= p.y <= maxy

    def check_circle_in_rectangle(self, c):
        """
        Verify if the circle is inside the rectangle
        :param c: The point to verify
        :type c: Circle
        :return: True or False
        :rtype: Boolean
        """
        minx = min(self.p1.x, self.p2.x)
        maxx = max(self.p1.x, self.p2.x)
        miny = min(self.p1.y, self.p2.y)
        maxy = max(self.p1.y, self.p2.y)

        return minx <= (c.x - c.raza) and (c.x + c.raza) <= maxx and miny <= (c.y - c.raza) and (c.y + c.raza) <= maxy

    def check_element_in_rectangle(self, e):
        """
        Verify if the element is inside the rectangle
        :param e: The point to verify
        :return: True or False
        :rtype: Boolean
        """
        minx = min(self.p1.x, self.p2.x)
        maxx = max(self.p1.x, self.p2.x)
        miny = min(self.p1.y, self.p2.y)
        maxy = max(self.p1.y, self.p2.y)
        if type(e) == Point:
            return minx <= e.x <= maxx and miny <= e.y <= maxy
        elif type(e) == Circle:
            return minx <= (e.x - e.raza) and (e.x + e.raza) <= maxx and miny <= (e.y - e.raza) and (e.y + e.raza) <= maxy

    def __eq__(self, other):
        return self.length_of_sides() == other.length_of_sides()
        # (min(self.length_of_sides()), max(self.length_of_sides())) == (min(other.length_of_sides()), max(other.length_of_sides()))

    def __str__(self):
        return f'Rectangle(Point({self.p1.x}, {self.p1.y}), Point({self.p2.x}, {self.p2.y}))'



