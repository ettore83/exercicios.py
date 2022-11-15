#program type the number and add in a tuple
cont = 0
numero = (int(input('type the number: ')),
int(input('type one more number: ')),
int(input('type one more number: ')),
int(input('type one more number: ')))
for n in numero:
    if n % 2 == 0:
        cont += 1
print(numero)
print(f'o numero nove apareceu {numero.count(9)} vezes na minha tupla') 
if 3 in numero:
    print(f'a posicao do primeiro valor 3 foi {numero.index(3)+1}')
else:
    print('o valor 3 nao foi digitado na tupla')
print(f'existem na tupla {cont} numeros pares')