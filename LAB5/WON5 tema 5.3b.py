def schimb_nota(elev, nota=None):
    if nota == None:
        if elev not in catalog:
            print('Acest nume nu exista in catalog.')
        else:
            catalog[elev] = []
    else:
        if elev not in catalog:
            print('Acest nume nu exista in catalog.')
        else:
            if (nota not in range(1, 11)) or (nota not in catalog[elev]):
                print('Nu exista aceasta nota.')
            else:
                for e in catalog:
                    if e == elev:
                        for f in catalog[e]:
                            if f == nota:
                                catalog[e].remove(f)
                return catalog[e]


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
#nota = int(input('Introdu nota de eliminat:\n'))
schimb_nota(elev)
catalog_actual(catalog)
