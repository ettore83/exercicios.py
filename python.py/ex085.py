#working with list ,using only one list to storage odds and pairs.
lista = [[], []]
for i in range(0,7):
    n = int(input(f'type the {i} number: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Pair values was {lista[0]} ')  
print(f'Odds values was {lista[1]} ')  
