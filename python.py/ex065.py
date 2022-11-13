#make a program read many numbers and make a good analysis,like the greater,the lower
#v = int(input('type a value: '))
#r = str(input('do you want continue? [Y/N]')).upper()
r = 'Y'
s = t = ma = me = 0
while r in 'Yy':    
    v = int(input('type a value: '))
    t += 1
    s += v
    if t == 1:
        ma = me = v
    else:
        if v > ma:
            ma = v
        if v < me:
            me = v
    r = str(input('do you want continue? [Y/N]')).upper().strip()[0]
print('o total de vezes foi {} e a media foi{:.2f} o maior numero {} e o menor numero foi {}'.format(t,s / t,ma,me))