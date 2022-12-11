ls = ['5', '123', '-7', '33']
li = [5, 123, -7, 33]

ls_sorted = sorted(ls, key=float)
li_sorted = sorted(li)

print(ls_sorted)
print(li_sorted)

l = [(5, 21, 8), (6, 11, -5), (0, 25, 3), (-6, 6, 1)]
l_sorted = sorted(l, key=lambda x: sum(x))
print(l_sorted)
