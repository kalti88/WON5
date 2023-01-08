from geometry import Point, Rectangle

x11 = float(input('Inrodu valoarea coordonatei x pentru punctul A1!'))
y11 = float(input('Inrodu valoarea coordonatei y pentru punctul A1!'))
x12 = float(input('Inrodu valoarea coordonatei x pentru punctul B!'))
while x12 == x11:
    x12 = float(input(f'Valoarea coordonatei x pentru punctul B trebuie sa fie diferita de {x11}. Alege alt numar!'))
y12 = float(input('Inrodu valoarea coordonatei y pentru punctul B!'))
while y12 == y11:
    y12 = float(input(f'Valoarea coordonatei x pentru punctul B trebuie sa fie diferita de {y11}. Alege alt numar!'))
x21 = float(input('Inrodu valoarea coordonatei x pentru punctul A2!'))
y21 = float(input('Inrodu valoarea coordonatei y pentru punctul A2!'))
x22 = float(input('Inrodu valoarea coordonatei x pentru punctul B!'))
while x22 == x21:
    x22 = float(input(f'Valoarea coordonatei x pentru punctul B trebuie sa fie diferita de {x21}. Alege alt numar!'))
y22 = float(input('Inrodu valoarea coordonatei y pentru punctul B!'))
while y22 == y21:
    y22 = float(input(f'Valoarea coordonatei x pentru punctul B trebuie sa fie diferita de {y21}. Alege alt numar!'))

p11 = Point(x11, y11)
p12 = Point(x12, y12)
p21 = Point(x21, y21)
p22 = Point(x22, y22)

R1 = Rectangle(p11, p12)
R2 = Rectangle(p21, p22)

print(f'{R1 == R2}')

