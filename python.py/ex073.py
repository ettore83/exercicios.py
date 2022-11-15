#work with tuplas
times = ('Palmeiras','Internacional','Flamengo','Fluminense','Corinthias','Athetico-PR'
,'Atletico-MG','America-MG','Goias','Santos','Bragantino','Botafogo'
,'Sao Paulo','Ceara','Fortaleza','Curitiba','Cuiaba'
,'Avai','Aletico Goianiense','Juventude')
print('*' * 100)
print(f'list of teams of Brasileirao {times}')
print('*' * 100)
print(f'the first 4 who will going to Libertadores {times[:4]}')
print('*' * 100)
print(f'the last four who going to low division {times[-4:]}')
print('*' * 100)
print(f'lista ordered alphabetic {sorted(times)}')
print('*' * 100)
print(f'o corinthias estan na {times.index("Corinthias")+1}ª posicao')