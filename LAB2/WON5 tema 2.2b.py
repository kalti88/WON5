a = eval(input('Introdu prima latura: '))
b = eval(input('Introdu a doua latura: '))
c = eval(input('Introdu a treia latura: '))
oarecare=True
if a==b==c:
    print ('Triunghiul este echilateral')
    oarecare=False
elif (a==b or b==c or a==c):
    print('Triunghiul este isoscel')
    oarecare = False
if (round(a**2, 5) == round(b**2, 5) + round(c**2, 5)) or (round(b**2, 5) == round (a**2, 5) + round (c**2, 5)) or (round(c**2, 5) == round (a**2, 5) + round (b**2, 5)):
    print('Triunghiul este dreptunghic')
    oarecare=False
if oarecare:
    print('Triunghi este oarecare')