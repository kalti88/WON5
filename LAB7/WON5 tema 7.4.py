import statistics
catalog = {}
note_teza = {}

def import_data(filename1: str, filename2: str):
    """Importa datele pentru crearea catalogului listei cu notele de la teza. Trebuie introdus doua nume de fisier."""
    file = open(filename1, 'r')
    for line in file:
        ln = line.strip().split(';')
        note = ln.copy()
        note.remove(note[0])
        if note[0]:
            note = [int(i) for i in note]
            catalog[ln[0]] = note
        else:
            catalog[ln[0]] = []
    file2 = open(filename2, 'r')
    for line in file2:
        ln = line.strip().split(';')
        teza = ln.copy()
        if teza[1]:
            nota_teza = int(teza[1])
            note_teza[teza[0]] = nota_teza
        else:
            note_teza[teza[0]] = []


def lista_alfabet(c: dict):
    """Creaza o lista cu toate numele din catalog in ordine alfabetica."""
    lista_ord_alfa = []
    for e in c:
        lista_ord_alfa.append(e)
    lista_ord_alfa.sort()
    return lista_ord_alfa


def print_rezultate_finale(c: dict, t: dict):
    """Calculeaza mediile finale (media note - teza) si afiseaza in fisierul "rezultate finale.txt"."""
    antet = ['Nume', 'Prenume', 'Media finala', 'Fara note si teza', '_', 'Fara teza', 'Fara note']
    lista_elevi = lista_alfabet(c)
    with open('rezultate finale.txt', 'w') as rez_fin:
        print(f'{antet[0]:<25}{antet[1]:<25}{antet[2]:>12}\n{antet[4] * 62}', file=rez_fin)
        for e in lista_elevi:
            if c[e]:
                if t[e]:
                    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{((statistics.mean(c[e]) + t[e])/2):>12.2f}', file=rez_fin)
                else:
                    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{antet[5]:>12}', file=rez_fin)
            else:
                if t[e]:
                    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{antet[6]:>12}', file=rez_fin)
                else:
                    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{antet[3]:>12}', file=rez_fin)


import_data('note.txt', 'teze.txt')

print_rezultate_finale(catalog, note_teza)
