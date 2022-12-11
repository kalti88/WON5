lista = []
sir = input('Introdu primul caracter')
n_citire = 1
while sir != 'x' or sir != 'X':
    lista += [sir]
    n_citire += 1
    sir = input('Introdul al {}-a caracter'.format(n_citire))
    if sir == 'x' or sir == 'X':
        print(lista)
        break
