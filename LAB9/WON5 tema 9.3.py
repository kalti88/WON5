rezultat = list(map(lambda x, y, z: (x + y) * z,
                    [2, 3, 1],
                    [1, 4, 5],
                    ['A', 'q', '#']
                    )
                )
print(rezultat)  # ['AAA', 'qqqqqqq', '######']
