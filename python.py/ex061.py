#PA using while
t = int(input('digite o primeiro termo: '))
r = int(input('digite a razao: '))
contador = 0
i = t
while contador < 10:
    print('{}-'.format(i),end='')
    i += r
    contador += 1
print('fim')