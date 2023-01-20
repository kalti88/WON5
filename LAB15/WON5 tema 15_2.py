def import_data(filename: str):
    """Importa datele din csv

    Parameters
    ----------
    filename: str
                Fisierul ce contine datele elevilor.

    Returns
    -------
    list:
            Returneaza o lista cu datele pentru coduri.
    """
    lista = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i > 0:
                ln = line.strip().split(',')
                print('insert into student (surname, first_name, class_nr, class_letter, birth_date, average_grade)')
                print(f"    values ('{ln[0]}', '{ln[1]}', '{ln[2]}', '{ln[3]}', '{ln[4]}', '{ln[5]}');")
                print('')


import_data('student.csv')

