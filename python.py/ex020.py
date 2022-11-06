#program to type 4 names and put them in order totaly diferent
import random
n1 = str(input('type the 1 name: '))
n2 = str(input('type the 2 name: '))
n3 = str(input('type the 3 name: '))
n4 = str(input('type the 4 name: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('the order of the presentation will be{}'.format(lista))
#another way is  
"""from random import shuffle
n1 = str(input('type the 1 name: '))
n2 = str(input('type the 2 name: '))
n3 = str(input('type the 3 name: '))
n4 = str(input('type the 4 name: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('the order of the presentation will be{}'.format(lista))"""