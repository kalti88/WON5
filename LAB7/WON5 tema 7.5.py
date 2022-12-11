import statistics

catalog = {}
note_teza = {}
lista_ord_alfa = []
lista_p = []
lista_corigenti = []


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
    for e in c:
        lista_ord_alfa.append(e)
    lista_ord_alfa.sort()


def selectare_note(c):
    for e in c:
        if len(c[e]) > 3:
            c[e].sort(reverse=True)
            c[e] = [c[e][i] for i in range(0, 3)]


def premianti_3(c: dict, t: dict):
    """Listeaza premiantii clasei cu media calculata (dupa metoda noua) in fisierul "premianti metoda noua.txt"."""
    for e in c:
        media = ((statistics.mean(c[e]) + t[e]) / 2) if (c[e] and t[e]) else 0
        lista_p.append((media, e))
    lista_p.sort(reverse=True)
    antet = ['Premiu', 'Elev', 'Media finala', '_', 'Fara medie', 'Fara note']
    with open('premianti metoda noua.txt', 'w') as prem:
        print(f'{antet[0]:<8}{antet[1]:<25}{antet[2]:>12}\n{antet[3] * 45}', file=prem)
        for e in range(0, 3):
            if lista_p[e]:
                print(f'{e + 1:<8}{lista_p[e][1]:<25}{(lista_p[e][0]):>12.2f}', file=prem)
            else:
                print(f'{e + 1:<8}{lista_p[e][1]:<25}{antet[5]:>12}{antet[6]:>12}', file=prem)


def corigenti(c: dict, t: dict):
    """Listeaza corigentii clasei cu media calculata (dupa metoda noua) in fisierul "corigenti metoda noua.txt"."""
    for e in c:
        media = ((statistics.mean(c[e]) + t[e]) / 2) if (c[e] and t[e]) else 0
        lista_corigenti.append((media, e))
    lista_corigenti.sort()
    antet = ['Nr.ord.', 'Elev', 'Media finala', '_', 'Fara medie', 'Fara note']
    with open('corigenti metoda noua.txt', 'w') as corg:
        print(f'{antet[0]:<8}{antet[1]:<25}{antet[2]:>12}\n{antet[3] * 45}', file=corg)
        i = 0
        while lista_corigenti[i][0] < 5:
            if lista_corigenti[i][0]:
                print(f'{i + 1:<8}{lista_corigenti[i][1]:<25}{(lista_corigenti[i][0]):>12.2f}', file=corg)
            else:
                print(f'{i + 1:<8}{lista_corigenti[i][1]:<25}{antet[5]:>12}{antet[6]:>12}', file=corg)
            i += 1


def print_rezultate_finle(c: dict, t: dict):
    """Listeaza rezultatele finale calculata cu metoda noua in fisierul "rezultate finale metoda noua"."""
    antet = ['Nume', 'Prenume', 'Media finala', 'Fara note si teza', '_', 'Fara teza', 'Fara note']
    with open('rezultate finale metoda noua.txt', 'w') as rez_fin_n:
        print(f'{antet[0]:<25}{antet[1]:<25}{antet[2]:>12}\n{antet[4] * 62}', file=rez_fin_n)
        for e in lista_ord_alfa:
            if c[e]:
                if t[e]:
                    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{((statistics.mean(c[e]) + t[e]) / 2):>12.2f}',
                          file=rez_fin_n)
                else:
                    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{antet[5]:>12}', file=rez_fin_n)
            else:
                if t[e]:
                    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{antet[6]:>12}', file=rez_fin_n)
                else:
                    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{antet[3]:>12}', file=rez_fin_n)


import_data('note.txt', 'teze.txt')

selectare_note(catalog)

lista_alfabet(catalog)

print_rezultate_finle(catalog, note_teza)

premianti_3(catalog, note_teza)

corigenti(catalog, note_teza)
