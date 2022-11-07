#program to checking string
frase = str(input('type any phrase: ')).upper().strip()
print('there are {} in the phrase'.format(frase.count('A')))
print('the first one are in position {}'.format(frase.find('A') - frase.find(' ')))
print('the last one show up in position {}'.format(frase.rfind('A')+1))
