from geometry import Circle

x = float(input('Inrodu valoarea coordonatei x al centrul cercului!'))
y = float(input('Inrodu valoarea coordonatei y al centrul cercului!'))
raza = float(input('Inrodu valoarea razei cercului!'))

C = Circle(x, y, raza)

print(f'Aria cercului este {C.get_area():,.2f}')
print('Distanta cercului de la centru este {}'.format(C.get_distance()))

