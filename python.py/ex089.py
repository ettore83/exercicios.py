#list with classmates scores
lista = []
while True:
    nome = str(input('type the name of student: '))
    nota1 = float(input('type the first score: '))
    nota2 = float(input('type the second score: '))
    media = (nota1 + nota2) / 2 
    lista.append([nome, [nota1, nota2], media])
    r = str(input('do you want register more? [Y/N]'))
    if r in 'nN':
        break
print('-' * 23)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 23)
for i , a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('type the number of register,and(999 to finish): '))
    if opc == 999:
        print('FINALIZANDO....')    
        break
    if opc <= len(lista) - 1:
        print(f'as Notas do aluno {lista[opc][0]} sao {lista[opc][1]}')
print('Always Come back')