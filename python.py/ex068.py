#(odd or even game)
import random
cont = 0
while True:
    v = int(input('type a value between 1 - 10 : ')) #we have 10 fingers
    x = str(input('type your choice [I / P]:')).upper()
    lista = [1,2,3,4,5,6,7,8,9,10]
    sort = random.choice(lista)
    s = sort + v
    if s % 2 == 0:
        if x == 'P':
            print('\033[31mYOU WON\033[m your oponent played {}'.format(sort))
            cont += 1
        else:
            print('YOU LOST')
            break
    else:
        if x == 'I':          
            print('\033[31mYOU WON\033[m your oponent played {}'.format(sort))
            cont += 1
        else:
            print('YOU LOST')
            break
print('we finished with {} wins'.format(cont))