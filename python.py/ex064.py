#programa type many numbers and make the sum of them
n = 0
cont = 0
soma = 0 # we can do like this n = cont = soma = 0
while n != 999:
    n = int(input('type the number and 999 to stop: '))
    cont += 1
    soma += n
print('we make the sum with {} numbers and the total value is {}'.format(cont - 1,soma - 999))
#solucao pra tirar o 999 e solicitar o numero antes do while e solicitar o numero depois do while na ultima linha