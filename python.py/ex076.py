#work with tuplas
aniversario = ('Ettore','13/12/1983','Priscila','25/04/1986','Lorenzo','18/08/2015','Vicenzo','15/07/2019','Maria','03/09/1959','Luiz','07/04/1957','Debora','20/10/1977','Bruna','26/10/1981','Miguel','10/05/1996')
print('-' * 40)
print(f'{"DATA DOS ANIVERSARIOS":^40}')
print('-' * 40)
for pos in range(0,len(aniversario)):
    if pos % 2 == 0:
        print(f'{aniversario[pos]:.<30}',end = '')
    else:
        print(f'{aniversario[pos]:>10}')
print('-' * 40)
