#sine,cosine e tangent
import math
angulo = float(input('type the angle of triangle: '))
#have to convert to radians(radiano for angulation in degrees)
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo)) 
print('the angle of {} ,the cos {:.2f} , sen {:.2f} , tang {:.2f}'.format(angulo,cos,sen,tang))