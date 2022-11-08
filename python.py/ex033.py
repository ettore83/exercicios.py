#check with one is greater and with one is lower value
n1 = int(input('\033[1;33;44mtype of the number \033[m'))
n2 = int(input('\033[1;34;45mtype of the number \033[m'))
n3 = int(input('\033[1;35;46mtype of the number \033[m'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('the lower value is {}'.format(menor))
print('the greater value is {}'.format(maior))
