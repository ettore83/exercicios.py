#program to do factorial number
n = int(input('type the factorial number: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c),end='')
    print(' x 'if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('o fatorial de {} e {}'.format(n,f))