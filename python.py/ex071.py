#program to distribuity your money in cedules 100 , 50 , 20 ,5 , 1
ced = 100
troca = 0
cont = 0
money = int(input('how much money do you want ? R$'))
troca = money
while True:
    if troca >= ced:
        troca -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'total de {cont} cedulas de r$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 5
        elif ced == 5:
            ced = 1
        cont = 0
        if troca == 0:
            break
print('finish')
