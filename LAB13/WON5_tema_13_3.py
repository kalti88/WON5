from geometry import Point, Rectangle

x1 = float(input('Inrodu valoarea coordonatei x pentru punctul A!'))
y1 = float(input('Inrodu valoarea coordonatei y pentru punctul A!'))
x2 = float(input('Inrodu valoarea coordonatei x pentru punctul B!'))
while x2 == x1:
    x2 = float(input(f'Valoarea coordonatei x pentru punctul B trebuie sa fie diferita de {x1}. Alege alt numar!'))
y2 = float(input('Inrodu valoarea coordonatei y pentru punctul B!'))
while y2 == y1:
    y2 = float(input(f'Valoarea coordonatei x pentru punctul B trebuie sa fie diferita de {y1}. Alege alt numar!'))

print('Punctul pentru a verifica daca e sau nu in interiorul dreptunghiului:')
x = float(input('Inrodu valoarea coordonatei x!'))
y = float(input('Inrodu valoarea coordonatei y!'))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

p = Point(x, y)

R = Rectangle(p1, p2)

print(R.check_point_in_rectangle(p))

