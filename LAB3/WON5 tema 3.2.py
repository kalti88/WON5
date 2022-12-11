lista = ['ABCD', '12', 'w', '-', ':-)']
i = 0
for s in lista:
    lista[i] = s[::-1]
    i += 1
print(lista[::-1])
