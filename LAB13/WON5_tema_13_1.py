from geometry import Point, Rectangle

x1 = float(input('Inrodu valoarea coordonatei x pentru punctul A!'))
y1 = float(input('Inrodu valoarea coordonatei y pentru punctul A!'))
x2 = float(input('Inrodu valoarea coordonatei x pentru punctul B!'))
y2 = float(input('Inrodu valoarea coordonatei y pentru punctul B!'))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

R = Rectangle(p1, p2)
l1, l2 = R.length_of_sides()
prm = R.rectangle_perimeter()
area = R.rectangle_area()

print(f'Lungimea laturilor dreptunghiului format din puntele A si B sunt {l1:,.2f} si {l2:,.2f}')
print(f'Perimetrul dreptunghiului este {prm:,.2f}')
print(f'Aria dreptunghiului este {area:,.2f}')
