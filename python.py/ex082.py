#normal list and after that identify the numbers ods and pair
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('type the number: ')))
    r = str(input('do you want continue [Y/N] '))
    if r in 'nN':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'a lista foi {lista}')
print(f'a lista par foi {pares}')
print(f'a lista par foi {impares}')