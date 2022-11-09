#program descrive which level the user are
from datetime import date
birth = int(input('\033[1;36;41mtype the date of your birth: \033[m'))
y = date.today().year 
years = y - birth
if years < 9:
    print('the user has {} , and he is \033[1;36;45m MIRIM \033[m'.format(years))
elif 9 <= years < 14:
    print('the user has {} , and he are \033[1;36;45m INFANTIL \033[m'.format(years))
elif 14 <= years < 19:
    print('the user has {} , and he are \033[1;36;45m JUNIOR \033[m'.format(years))
elif 19 <= years < 25:
    print('the user has {} , and he are \033[1;36;45m SENIOR \033[m'.format(years))
else:
    print('the user has {} , and he are \033[1;36;45m MASTER \033[m'.format(years))