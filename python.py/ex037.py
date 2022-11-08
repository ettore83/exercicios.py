#program to transfor number integer in binario,octa,hexadecimal
n = int(input('type the integer number '))
print('''escolha uma das bases para conversao:
    [ 1 ]converter para binario
    [ 2 ]converter para octal
    [ 3 ]converter para hexadecimal''')
option = int(input('choose your option: '))
if option == 1:
    print('the number was{} and the conversion was: {}'.format(n,bin(n)[2:]))
elif option == 2:
    print('the number was{} and the conversion was: {}'.format(n,oct(n)[2:]))
elif option == 3:
    print('the number was{} and the conversion was: {}'.format(n,hex(n)[2:]))
else:
    print('option invalid')