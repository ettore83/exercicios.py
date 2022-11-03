#make the program to read a number and show its predecessor and its successor
n = int(input('type the number to check: '))
a = n - 1 #variable a to predecessor
p = n + 1 #variable p to successor
print('the number typed was {} the number predecessor it is {} and the number successor it is {}'.format(n , a , p))
#we can do directly in funcion print
print('the number typed was {} the number predecessor it is {} and the number successor it is {}'.format(n , n-1 , n+1))