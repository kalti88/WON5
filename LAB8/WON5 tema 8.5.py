import xlsxwriter
import statistics


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
    """
    catalog = {}
    with open(filename, 'r') as file:
        for line in file:
            ln = line.strip().split(';')
            note = ln.copy()
            note.remove(note[0])
            if note[0]:
                note = [float(i) for i in note]
                catalog[ln[0]] = round(statistics.mean(note), 2)
    return catalog


catalog = import_data_create_catalog('note.txt')

workbook = xlsxwriter.Workbook('catalog_excel.xlsx')

worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', len(max(catalog, key=len)) + 10)
worksheet.set_column('B:B', len('Media') + 10)

cell_1 = workbook.add_format()
cell_2 = workbook.add_format()

cell_1.set_align('left')
cell_2.set_align('right')
cell_2.set_bold('bold')

number_format = workbook.add_format({'num_format': '#,##0.00'})

bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Nume elev', bold)
worksheet.write('B1', 'Media', cell_2)
row = 1
col = 0
for elev in sorted(catalog):
    worksheet.write(row, col, elev, cell_1)
    worksheet.write_number(row, col+1, catalog[elev], cell_format=number_format)
    row += 1

workbook.close()
