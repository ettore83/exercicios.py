#program make the sum the multiple of 3
soma = 0
count = 0
for c in range(1,501,2):
    if c % 3 == 0:
        count = count + 1#count+=1
        soma = soma + c #soma+=c
print('the summ of this count is {} with {} numbers'.format(soma,count))