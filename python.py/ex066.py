#program using break and while True
soma = qtd = 0
while True:
    valor = int(input('type the number 999 to stop : '))
    if valor == 999:
        break
    soma += valor
    qtd += 1
print(f'we typed {qtd} numbers and {soma} was the sum.')