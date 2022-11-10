#program to read 6 integer number and make the sum of only if the number is pair
soma = 0
cont = 0
for c in range(1,7):
    n = int(input('type the number {}:'.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print('the sum of the pair numbers is {} and was counting {} numbers'.format(soma,cont))