import statistics

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
antet = ['Elev', 'Media', '_']
print(f'{antet[0]:<50}{antet[1]:5}\n{antet[2]*55}')
for e in catalog:
    print(f'{e:<50}{statistics.mean(catalog[e]):5.2f}')
