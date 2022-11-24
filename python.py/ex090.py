#working with dictionaries
register = dict()
register['nome'] = str(input('type the name: '))
register['media'] = float(input(f'type the average of {register["nome"]}: '))
if register['media'] >= 7:
    register['status'] = 'Approved'
elif 5 <= register['media'] < 7:
    register['status'] = 'Recovery'
else:
    register['status'] = 'Disapproved'
for k, v in register.items():
    print(f'  -{k} e igual a {v}')