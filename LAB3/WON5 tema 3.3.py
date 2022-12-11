lista = [2, 4, 6, -7, 9, 23.6, 0.5, 19.8, 40]
min, max = lista[0], lista[0]
for e in lista:
    if min > e:
        min = e
    if max < e:
        max = e
print('valoarea minima din lista este {}'.format(min))
print('valoarea maxima din lista este {}'.format(max))

"""l = ['shs', 'gg', 'abc']
min , max = l[0] , l[0]
for e in l:
    if min > e:
        min = e
    if max < e:
        max = e
print('valoarea minima din lista este {}'.format(min))
print('valoarea maxima din lista este {}'.format(max))"""

""" Daca lin "lista" avem si alte tipuri de informatii in afara de int sau float programul va da eroare pentru ca nu poate compara int/float cu string (de exemplu).
Se poate compara string cu string (varianta b intre ""). """