#program to check age of peoaple and we can know if it is a yong or adult person
from datetime import date
menor = 0
maior = 0
y = date.today().year
for c in range (1,8):
    nasc = int(input('type when {} person born: '.format(c)))
    if nasc >= y - 21:
        menor += 1
        #print('the person it is not adult yet')
    else:
        maior += 1
        #print('the person it is an adult')
print('among this 7 persons {} is an adult and {} it is a teenager'.format(maior,menor))