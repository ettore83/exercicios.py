#program to read 4 numbers and computer chose ramdom number.
import random
n1 = str(input('type the 1 name: '))
n2 = str(input('type the 2 name: '))
n3 = str(input('type the 3 name: '))
n4 = str(input('type the 4 name: '))
lista = [n1,n2,n3,n4]
sort = random.choice(lista)
print('the name sorted was {}'.format(sort))
