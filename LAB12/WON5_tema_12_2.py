import geometry

x = float(input('Inrodu valoarea coordonatei x!'))
y = float(input('Inrodu valoarea coordonatei y!'))

p1 = geometry.Point(x, y)

print('Distanta de la punct la origine {}'.format(f'{p1.get_distance():,.2f}'))
