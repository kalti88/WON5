import statistics

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
antet = ['Nume', 'Prenume', 'Media', 'Note', '_']
print(f'{antet[0]:<25}{antet[1]:<25}{antet[2]:5}{antet[3]:^8}\n{antet[4] * 61}')
for e in catalog:
    print(f'{e.split()[0]:<25}{e.split()[1]:<25}{statistics.mean(catalog[e]):5.2f}{len(catalog[e]):^8}')
