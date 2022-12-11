import statistics
catalog = {}
lista_p = []


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


def premianti_3(c: dict):
    """Listeaza premiantii clasei cu media calculata in fisierul "premianti.txt"."""
    for e in c:
        media = statistics.mean(c[e]) if c[e] else 0
        lista_p.append((media, e))
    lista_p.sort(reverse=True)
    antet = ['Premiu', 'Elev', 'Media', '_', 'Fara medie', 'Fara note']
    with open('premianti.txt', 'w') as prem:
        print(f'{antet[0]:<8}{antet[1]:<25}{antet[2]:>12}\n{antet[3] * 45}', file=prem)
        for e in range(0, 3):
            if lista_p[e]:
                print(f'{e+1:<8}{lista_p[e][1]:<25}{(lista_p[e][0]):>12.2f}', file=prem)
            else:
                print(f'{e+1:<8}{lista_p[e][1]:<25}{antet[5]:>12}{antet[6]:>12}', file=prem)


import_data('note.txt')

premianti_3(catalog)
