#multiplication table with looping
n = int(input('type the number of you want multiplication table: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n, c , n*c))
    