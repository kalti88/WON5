import os


def total_size(address):
    total = 0

    def local_total_size(address):
        nonlocal total
        for item in os.listdir(address):
            if os.path.isfile(f'{address}/{item}'):
                total += os.path.getsize(f'{address}/{item}')
            elif os.path.isdir(f'{address}/{item}'):
                ad = f'{address}/{item}'
                local_total_size(ad)
    local_total_size(address)
    return total


address = 'C:/Users/Zsolt/PycharmProjects/PITHON_WON5/'
total = total_size(address)
print(address)
print('Total file size {} Kilobytes'.format(f'{total/(1024):,.2f}'))
