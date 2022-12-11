import statistics
catalog = {}


def import_data(filename: str):
    """Importa datele pentru crearea catalogului. Trebuie introdus un nume de fisier."""
    file = open(filename, 'r')
    for line in file:
        ln = line.strip().split(';')
        note = ln.copy()
        note.remove(note[0])
        if note[0]:
            note = [int(i) for i in note]
            catalog[ln[0]] = note
        else:
            catalog[ln[0]] = []


def print_catalog(c: dict):
    """Listeaza catalogul elevilor cu media calculata in fisierul "rezultate.txt"."""
    antet = ['Nume', 'Prenume', 'Media', 'Note', '_', 'Fara medie', 'Fara note']
    with open('rezultate.txt', 'w') as rez:
        print(f'{antet[0]:<25}{antet[1]:<25}{antet[2]:>12}{antet[3]:>12}\n{antet[4] * 74}', file=rez)
        for e in c:
            if c[e]:
                print(f'{e.split()[0]:<25}{e.split()[1]:<25}{statistics.mean(c[e]):>12.2f}{len(c[e]):>12}', file=rez)
            else:
                print(f'{e.split()[0]:<25}{e.split()[1]:<25}{antet[5]:>12}{antet[6]:>12}', file=rez)


import_data('note.txt')

print_catalog(catalog)
