#program that checks whith number is greater and whith is smaller
n1 = int(input('type the first number: '))
n2 = int(input('type the second number: '))
if n1 > n2:
    print('\033[1;31;40mthe first number is greater\033[m')
elif n2 > n1:
    print('\033[1;31;40mthe second number is greater\033[m')
else:
    print('\033[1;35;40mos valores sao iguais\033[m')
    