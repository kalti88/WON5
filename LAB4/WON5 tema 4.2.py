import statistics
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
print('Lista elevilor in ordinea alfabetica cu media notelor este:')
lista_nume = sorted(d)
d_alfabet = {}
i = 0
while i < len(lista_nume):
    for e in d:
        if e == lista_nume[i]:
            d_alfabet[e] = d[e]
    i += 1
i = 1
for elev in d_alfabet:
    #print('{}. {} - {}'.format(i, elev, f'{(statistics.mean(d_alfabet[elev])):.2f}'))
    print('{}. {} - {}'.format(i, elev, '{:.2f}'.format((statistics.mean(d_alfabet[elev])))))
    i += 1
