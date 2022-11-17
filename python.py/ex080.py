#continuing with lists
lista = []
for i in range(0,5):
    n = int(input('type the number: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posicao {pos} na lista')
                break
            pos += 1
print(f'os valores da lista sao {lista}')