import os

total = 0
for roots, dirs, files in os.walk('C:/Users/Zsolt/PycharmProjects/PITHON_WON5'):
    for f in files:
        total += os.path.getsize(f'{roots}/{f}')
print('C:/Users/Zsolt/PycharmProjects/PITHON_WON5')
print('Total file size {} Megabytes'.format(total/(1024**2)))
