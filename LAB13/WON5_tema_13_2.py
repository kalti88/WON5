def abs_val(x):
    """
    Return the absolute value of a float.
    :param x: A float number
    :type x: float
    :return: Absolute value for x
    :rtype: float
    """
    return -x if x < 0 else x


x = float(input('Introdu numarul'))
print(f'Valoarea absoluta a numarului introdus {abs_val(x)}')

