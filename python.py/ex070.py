#program register product and prize and after display the most value and how much
total = acima = barato = cont = nome = 0
while True:
    produto = str(input('type the item: '))
    price = float(input('type the price: '))
    cont += 1
    total += price
    if price > 1000:
        acima += 1
    if cont == 1 or price < barato :
        barato = price
        nome = produto
   # ask = ' '
   # while ask not in 'YN':
    ask = str(input('do you want continue: [Y/N]')).strip().upper()[0]
    if ask == 'N':
        break
print (f'o total gasto foi {total},{acima} produtos acima de 1000 o preco mais barato foi {nome} no valor de  {barato}' )