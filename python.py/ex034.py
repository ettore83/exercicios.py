#program for calculation the value of payment and how mauch he have raise
pay = float(input('type the payment: '))
if pay > 1250:
    a = pay + ((pay * 10) / 100)
    print('the increasing was {:.2f}'.format(a))
else:
    b = pay + ((pay * 15) / 100)
    print('the incrasing was {:.2f}'.format(b))