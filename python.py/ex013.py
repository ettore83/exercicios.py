#the program  read how much the worker receive and made the calculation with 15% of increasing
payment = float(input('type the value of payment: '))
#15% of increase
increase = payment + (payment*15/100)
print('the payment is:${},and the new payment with increase is:${}'.format(payment,increase))