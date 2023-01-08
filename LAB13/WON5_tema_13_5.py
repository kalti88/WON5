from geometry import Point, Rectangle

x11 = float(input('Inrodu valoarea coordonatei x pentru punctul A1!'))
y11 = float(input('Inrodu valoarea coordonatei y pentru punctul A1!'))
x12 = float(input('Inrodu valoarea coordonatei x pentru punctul B1!'))
y12 = float(input('Inrodu valoarea coordonatei y pentru punctul B1!'))
x21 = float(input('Inrodu valoarea coordonatei x pentru punctul A2!'))
y21 = float(input('Inrodu valoarea coordonatei y pentru punctul A2!'))
x22 = float(input('Inrodu valoarea coordonatei x pentru punctul B2!'))
y22 = float(input('Inrodu valoarea coordonatei y pentru punctul B2!'))

p11 = Point(x11, y11)
p12 = Point(x12, y12)
p21 = Point(x21, y21)
p22 = Point(x22, y22)

R1 = Rectangle(p11, p12)
R2 = Rectangle(p21, p22)

print(f'{R1 == R2}')

