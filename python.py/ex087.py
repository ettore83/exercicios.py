#matriz e analise de matriz
cont_maior = tc = ml = 0
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'type the numeber para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            cont_maior += matriz[l][c]
for l in range(0 ,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end = '')
    print()
print(f' a soma dos numeros pares foram: {cont_maior}')
for l in range(0, 3):
    tc += matriz[l][2]
print(f'a soma da terceira coluna e de {tc} ')
for c in range(0, 3):
    if c == 0:
        ml = matriz[1][c]
    elif matriz[1][c] > ml:
            ml = matriz[1][c]
print(f'o maior valor da segunda linha e {ml}')