#program registered user and check how many persons and anothers thinks
adulto = man = mulher = 0
while True:
    print('-' * 15)
    print('CADASTRE UMA PESSOA')
    print('-' * 15)
    i = int(input('type the age of the person: '))
    if i > 18:
        adulto += 1
    s = ' '
    while s not in 'MF':
        s = str(input('type sexo of the person [M/F] ')).strip().upper()[0]
        if s == 'M':
            man += 1
        else:
            if i < 20:
                mulher += 1
    p = ' '
    while p not in 'YN':
        p = str(input('do you want continue ? [Y/N] ')).strip().upper()[0]
    if p == 'N':
        break
print(f'registro encerrado com {adulto} adultos ,{man} foram homens e {mulher} mulher menos de 20')
