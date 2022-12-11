def media(a):
    lista_medii = []
    for k, v in a.items():
        if v:
            media = round(sum(v) / len(v), 2)
        else:
            media = 0
        lista_medii.append(media)
    media_generala = round(sum(lista_medii) / len(lista_medii), 2)
    print('Media generala a clasei e', media_generala)


catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
media(catalog)