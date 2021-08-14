nota1 = float(input('Escreva a primeira nota: '))
nota2 = float(input('Escreva a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Voce teve uma media de {:.1f}. Voce foi \033[1;31mREPROVADO'.format(media))
elif 7 > media >= 5:
    print('Voce teve uma media de {:.1f}. Voce está em \033[1;34mRECUPERAÇÃO'.format(media))
else:
    print('Voce teve uma media de {:.1f}. Voce foi \033[1;32mAPROVADO!\033[m Parabens!!!'.format(media))
