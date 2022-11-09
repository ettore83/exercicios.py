#program game:JO KEN PO
import random
from time import sleep
print('''\033[1;32;40myour options
[ 0 ] =  pedra
[ 1 ] =  papel
[ 2 ] =  tesoura\033[m''')
option = int(input('type your choice: '))
print('\033[1;31;40mJO\033[m')
sleep(1)
print('\033[1;32;40mKEN\033[m')
sleep(1)
print('\033[1;33;40mPO!!!\033[m')
lista = [0,1,2]
sort = random.choice(lista)
print('-=' * 20)
if option == 0:
    if sort == 0:
        print('both play Pedra ,Draw')
    elif sort == 1:
        print('you play Pedra and computer play Papel,You Lost')
    else:
        print('you play Pedra and computer play Tesoura,You Won')
elif option == 1:
    if sort == 0:
        print('you play Papel and computer play Pedra,You Won')
    elif sort == 1:
        print('Both play Papel,Draw')
    else:
        print('you play Papel and computer play Tesoura,You Lost')
elif option == 2:
    if sort == 0:
        print('you play Tesoura and computer play Pedra,You Lost')
    elif sort == 1:
        print('you play Tesoura and computer play Papel,You Won')
    else:
        print('Both play Tesoura,Draw')
else:
    print('wrong choice,try again')
    