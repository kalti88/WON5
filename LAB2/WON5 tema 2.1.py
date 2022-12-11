my_list = list('ABcdEfghI')

i = 0
while i < len(my_list):               #Ajunge sa conditionam functia while la i < len(my_list) (nu la <=). Pozitia my_list[len(my_list)] nu exista.
    if 'A' <= my_list[i] <= 'Z':      #Se poate scri conditia my_list[i] > 'A' and 'Z' > my_list[i] mai simplu
        print(my_list[i])
    i += 1
    if i==len(my_list):               # lipseste conditia la care se activeaza functia break
        break # gata programul        # break trebuie sa fie in interiorul functiei if si va intrerupe functia while, deci trebuie sa fie la 2 TAB-uri