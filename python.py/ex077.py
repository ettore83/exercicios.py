#program for check a tupla and display yours vowels
tupla = (str(input('digite a palavra: ')),str(input('digite a palavra: ')),str(input('digite a palavra: '))
,str(input('digite a palavra: ')),str(input('digite a palavra: ')),str(input('digite a palavra: ')),
str(input('digite a palavra: ')),str(input('digite a palavra: ')),str(input('digite a palavra: ')),
str(input('digite a palavra: ')))
for i in tupla:
    print(f'\nna palavra {i} temos ',end = '')
    for letra in i:
        if letra in 'aeiou':
            print(letra,end = '')