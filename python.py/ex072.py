#program read the extensive number
#starting with a tuple
numbers = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito',
'nove','dez','onze','doze','treze','catorze','quinze','dezesseis',
'dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('type the numbe between 0 and 20: '))
    if n >= 0 and n <= 20:
        print(f'you type the number {numbers[n]}')
        break
    