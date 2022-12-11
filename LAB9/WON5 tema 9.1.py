import math


l = [(5, 21), (6, 11), (0, 25), (-6, 6)]

l_sorted = sorted(l, key=lambda x: math.prod(x))

print(l_sorted)
