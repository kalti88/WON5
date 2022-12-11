import statistics
def media_m(elev, materie=None):
    if materie is None:
        if elev not in catalog:
            print('Acest nume nu exista in catalog.')
        else:
            catalog_medii = catalog
            for k, v in catalog[elev].items():
                if v:
                    media = round(sum(v) / len(v), 2)
                else:
                    media = 0
                catalog_medii[elev][k] = media
            print('Elevul {} are urmatoarele medii:'.format(elev))
            for e in catalog_medii[elev]:
                print('{}: {}'.format(denumiri[e], catalog_medii[elev][e]))
    else:
        if elev not in catalog:
            print('Acest nume nu exista in catalog.')
        else:
            if catalog[elev][materie]:
                print('Elevul {} are media la {}: {}'.format(elev, denumiri[materie], '{:.2f}'.format(statistics.mean(catalog[elev][materie]))))
            else:
                print('Elevul {} nu are note la {}'.format(elev, denumiri[materie]))


denumiri = {
    'm': 'Matematica',
    'r': 'Romana',
    'f': 'Fizica'
}

catalog = {
    'Popescu Ion': {
        'm': [2, 5, 7],
        'f': [],
        'r': [6, 9, 8],
    },
    'Ionescu Geta': {
        'r': [6, 3, 8],
        'm': [4, 5],
        'f': [7, 9, 10]
    },
    'Georgescu Gelu': {
        'm': [2, 5, 7, 9],
        'r': [9, 8],
        'f': [6, 9]
    },
    'Radulescu Ioana': {
        'm': [7],
        'f': [],
        'r': [6, 9, 8],
    },
}

elev = input('Introdu numele elevului:\n')
media_m(elev)