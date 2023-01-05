from geometry import Point

x1 = float(input('Inrodu valoarea coordonatei x al puntului P1!'))
y1 = float(input('Inrodu valoarea coordonatei y al puntului P1!'))
x2 = float(input('Inrodu valoarea coordonatei x al puntului P2!'))
y2 = float(input('Inrodu valoarea coordonatei y al puntului P2!'))

P1 = Point(x1, y1)
P2 = Point(x2, y2)

if P1.get_distance() == P2.get_distance():
    print('P1 si P2 sunt la aceeasi distanta fata de centru.')
elif P1.get_distance() > P2.get_distance():
    print('P1 este mai departe de centru decat P2')
else:
    print('P2 este mai departe de centru decat P1')

