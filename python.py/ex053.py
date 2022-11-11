#program identify if the frase is a PALINDROMO,it is mean if we can read as the same 
#like apos a sopa , a sacada da casa,a torre da derrota,o lobo ama o bolo,repaper in english
frase = str(input('enter a frase: ')).strip().upper()
separa = frase.split()
print(separa)
junta = ''.join(separa)
print(junta)
#another way to do this exercicio is ,without use the for
#inverso = junta[::-1]
inverso = ''
for c in range(len(junta)- 1 ,- 1 ,- 1):
    inverso += junta[c]
print(inverso)
if inverso == junta:
    print('this is a PALINDROMO')
else:
    print('this is not a PALINDROMO')