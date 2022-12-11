def nota_noua (elev, nota):
    if elev in catalog:
        if 1 <= nota <= 10:
            catalog[elev].append(nota)
        else:
            print('Nu exista aceasta nota.')
    else:
        print('Acest nume nu exista in catalog.')


def catalog_actual(d):
    print('Catalogul actual este:')
    i = 1
    for e in d:
        print('{}. {} - {}'.format(i, e, (d[e])))
        i += 1

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
elev = input('Introdu numele elevului:\n')
nota = int(input('Introdu nota noua:\n'))
nota_noua(elev, nota)
catalog_actual(catalog)

