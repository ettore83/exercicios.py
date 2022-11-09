#program to average of scores
n1 = float(input('type the first score: '))
n2 = float(input('type the second score: '))
nf = (n1 + n2)/2
if nf >= 7:
    print('\033[1;32;40maluno aprovado\033[m')
elif nf >= 5 and nf < 7:
    print('\033[1;33;44maluno em recuperacao\033[m')
else :
    print('\033[1;31;44maluno reprovado\033[m')