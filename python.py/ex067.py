#program read the number and display multiplication table
#first way
#v = 0
#while v >= 0:
#    v = int(input('type the number: '))
#    for i in range (1,11):
#        print('{} x {} = \033[1;31;40m{}\033[m'.format(v,i,i * v))
#second way
while True:
    v = int(input('type the number to multiplication table: '))
    print('-' * 30)
    if v < 0:
        break
    for i in range(1,11):
        print(f'{v} x {i} = {v*i}')
    print('-' * 30)
print('the program end ')