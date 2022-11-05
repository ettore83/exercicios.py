#program receive the value of product and made the calculation in porcentagen of descont
#type the price of product
produto = float(input('type the value of product $: '))
#the calculation was made it with 5% of descont and directly,
#descont = produto - (produto*5/100)
#another way is if im doing with other variable
porc = produto*30/100
desconto = produto - porc
print('the value of product is {},and the final price with descont is {}'.format(produto,desconto))