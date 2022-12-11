a = float(input('Introdu prima latura: '))
b = float(input('Introdu a doua latura: '))
c = float(input('Introdu a treia latura: '))
oarecare=True
if a==b==c:
    print('Triunghiul este echilateral')
    oarecare=False
elif (a==b or b==c or a==c):
    print('Triunghiul este isoscel')
    oarecare = False
if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
    print('Triunghiul este dreptunghic')
    oarecare=False
if oarecare:
    print('Triunghi este oarecare')

