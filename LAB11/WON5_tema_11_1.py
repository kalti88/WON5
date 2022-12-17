import statistics


def media(t):
    """Calculeaza media numerelor din tupla.

    Parameters
    ----------
    t: tuple
        Tupla cu cel putin un numar intreg.

    Returns
    -------
    float:
        Media numerelor din tupla.

    Example usage:
    >>> media((5, 6, 20, 21))
    13.0
    >>> media((50, 150, 500, 1000))
    425.0
    """
    tot = 0
    for i in t:
        tot += i
    med = tot / len(t)
    return med


def import_data_create_catalog(filename: str):
    """Importa datele pentru crearea catalogului cu medii

    Parameters
    ----------
    filename: str
                Fisierul ce contine numele si notele elevilor.

    Returns
    -------
    dict:
            Returneaza catalogul elevilor cu mediile calculate.

    Example usage:
    >>> import_data_create_catalog('note.txt')
    {'Popescu Ion': 3, 'Ionescu Geta': 8.25, 'Georgescu Gelu': 3, 'Radulescu Ioana': 6.8, 'Vasilescu Vasile': 8.5, \
'Bengescu Hortensia': 9}
    """
    catalog = {}
    with open(filename, 'r') as file:
        for line in file:
            ln = line.strip().split(';')
            note = ln.copy()
            note.remove(note[0])
            if note[0]:
                note = [int(i) for i in note]
                catalog[ln[0]] = round(statistics.mean(note), 2)
    return catalog


def premianti_3(c: dict):
    """Creeaza lista cu cei 3 premianti.

    Parameters
    ----------
    c : dict
        Dictionar care contine catalogul clasei

    Returns
    -------
    list
        "Lista cu cei 3 premianti.

    Example usage:
    >>> premianti_3({'Popescu Ion': 3, 'Ionescu Geta': 8.25, 'Georgescu Gelu': 3, 'Radulescu Ioana': 6.8, \
'Vasilescu Vasile': 8.5, 'Bengescu Hortensia': 9})
    [(9, 'Bengescu Hortensia'), (8.5, 'Vasilescu Vasile'), (8.25, 'Ionescu Geta')]
    """
    lista_p = []
    for e in c:
        lista_p.append((c[e], e))
    lista_p.sort(reverse=True)
    return lista_p[:3]


if __name__ == '__main__':
    from doctest import testmod
    # testmod()
    testmod(verbose=True)
