#registering people and yours weight and checking the bigger 
nomes = [] #temporary list
pesos = []
maior = menor = 0
#solicitando ao usuario nome e peso
while True:
    nomes.append(str(input('Type the name of the person: ')))
    nomes.append(float(input('Type the weight of the person: ')))
    if len(pesos) == 0:#se eu nao cadastrei ninguem e sinal q eu n tenho menor nem maior ==0
        maior = menor = nomes[1] #nomes na posicao 0 sao os nomes na posicao 1 sao os pesos 
    else:
        if nomes[1] > maior:
            maior = nomes[1]
        elif nomes[1] < menor:
            menor = nomes[1]
    pesos.append(nomes[:]) #copy of the list
    nomes.clear() #necessary clean 
    r = str(input('Do you want continue [Y/N]: '))
    if r in 'nN':
        break
print(f'voce cadastrou {len(pesos)} pessoas')
print(f'The heavy weight was {maior} the person was ',end ='')
for p in pesos: #para cada pessoa em pesos(nome da lista)
    if p[1] == maior:
        print(f'{p[0]}',end = '')
print(f' o menor peso foi {menor}',end = '')
for p in pesos:
    if p[1] == menor:
        print(f'{p[0]}',end = '')