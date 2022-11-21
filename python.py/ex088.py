#sorteio dos numeros mega sena
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('    joga na mega sena    ')
print('-' * 30)
n = int(input('quantos jogos voce quer fazer? '))
tot = 1 #comeca com 1 senao vai ser impressa uma lista a mais
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {n} JOGOS','-=' * 3)
for i ,l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, 'BOA SORTE','-=' * 3)