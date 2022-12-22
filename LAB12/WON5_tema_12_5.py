import geometry

P1 = geometry.Point(2, 9)
P2 = geometry.Point(-4, 11)
P3 = geometry.Point(7, 3)
P4 = geometry.Point(-4, 6)
C1 = geometry.Circle(3, 5, 6)

li = [P1, P2, P3, P4]
li_sort = sorted(li, key=lambda x: x.get_distance())
for i in li:
    print(f'{i.get_distance():,.4f}')
print('-----------------------')
for i in li_sort:
    print(f'{i.get_distance():,.4f}')
