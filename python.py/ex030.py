#program check if the number is odd or pair
nu = int(input('enter a number: '))
r = nu % 2
if r == 0:
    print('\033[0;33;44m number {} is pair\033[m'.format(nu))
else:
    print('the number {} is odd'.format(nu))