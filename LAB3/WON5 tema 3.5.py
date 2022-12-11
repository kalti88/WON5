s = "În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele? Variante: perele, merele, prunele și apoi ciresele. Foarte gresit! Corect este: ciresele, merele, perele și apoi prunele."
i, l, no, l2, l4 = 0, [], 0, [], []
lista = s
l = s.split(' ')
for e in l:
    l[no] = e.strip('.')
    l[no] = l[no].strip('?')
    l[no] = l[no].strip(',')
    l[no] = l[no].strip(':')
    l[no] = l[no].strip('!')
    l[no] = l[no].lower()
    no += 1
while i < len(l):
    ctr = 0
    for e in l2:
        if l[i] == e:
            ctr = 1
    if ctr == 0:
        l2 += [l[i]]
    i += 1
print('Lista cuvintelor prezente in text: \n {}'.format(l2))
l3 = l2
a = 0
while a < (int(len(l3) / 2) - 1):
    min = l3[a]
    max = l3[a]
    for e in l3[a:(len(l3) - a)]:
        if min > e:
            min = e
        if max < e:
            max = e
    i = 0
    while i < len(l3):
        if l3[i] == min:
            l3[i], l3[a] = l3[a], l3[i]
        if l3[i] == max:
            l3[i], l3[(len(l3) - a - 1)] = l3[(len(l3) - a - 1)], l3[i]
        i += 1
    a += 1
print('Lista cuvintelor in ordinea alfabetica: \n {}'.format(l3))
test = l2
test.sort()
print(test)
