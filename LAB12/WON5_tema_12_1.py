class Point:

    def __init__(self, coordonate_x: float, coordonate_y: float):
        """Constructor of points"""
        self.x = coordonate_x
        self.y = coordonate_y

    def get_distance(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return f'{distance:,.2f}'


x = float(input('Inrodu valoarea coordonatei x!'))
y = float(input('Inrodu valoarea coordonatei y!'))

p1 = Point(x, y)

print('Distanta de la punct la origine {}'.format(p1.get_distance()))

