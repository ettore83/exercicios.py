#working with matriz
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'type the numeber for [{l+1}, {c+1}]: ')) #comecando na linha 1 coluna 1
print('-*-' * 10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end = '')
    print()