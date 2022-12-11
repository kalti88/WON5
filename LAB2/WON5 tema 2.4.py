sir = input('Introdu sirul de caractere')
pozitie = 0
lista_sir = []
lista_sir += sir
palindrom = True
while pozitie < (int(len(lista_sir)/2) -1):
    if lista_sir[pozitie] == lista_sir[(len(lista_sir)-pozitie-1)]:
        pozitie += 1
    else:
        palindrom = False
        break
if palindrom:
    print("Sirul e palindrom")
else:
    print("Sirul nu e palindrom")