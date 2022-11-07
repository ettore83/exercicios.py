#game, make a program that the computer "thinks" of an integer number between 0 and 5 and the user tries to figure out
import random
lista = [0,1,2,3,4,5]
sort = random.choice(lista)
print('<>'* 20)
print('\033[1;33;44mi will think of a number from 0 to 5,try to guess\033[m  ')
print('<>'* 20)
n = int(input('type the number : '))
if n == sort:
    print('voce venceu')
else:
    print('voce perdeu tente novamente')
print('numero sorteado foi {}'.format(sort))