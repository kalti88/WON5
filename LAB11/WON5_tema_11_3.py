import os

count_py = 0
address = 'C:/Users/Zsolt/PycharmProjects/PITHON_WON5'
for roots, dirs, files in os.walk(address):
    for f in files:
        ext = f.split('.')[-1].lower()
        if ext == 'py':
            count_py += 1
            print(f'{roots}/{f}')
print('Nr. Python files {}'.format(count_py))
