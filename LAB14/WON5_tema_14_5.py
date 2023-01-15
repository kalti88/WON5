from geometry import Point, Rectangle

p11 = Point(1, 2)
p12 = Point(0, 23)

p21 = Point(5, 7)
p22 = Point(8, 10)

p31 = Point(5, 5)
p32 = Point(55, -11)

p41 = Point(12, 12)
p42 = Point(15, 15)

r1 = Rectangle(p11, p12)
r2 = Rectangle(p21, p22)
r3 = Rectangle(p31, p32)
r4 = Rectangle(p41, p42)

print(Rectangle.get_square_percent())
