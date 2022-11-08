#checking if the year is bissexto 
from datetime import date
y = int(input('\033[1;33;44mtype the year you want check and press 0 if you want the current year: \033[m'))
if y == 0:
    y = date.today().year
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('the year you choice is {} and it is \033[1;33;44mbissexto\033[m'.format(y))
else:
    print('the year you choice is {} and it is not a bissexto year'.format(y))
    