#program to do complete analisys
totage = 0 # for check avarage of the group
old = 0 # for check who are the oldest
new = 0
masc = 0
menor = 0
nomevelho = ''
for c in range(1,5):
    print('\033[31m-----{}PESSOA-----\033[m'.format(c))
    nome = str(input('NAME: ')).strip()
    idade = int(input('AGE: '))
    sexo = str(input('SEXO [M/F] ')).strip().upper()
    if sexo == 'M':
        masc += 1
    elif sexo == 'F':
        if idade < 20:
            menor += 1
    else:
        print('invalid typed')
    totage = totage + idade
    if c == 1 and sexo == 'M':
        old = idade
        nomevelho = nome
        new = idade
    if sexo == 'M' and idade > old:
        old = idade
        nomevelho = nome
print('avarege is {:.2f}, and the oldes is {} and your name is {}'.format(totage/4,old,nomevelho))
print('there are {} womans less than 20 years'.format(menor))