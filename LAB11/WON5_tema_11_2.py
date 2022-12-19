import os

count_dir = 0
count_files = 0
address = 'C:/Users/Zsolt/PycharmProjects/PITHON_WON5'
for roots, dirs, files in os.walk(address):
    count_dir += len(dirs)
    count_files += len(files)
print(address)
print('Nr. Folders {}'.format(count_dir))
print('Nr. Files {}'.format(count_files))
