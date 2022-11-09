#program that checks the age of user and tell him if it is time to do army of not
from datetime import date
year = int(input('type the date of your birth: '))
y = date.today().year
age = y - year
if age < 18:
    print('sua idade e {} e falta {} para alistamento'.format(age,18 - age))
    print('voce tem que se alistar no ano de {}'.format(y + (18 - age)))
else:
    print('ja passou o tempo ')
    