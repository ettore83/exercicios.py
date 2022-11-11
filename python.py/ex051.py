#arithmetic progression,PA
t = int(input('type termo: '))
r = int(input('type reason: '))
#calculo para saber o enezimo termo.
decimo = t + (10 - 1) * r
for c in range(t,decimo + r,r):
    print(c,end = '_')