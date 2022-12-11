import statistics
def get_second_elem(iterable):
    return iterable[1]
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
sorted_d_media = sorted(d_media.items(), key=get_second_elem, reverse=True)
print('Lista elevilor in ordinea descrescatoare ale mediilor notelor este:')
i = 1
for e, m in sorted_d_media:
    print('{}. {} - {}'.format(i, e, m))
    i += 1
