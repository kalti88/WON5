import WON5_Module_tema9_5b as m


catalog = m.import_data_create_catalog('note.txt')

premiantii = m.premianti_3(catalog)

i = 1
for i in range(1, 4):
    m.create_diploma('diploma.txt', premiantii, i)
    i += 1
