import os


def count_py_files(address):
    count_py = 0

    def local_count_py_files(address):
        nonlocal count_py
        for item in os.listdir(address):
            if os.path.isfile(f'{address}/{item}'):
                ext = item.split('.')[-1].lower()
                if ext == 'py':
                    count_py += 1
                    print(f'{address}/{item}')
            elif os.path.isdir(f'{address}/{item}'):
                ad = f'{address}/{item}'
                local_count_py_files(ad)
    local_count_py_files(address)
    return count_py


address = 'C:/Users/Zsolt/PycharmProjects/PITHON_WON5/'
py_file = count_py_files(address)
print('Nr. Python files {}'.format(py_file))
