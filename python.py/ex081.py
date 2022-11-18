#lista,how much numbers do you want,put in order,and check if the number 5 are in the list
lista = []
while True:
    lista.append(int(input('type the number: ')))
    r = str(input('Do you want continue? [y/n]: '))
    if r in 'nN':
        break    
if 5 in lista:
    print('the number 5 make part of your list')
else:
    print('the number 5 do not make part of your list')
lista.sort(reverse = True)
print(f'the numbers of the list was {lista} and typed {len(lista)} values')