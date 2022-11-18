#checking expression with parentesis
#criando uma lista para colocar os parenteses
lista = []
#solicite ao usuario uma expressao matematica
expr = str(input('digite sua expressao matematica: '))
#fazendo a verredura da expressao identificando os simbolos de parenteses
for simbolo in expr:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('sua expressao esta correta')
else:
    print('sua expressao esta incorreta')
    