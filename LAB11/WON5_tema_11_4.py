import os

total = 0
address = 'C:/Users/Zsolt/PycharmProjects/PITHON_WON5'
for roots, dirs, files in os.walk(address):
    for f in files:
        total += os.path.getsize(f'{roots}/{f}')
print(address)
print('Total file size {} Megabytes'.format(total/(1024**2)))
