#dictionaries multiple
from datetime import datetime
work = {} #create a dictionarie
work['nome'] = str(input('Nome: ')) #asking the user a name
nasc = int(input('ano de nascimento: ')) #criando uma variavel solicitando o ano de nascimento 
work['idade'] = datetime.now().year - nasc #calculando a idade e ja acrescentando no dicionario
work['ctps'] = int(input('n Carteira de trabalho,(0 nao tem): '))
if work['ctps'] != 0: #colocando uma condicao para continuar o dicionario
    work['contratacao'] = int(input('Ano da Contratacao: '))
    work['salario'] = int(input('salario: '))
    work['aposentadoria'] = work['idade'] + ((work['contratacao'] + 35) - datetime.now().year)
print('='* 20)
for k, v in work.items():
    print(f'{k} tem o valor {v}')