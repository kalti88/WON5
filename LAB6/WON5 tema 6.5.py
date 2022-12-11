import statistics


def sortare(d, d_alfabet):
    lista_nume = sorted(d)
    i = 0
    while i < len(lista_nume):
        for k in d:
            if k == lista_nume[i]:
                d_alfabet[k] = d[k]
        i += 1
    i = 1


def lung(li):
    global maxnume
    global maxprenume
    for n in li:
        if len(n.split()[0]) > maxnume:
            maxnume = len(n.split()[0])
        if len(n.split()[1]) > maxprenume:
            maxprenume = len(n.split()[1])


catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
maxnume = len('Nume')
maxprenume = len('Prenume')
catalog_alfabet = {}
sortare(catalog, catalog_alfabet)
lung(catalog)

antet = ['Nume', 'Prenume', 'Media', 'Note', '_']
print(f'{antet[4] * (maxnume + maxprenume +19)}\n|{antet[0]:<{maxnume + 2}}{antet[1]:<{maxprenume+2}}{antet[2]:5}{antet[3]:^8}|\n{antet[4] * (maxnume + maxprenume +19)}')
for e in catalog_alfabet:
    print(
        f'|{e.split()[0]:<{maxnume +2}}{e.split()[1]:<{maxprenume + 2}}{statistics.mean(catalog_alfabet[e]):5.2f}{len(catalog_alfabet[e]):^8}|')
print(f'{antet[4] * (maxnume + maxprenume +19)}')
