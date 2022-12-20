import os

count_py = 0
address = 'C:/Python/WON5'
for root, dirs, files in os.walk(address):
    for f in files:
        ext = f.split('.')[-1].lower()
        if ext == 'py':
            count_py += 1
            print(f'{root}/{f}')
print('Nr. Python files {}'.format(count_py))
