#check if we can make a triangle ,and whith kind of triangle
l1 = float(input('type the first side of triangle: '))
l2 = float(input('type the second side of triangle: '))
l3 = float(input('type the tirth side of triangle: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    #we use ,end=''to extend frase together with another print
    print('we can make a triangle ',end='')
    if l1 == l2 == l3:
        print('3 equal sides\033[1;34;40mEQUILATERO\033[m')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('2 equal sides \033[1;34;43mISOSCELES\033[m')
    elif l1 != l2 or l2 != l3 or l1 != l3:
        print('3 diferent sides \033[1;32;42mESCALENO\033[m')
else:
    print('\033[1;34;41mWe cannot make a triangle\033[m')