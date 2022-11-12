#program to read 2 numbers and display a menu of options
n1 = int(input('leia o primeiro numero: '))
n2 = int(input('leia o segundo numero: '))
option = 0
while option != 5:
    print('''        [ 1 ] SOMA
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NUMEROS
        [ 5 ] SAIR DO PROGRAMA''')
    option = int(input('escolha sua opcao? '))
    if option == 1:
         print('A soma dos numeros e {}'.format(n1+n2))
    elif option == 2:
         print(' a multiplicacao dos numeros e{}'.format(n1 * n2))
    elif option == 3:
        if n1 > n2:
            print('o maior numero e {}'.format(n1))
        elif n2 > n1:
            print('o maior numero e {}'.format(n2))
        else:
            print('os numeros sao iguais ')
    elif option == 4:
        novo1 = int(input('digite um novo numer: '))
        n1 = novo1
        novo2 = int(input('digite um segundo numer: '))
        n2 = novo2
    elif option == 5:
        print('fim do programa')
    else:
        print('informacao invalida')
        print('Tente novamente')