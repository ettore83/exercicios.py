#check if we can make a triangle
s1 = float(input('type of segment \033[1;31;40m1\033[m: '))
s2 = float(input('type of segment \033[1;32;40m2\033[m: '))
s3 = float(input('type of segment \033[1;33;40m3\033[m: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('\033[1;32;40mthe segments can make triangle\033[m')
else:
    print('\033[1;31;40mthe segments can not make a triangle\033[m')