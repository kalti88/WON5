import os

count_py = 0
for roots, dirs, files in os.walk('C:/Users/Zsolt/PycharmProjects/PITHON_WON5'):
    for f in files:
        ext = f.split('.')[-1].lower()
        if ext == 'py':
            count_py += 1
            print(os.path.abspath(f))
print('Nr. Python files {}'.format(count_py))
