d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (9,),
    'Popescu Sandokan': (7, 6, 7),
}
lista = []
nume_fam = {}
for e in d:
    lista.append(e.split(' '))
for e in lista:
    if e[0] in nume_fam:
        nume_fam[e[0]] = int(nume_fam[e[0]]) + 1
    else:
        nume_fam[e[0]] = 1
print('Lista frecventei numelor de familie este:')
i = 1
for elev in nume_fam:
    if nume_fam[elev] == 1:
        print('{}. Numele de familie {} apare o data.'.format(i, elev))
    else:
        print('{}. Numele de familie {} apare de {} ori.'.format(i, elev, nume_fam[elev]))
    i += 1

