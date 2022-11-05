#1 program to read opposite side of triangle and adjacent side of triangle and make the calculation of hypotenuse
#2 another way is import math
import math
#3 we can also use only ,from math import hypot
co = float(input('opposite side of triangle : '))
ca = float(input('adjacente side of triangle : '))
#3 then we have to take out math on line below 
hi = math.hypot(co,ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)
print('hi of triangle is:{:.2f}'.format(hi))
