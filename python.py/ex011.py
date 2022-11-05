#the program take the mesure of the wall and make the calculation of your area and how much liters of ink to paint this wall
#take the first mesure of width
width = float(input('type the width of the wall: '))
#take the first mesure of hight
hight = float(input('type the hight of the wall: '))
area = width * hight
ink = area / 2
print('the width is {:.2f} the hight is {:.2f} the area is {:.2f} and we need to paint {:.2f}liters'.format(width,hight,area,ink))