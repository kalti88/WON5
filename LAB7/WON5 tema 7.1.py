import statistics
catalog = {}


def import_data(filename: str):
    """Importa datele pentru crearea catalogului. Trebuie introdus un nume de fisier."""
    file = open(filename, 'r')
    for line in file:
        ln = line.strip().split(';')
        note = ln.copy()
        note.remove(note[0])
        if True or note[0]:
            note = [int(i) for i in note]
            catalog[ln[0]] = note
        else:
            catalog[ln[0]] = []


def print_catalog(c: dict):
    """Listeaza catalogul elevilor cu media calculata pe ecran."""
    antet = ['Elev', 'Media', '_', 'Fara note']
    print(f'{antet[0]:<55}{antet[1]:5}\n{antet[2] * 60}')
    for e in c:
        if c[e]:
            print(f'{e:<50}{statistics.mean(c[e]):10.2f}')
        else:
            print(f'{e:<50}{antet[3]:>10}')


import_data('note.txt')

print_catalog(catalog)
