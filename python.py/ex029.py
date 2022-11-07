#program to check if the car pass out of velocity
#only 1 if we call simple condicion
velocity = float(input('type velocity of the car: '))
#check if velocity pass out 80KM for hours
penalty = (velocity - 80) * 7
if velocity > 80:
    print('you got a penalty of ${:.2f}'.format(penalty))
else:
    print('you are in good velocity')
print('\033[1;33;44mhave a good day,Drive safety')