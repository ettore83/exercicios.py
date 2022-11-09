#program to calcutation o IMC = peso / (altura x altura)
peso = float(input('type the weight: '))
altura = float(input('type the height: '))
imc = peso / (altura * altura)
print('imc {:.2f}'.format(imc),end='')
if imc <= 18.5:
    print('\033[1;30;40mAbaixo do peso\033[m')
elif imc <= 25:
    print('\033[1;32;40mPeso ideal\033[m')
elif imc <= 30:
    print('\033[1;34;40mSobrepeso\033[m')
elif imc <= 40:
    print('\033[1;31;40mObesidade\033[m')
else:
    print('\033[1;34;40mObesidade morbida\033[m')
    