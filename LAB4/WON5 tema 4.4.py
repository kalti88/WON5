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
d_media = {}
for e in d:
    d_media[e] = f'{(statistics.mean(d[e])):.2f}'
d_corigenti = {}
for elev in d_media:
    if float(d_media[elev]) < 5:
        d_corigenti[elev] = d_media[elev]
print('Lista elevilor corigenti este:')
i = 1
for elev in d_corigenti:
    print('{}. {} - {}'.format(i, elev, d_corigenti[elev]))
    i += 1
