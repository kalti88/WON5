import statistics


def import_data(filename1, filename2):
    """Importa datele pentru crearea catalogului de note si notele de teza.

    Parameters
    ----------
    filename1 : str
                Fisierul "txt" care contine numele si notele elevilor
    filename2 : str
                Fisierul "txt" care contine numele elevilor si notele lor de la teza

    Returns
    -------
    tuple:
                Returneaza dictionarul care contine catalogul clasei.
                Returneza dictionarul care contine notele de la teza.
    """

    catalog = {}
    note_teza = {}
    with open(filename1, 'r') as file:
        for line in file:
            ln = line.strip().split(';')
            note = ln.copy()
            note.remove(note[0])
            if note[0]:
                note = [int(i) for i in note]
                catalog[ln[0]] = note
    with open(filename2, 'r') as file2:
        for line in file2:
            ln = line.strip().split(';')
            teza = ln.copy()
            if teza[1]:
                nota_teza = int(teza[1])
                note_teza[teza[0]] = nota_teza
    return catalog, note_teza


def print_catalog(c: dict):
    """Listeaza catalogul elevilor cu media calculata pe ecran.

    Parameters
    ----------
    c : dict
        Dictionar care contine catalogul clasei

    Returns
    -------
    None
    """
    antet = ['Elev', 'Media', '_', 'Fara note']
    print(f'{antet[0]:<55}{antet[1]:5}\n{antet[2] * 60}')
    for e in c:
        if c[e]:
            print(f'{e:<50}{statistics.mean(c[e]):10.2f}')
        else:
            print(f'{e:<50}{antet[3]:>10}')


def print_catalog_file(c: dict):
    """Listeaza catalogul elevilor cu media calculata in fisierul "rezultate.txt"

        Parameters
        ----------
        c : dict
            Dictionar care contine catalogul clasei

        Returns
        -------
        None
        """
    antet = ['Nume', 'Prenume', 'Media', 'Note', '_', 'Fara medie', 'Fara note']
    with open('rezultate.txt', 'w') as rez:
        print(f'{antet[0]:<25}{antet[1]:<25}{antet[2]:>12}{antet[3]:>12}\n{antet[4] * 74}', file=rez)
        for e in c:
            if c[e]:
                print(f'{e.split()[0]:<25}{e.split()[1]:<25}{statistics.mean(c[e]):>12.2f}{len(c[e]):>12}', file=rez)
            else:
                print(f'{e.split()[0]:<25}{e.split()[1]:<25}{antet[5]:>12}{antet[6]:>12}', file=rez)


def premianti_3(c: dict):
    """Listeaza premiantii clasei cu media calculata in fisierul "premianti.txt".

    Parameters
    ----------
    c : dict
        Dictionar care contine catalogul clasei

    Returns
    -------
    None
    """
    lista_p = []
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
    return lista_p


def print_rezultate_finale(c: dict, t: dict):
    """Calculeaza mediile finale (media note - teza) si afiseaza in fisierul "rezultate finale.txt".

        Parameters
        ----------
        c : dict
            Dictionar care contine catalogul clasei
        t : dict
            Dictionar care contine notele de la teza

        Returns
        -------
        None
        """
    antet = ['Nume', 'Prenume', 'Media finala', 'Fara note si teza', '_', 'Fara teza', 'Fara note']
    lista_ord_alfa = []
    for e in c:
        lista_ord_alfa.append(e)
    lista_elevi = sorted(lista_ord_alfa)
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

