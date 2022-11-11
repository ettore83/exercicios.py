#program identify if the number is prime number
n = int(input('type the numbe: '))
tot = 0
for c in range(1,n+1):
   if n % c == 0:
       print('\033[33m',end = '-')
       tot += 1 
   else:
       print('\033[31m',end = '-')
   print('{}'.format(c),end = '')  
print('\n\033[mO numero {} foi divizivel {} vezes'.format(n,tot))
if tot == 2:
    print('por isso ele e PRIMO')
else:
    print('por isso ele nao e PRIMO')