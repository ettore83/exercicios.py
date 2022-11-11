#program identify greater and the lower weight.
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('type your {} weight:'.format(c)))
    if c == 1:
        maior = peso
        menor = peso 
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} kg e o menor peso foi de {} kg'.format(maior,menor))