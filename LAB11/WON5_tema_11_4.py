import os

total = 0
address = 'C:/Users/Zsolt/PycharmProjects/PITHON_WON5'
for root, dirs, files in os.walk(address):
    for f in files:
        total += os.path.getsize(f'{root}/{f}')
print(address)
print('Total file size {} Megabytes'.format(f'{total/(1024**2):.2f}'))
