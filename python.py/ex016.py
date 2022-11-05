#make a program that reads the float number and transform the number in integer 
#import math
from math import trunc
numero = float(input('type the float number: '))
#1 way is format directly 
#print('the number is {:.0f}'.format(numero))
#2 way using a metod truncation we have to import math
print('the number typed is:{} , the number converted is: {}'.format(numero,trunc(numero)))
#3 way using insted of import all librery fro math,i need only import the metod to be used