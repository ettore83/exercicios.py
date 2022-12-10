#aprimorando o desafio ex093
times = [] #add this lista
dic = {}
partidas = []

while True:
    dic.clear()  #apagar o dic antes de ler os dados dele,pq a cada laco eu vou ler os dados de um mesmo jogador
    dic['nome'] = str(input('NOME: '))
    jogos = int(input(f'QUANTAS PARTIDAS {dic["nome"]} JOGOU?: '))
    partidas.clear()  #esvaziar os dados da partida antes de ler. senao o resultado concatena ou acumula os anteriores
    for c in range(0, jogos):
        partidas.append(int(input(f'quantos gols na partida {c+1}: '))) 
    dic['gols'] = partidas[:] # para passar a lista partida dentro do dicionario(obs: [:])
    dic['total'] = sum(partidas)
    times.append(dic.copy()) #pegar o dic e ler dentro do times,por ser dicionario tem q usar o copy
    while True:
        r = str(input('quer continuar?[Y/N]: ')).upper()[0]
        if r in 'YN':      #parte de validacao
            break
        print('resposta errada tente novamente')
    if r == 'N':
        break
#ate aqui o codigo vai coletar as informacoes ,e depois dessa linha o codigo ira mostrar
print('=' * 40) #codigo abaixo vai imprimir o cabecalho.
print('COD ',end = '')
for i in dic.keys():
    print(f'{i:<15}',end = '')
print() # faz com que va para linha de baixo
print('=' * 40)  
for k, v in enumerate(times):    #por ser lista usa enumerate,dicionario usa .items
    print(f'{k:>3} ',end = '')   #vai imprimir os indices 0,1,2,3 se quiser comecar do 1 coloca (k+1)
    for d in v.values():
        print(f'{str(d):<15}',end = '')
    print()
print('=' * 40)
while True:
    busca = int(input('qual jogador voce que consultar? [999] para o programa '))
    if busca == 999:
        break
    if busca >= len(times):
        print(f'ERRO nao existe jogador com codigo {busca} ')
    else:
        print(f'-- os dados do jogador {times[busca]["nome"]}: ')
        for i, g in enumerate(times[busca]['gols']):
            print(f'    no jogo {i+1} fez {g} gos')
    print('=' * 40)
print('-- PROGRAMA ENCERRADO --')