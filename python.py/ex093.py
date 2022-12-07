#dictionaries players
dic = {}
partidas = []
cont = 0
dic['nome'] = str(input('NOME: '))
jogos = int(input(f'QUANTAS PARTIDAS {dic["nome"]} JOGOU?: '))
for c in range(0, jogos):
    partidas.append(int(input(f'quantos gols na partida {c}: '))) 
dic['gols'] = partidas[:] # para passar a lista partida dentro do dicionario(obs: [:])
dic['total'] = sum(partidas)
print('+' * 30)
print(dic)
print('+' * 30)
for k, v in dic.items():
    print(f' _ {k} tem o valor {v} ')
print('+' * 30)
print(f'O jogador {dic["nome"]} jogou {jogos} partidas') #podendo usar o len de gols para saber o n de partidas
for i, v in enumerate(dic['gols']):
    print(f'  => Na partida {i} fez {v} gols')
print(f'Foi um total de {dic["total"]} gols'  )
