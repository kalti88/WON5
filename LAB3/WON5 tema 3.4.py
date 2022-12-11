s = "În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele? Variante: perele, merele, prunele și apoi ciresele. Foarte gresit! Corect este: ciresele, merele, perele și apoi prunele."
propozitii, cuvinte, l, no = 0, [], [], 0
for e in s:
    if e == '!' or e == '?' or e == '.':
        propozitii += 1
print('Numarul de propozitii din text este {}.'.format(propozitii))
cuvinte = s.split(' ')
print('Numarul de propozitii din text este {}.'.format(len(cuvinte)))
l = s.split(' ')
for e in l:
    l[no] = e.strip('.')
    l[no] = l[no].strip('?')
    l[no] = l[no].strip(',')
    l[no] = l[no].strip(':')
    l[no] = l[no].strip('!')
    l[no] = l[no].lower()
    no += 1
print('Cuvintele "curate" sunt: \n {}'.format(l))
