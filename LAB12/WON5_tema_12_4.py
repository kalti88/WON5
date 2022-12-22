import geometry

x = float(input('Inrodu valoarea coordonatei x al centrul cercului!'))
y = float(input('Inrodu valoarea coordonatei y al centrul cercului!'))
raza = float(input('Inrodu valoarea razei cercului!'))

C = geometry.Circle(x, y, raza)

print('Aria cercului este {}'.format(f'{C.get_area():,.2f}'))
print('Distanta cercului de la centru este {}'.format(C.get_distance()))

