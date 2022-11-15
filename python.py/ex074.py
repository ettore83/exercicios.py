#program that draws five random numbers
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'os valores sorteados foram: ',end ='')
for n in numeros:
    print(f'{n} ',end = '')
print(f'\nthe bigger value was {max(numeros)}')
print(f'the smaller value was {min(numeros)}')