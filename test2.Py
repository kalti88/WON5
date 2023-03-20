tb_supp = [('ala', 1), ('bala', 2), ('dala', 3)]
supp = 'bala'
supp_id = 0
for i in tb_supp:
    if i[0] == supp:
        supp_id = i[1]
print(supp_id)
