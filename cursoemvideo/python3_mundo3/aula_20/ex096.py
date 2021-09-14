def area(comp, alt):
    a = comp * alt
    print(f'Um terreno com {comp}m de comprimento e {alt}m de largura, tem uma area de {a} metros quadrados.')

#Calcular a area
print('=' * 20)
print('Calculando uma area')
print('=' * 20)
comp = float(input('Comprimento (m): '))
alt = float(input('Largura (m): '))
area(comp, alt)
