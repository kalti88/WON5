import email.utils


def check_mail(mail):
    global extension, domain
    controll = True
    m = email.utils.parseaddr(mail)[1]
    cntr = 0
    for lett in m:
        if lett == '@':
            cntr += 1
    if cntr > 1:
        controll = False
    if '@' not in m:
        controll = False
    else:
        user = m.split('@')[0]
        cntr1 = 0
        for lett in m.split('@')[1]:
            if lett == '.':
                cntr1 += 1
        if cntr1 > 1:
            controll = False
        else:
            if '.' in m.split('@')[1]:
                domain = m.split('@')[1].split('.')[0]
                extension = m.split('@')[1].split('.')[1]
            else:
                controll = False
            for i in user:
                if not (i.isalpha() or i.isnumeric() or i in ('-', '_', '.')):
                    controll = False
            if (user[0] in ('-', '_', '.')) or (user[-1] in ('-', '_', '.')):
                controll = False
            if not domain.isalpha():
                controll = False
            if len(extension) > 3 or not extension.isalpha():
                controll = False
    return controll


l = []
n = int(input())
i = 1
while i <= n:
    read = str(input())
    if check_mail(read):
        l.append(read)
    i += 1

for e in l:
    print(e)

