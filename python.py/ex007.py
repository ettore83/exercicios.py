#make a program to display the average of score
n1 = float(input('type the first score: '))
n2 = float(input('type the second score: '))
med = (n1 + n2)/2
#as always first the way with variable
print('the first score is {:.1f},the second score is {:.1f}, the average in between {:.1f} '.format(n1 , n2 , med))
# now the calculation directly in print
#print('first score:{} , second score:{} ,average:{}',format(n1 , n2 , ((n1 + n2)/2))

