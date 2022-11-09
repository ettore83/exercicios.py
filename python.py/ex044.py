#program simulated when you go to shop or store to buy itens
cash = float(input('type the value of purchases '))
print('''check your choices of payment:
[ 1 ] buy cash or check,10% descont
[ 2 ] pay by card,5% descont
[ 3 ] pay in 2x times on card
[ 4 ] 3x or more on card,20% taxes''')
option = int(input('type your choice: '))
if option == 1:
    cash1 = cash - ((cash * 10)/100)
    print('your purchases are {:.2f},and your new price with descont is {:.2f}'.format(cash,cash1))
elif option == 2:
    card1 = cash - ((cash * 5)/100)
    print('your purchases are {:.2f},and your new price with descont is {:.2f}'.format(cash,card1))
elif option == 3:
    print('your purchases are {:.2f},and you will pay in 2x times of {:.2f} on card'.format(cash,cash / 2))
elif option == 4:
    times = int(input('type how many times you want to pay'))
    total = cash + ((cash * 20) / 100)
    print('your purchases are {:.2f},and you will pay in {} times of {:.2f} on card'.format(cash,times,total / times))
else:
    print('\033[1;31;40mINVALID CHOICE\033[m')