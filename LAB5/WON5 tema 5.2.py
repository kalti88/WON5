def schimb_nota(elev, nota, overwrite=False):
    if elev in catalog:
        if 1 <= nota <= 10:
            if overwrite:
                catalog[elev] = [nota]
            else:
                catalog[elev].append(nota)
        else:
            print('Nu exista nota.')
    else:
        print('Acest nume nu exista in catalog.')


def catalog_actual(d):
    print('Catalogul actual este:')
    i = 1
    for e in d:
        print('{}. {} - {}'.format(i, e, (d[e])))
        i += 1


def suprascriere():
    supra = input('Vrei sa suprascrii notele elevului? Da/Nu \n')
    return supra.lower() == 'da'


catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
elev = input('Introdu numele elevului:\n')
nota = int(input('Introdu nota noua:\n'))
overwrite = suprascriere()
schimb_nota(elev, nota, overwrite)
catalog_actual(catalog)
