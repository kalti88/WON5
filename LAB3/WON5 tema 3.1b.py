x = int(input('Introdu numarul intreg la care vrei sa calculezi factorialul'))
factorial = 1
for e in range(1, x+1):
    factorial = factorial * e
print('Factorialul numarului {} este {}'.format(x, factorial))