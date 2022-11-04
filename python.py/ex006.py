#create an algorithm that reads a number and displays double, triple and square root
n = float(input('type number to check: '))
#one way to solve this is,with variable
# show the double of the number
d = n * 2
# show the triple of the number
t = n * 3
# show the square root
r = n ** (1/2)
#show as a print
print('the number is:{},\nthe double of the number is:{},\nthe triple of the number is:{}\n and the square root of the number is:{}'.format(n , d , t , r))
#another way is direct in print
#formating number of caracter
print('number{:.2f},double number{:.2f},triple number{:.2f},square root number{:.2f}'.format(n,n*2,n*3,n ** (1/2)))

