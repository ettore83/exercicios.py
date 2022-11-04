#make a program to read the value in meters and convert them in centimeters ans milimeters
#take the meters of the user
medida = float(input('type the number of the meters to be converted: '))
#doing with variable
cm = medida * 100
mm = medida * 1000
print('the value is:{:.0f}, the mesurament conversion in centimeters is:{:.0f},and in milimeters is:{:.0f}'.format(medida,cm,mm))
