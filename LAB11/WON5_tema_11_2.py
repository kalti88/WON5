import os

count_dir = 0
count_files = 0
for roots, dirs, files in os.walk('C:/Users/Zsolt/PycharmProjects/PITHON_WON5'):
    count_dir += len(dirs)
    count_files += len(files)
print(os.getcwd())
print('Nr. Folders {}'.format(count_dir))
print('Nr. Files {}'.format(count_files))
