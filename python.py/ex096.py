#funcoes simples
#funcao que calcule a area de um terreno
def area(larg, comp):
    a = larg * comp
    print(f'Aarea de um terreno {larg} x {comp} e de  {a}m²')
    
    
    
print('calculando a area de um terreno')
print('=' * 20)
l = float(input('Largura (m)'))
c = float(input('Comprimento (m)'))
area(l,c)
