#program computer ll choice one number and the player have to find out
import random
lista = [0,1,2,3,4,5,6,7,8,9,10]
sort = random.choice(lista)
tot = 1
print('<>'* 20)
print('\033[1;33;44mI will think of a number from 0 to 10,try to guess\033[m  ')
print('<>'* 20)
n = int(input('type your choice: '))
while n != sort:
    if sort > n:
        print('more , try again')
    elif sort < n:
        print('less , try again')
    n = int(input('type your choice: '))
    tot = tot + 1
print('was necessary {} tryings for to be right'.format(tot) )

#anothe way
#from random import randint
#computador = randint(0,10)
#print('sou seu computador ... acabei de pensar em um numero entre 0 e 10')
#print('sera que consegue adivinhar?')
#acertou = False
#paplite = 0
#while not acertou:
    #jogador = int(input('qual e o seu palpite'))
    #palpite += 1
    #if jogador == computador:
        #acertou = True
    #else:
        #if jogador < computador:
            #print('mais.. tente mais uma vez')
        #elif jogador > computador:
            #print('menos...tente mais uma ')
#print('acertou com{} palpites'.format(palpite))