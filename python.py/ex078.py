#checking listas
maior = 0
menor = 0
lista = []
for i in range(0,5):
    lista.append(int(input(f'digite um numero na posicao {i} ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(f'a lista e {lista} ')
print(f'o maior valor e:{maior} ')
for a , v in enumerate(lista):
    if v == maior:
        print(f'{a}...',end = '')
print(f'o menor valor e :')