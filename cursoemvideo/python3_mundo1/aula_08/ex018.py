import math
a = float(input('Escreva o valor de um angulo: '))
coseno = math.cos(math.radians(a))
seno = math.sin(math.radians(a))
tangente = math.tan(math.radians(a))
print('Para o angulo de {:.0f}º \nO coseno é {:.3f} \nO seno é {:.3f}  \nA tangente é {:.3f}'.format(a, coseno, seno, tangente))
