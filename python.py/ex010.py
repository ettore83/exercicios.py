#program to read how much reais you have in your pocket and convert to how much euro you can get
reais = float(input('type the money you have in your pocket: R$ '))
euro = reais/5.53 #this value is in the date out/2022
print('i have {:.2f} in my pocket and i can buy {:.2f} euros'.format(reais,euro))