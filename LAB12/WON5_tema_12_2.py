from geometry import Point

x = float(input('Inrodu valoarea coordonatei x!'))
y = float(input('Inrodu valoarea coordonatei y!'))

p1 = Point(x, y)

print(f'Distanta de la punct la origine {p1.get_distance():,.2f}')
