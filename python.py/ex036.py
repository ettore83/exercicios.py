#program for borrow money to buy a house
casa = float(input('Type the value of house : '))
payment = float(input('type the value of payment : '))
years = int(input('type how many years you want pay the house: '))
#transformed y to month
prestacao = casa/(years*12)
#checking if the user can pay the loan ,if the amount cannot exced 30%
verificacao = (payment * 30) /100
if verificacao < prestacao:
    print('the value of house is {:.2f},and you will pay {:.2f}for month'.format(casa,prestacao))
    print('\033[1;31;40myour bank loan was disapproved\033[m')
else:
    print('the value of house is {:.2f},and you will pay {:.2f}for month'.format(casa,prestacao))
    print('\033[1;32;40myour bank loan was approved\033[m')