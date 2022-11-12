#improve ex 61 ,asking if the user want show diferent termo.
t = int(input('primeiro termo: '))
r = int(input('razao: '))
cont = 0
i = t
total = 0
q = 10
while q != 0:
    total = total + q
    while cont <  total:
        print('{}-'.format(i),end='')
        i += r
        cont += 1
    print('pausa')
    q = int(input('digite quantos termos mais? '))
print('progressao finalizada com{} termos'.format(total))