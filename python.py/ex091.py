#work with dictionaries
from random import randint
from time import sleep
#new library
from operator import itemgetter
dados = {'jogador 1': randint(1, 6),
         'jogador 2': randint(1, 6),
         'jogador 3': randint(1, 6),
         'jogador 4': randint(1, 6)}
ranking = {}
print('Valores Sorteados')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1),reverse = True)
#the ranking dictionaries become we have to deal with list
print('   Colocacao   ')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)