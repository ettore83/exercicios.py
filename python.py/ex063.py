#sequencial fibonacci
print('-'*30)
n = int(input('how much terms you want show? '))
print('-'*30)
t1 = 0
t2 = 1
print('-'*30)
print('{} - {}'.format(t1,t2), end='')
cont = 3 #contador comeca no tres pois os dois primeiros termos ja sao definidos. 
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')
