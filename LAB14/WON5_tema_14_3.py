from geometry import Point, Polyline

list_points = []
x = float(input('Inrodu valoarea coordonatei x pentru primul punct!'))
y = float(input('Inrodu valoarea coordonatei y pentru primul punct!'))
list_points.append(Point(x, y))
ctrl = 'y'
while ctrl == 'y' or ctrl == 'Y':
    x = float(input('Inrodu valoarea coordonatei x pentru urmatorul punct!'))
    y = float(input('Inrodu valoarea coordonatei y pentru urmatorul punct!'))
    list_points.append(Point(x, y))
    ctrl = input('Vrei sa continui? y/n')


print(Polyline(*list_points))
