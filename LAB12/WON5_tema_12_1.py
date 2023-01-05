class Point:

    def __init__(self, coordonate_x: float, coordonate_y: float):
        """Constructor of points"""
        self.x = coordonate_x
        self.y = coordonate_y

    def get_distance(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return distance


x = float(input('Introdu valoarea coordonatei x!'))
y = float(input('Introdu valoarea coordonatei y!'))

p1 = Point(x, y)

print(f'Distanta de la punct la origine {p1.get_distance():26,.2f}')

