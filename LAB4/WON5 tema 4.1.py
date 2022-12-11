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
print('Lista elevilor cu media notelor este:')
i = 1
for elev in d:
    print('{}. {} - {}'.format(i, elev, f'{(statistics.mean(d[elev])):.2f}'))
    i += 1

