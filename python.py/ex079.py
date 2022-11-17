# working with list
lista = []
while True:
    n = int(input('type the number: '))
    if n not in lista:
        lista.append(n)
        print('number successfully added')
    else:
        print('this number already exist')
    r = str(input('do you want continue? [Y/N]'))
    if r in'nN':
        break
lista.sort()
print(lista)