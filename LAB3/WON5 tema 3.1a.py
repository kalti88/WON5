x = int(input('Introdu numarul intreg la care vrei sa calculezi factorialul'))
f, factorial = 1, 1
while f <= x:
    factorial = factorial * f
    f = f+1
print('Factorialul numarului {} este {}'.format(x, factorial))