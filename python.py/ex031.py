#program make calculation about the travel 
km = float(input('type the distance of travel in KM: '))
far = km * 0.45
near = km * 0.50
print('\033[1;33;44mYou will make a travel of {:.0f}KM\033[m'.format(km))
if km > 200:
    print('the price of travel will be {:.2f}'.format(far))
else:
    print('the price of travel will be {:.2f}'.format(near))