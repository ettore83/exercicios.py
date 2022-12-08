#cadastro de pessoas usando dicionarios e listas
galera = list()
pessoa = dict()
med = tot = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Type the name of person: '))
    while True:
        pessoa['sexo'] = str(input('Type the sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'M/F':
            break
        print('wrong answer try again.')
    pessoa['idade'] = int(input('Type your age: '))
    tot += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Do you want continue: [Y/N]')).upper()[0]
        if r in 'YN':
            break
        print('wrong answer try again.')
    if r == 'N':
        break
print('+' * 30)
med = tot / len(galera)
print('+' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas registradas.')
print(f'B) e {med:5.2f} e a media das idades ')
print(f'C) as mulheres cadastradas foram: ',end ='' )
for c in galera:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ', end = '' )
print()
print('D) lista das pessoas acima da media: ')
for c in galera:
    if c['idade'] >= med:
        print('     ',end = '')
        for k, v in c.items():
            print(f' {k} recebe {v} ', end = '' )
        print()
print('** encerrando **')