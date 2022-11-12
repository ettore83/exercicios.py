#checking validationfor sexo male and female
sexo = str(input('type the sexo [M / F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('type the sexo [M / F]: ')).strip().upper()[0]
print('sexo {} enter successfully'.format(sexo))