#checking the number 
number = int(input('type the number: '))
uni = number//1 % 10
dez = number//10 % 10
sen = number//100 % 10
mil = number//1000 % 10
#we can als take 2 number ,than we can %100 put 2 0
print('analising the number the un is {},the dez is {},the sen is {},the mil is {}'.format(uni,dez,sen,mil))
