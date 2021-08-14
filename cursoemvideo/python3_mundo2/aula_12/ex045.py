from random import choice
print('-=' * 19)
print('\033[1;31mVamos jogar pedra, papel ou tesoura!!!\033[m')
print('=-' * 19)
player = str(input('Escreva a sua escolha: ')).strip().lower()
c1 = str('Pedra').lower()
c2 = str('Papel').lower()
c3 = str('Tesoura').lower()
comp = [c1, c2, c3]
npc = choice(comp)
if player != c1 and player != c2 and player != c3:
    print('Escolha uma opção válida! (Pedra, Papel ou Tesoura)')
else:
    print('O PYSábio escolheu: {}'.format(npc))
    if player == c1 and npc == c2:
        print('O PYSábio ganhou!')
    elif player == c1 and npc == c3:
        print('Voce ganhou!')
    elif player == c2 and npc == c1:
        print('Voce ganhou!')
    elif player == c2 and npc == c3:
        print('O PYSábio ganhou!')
    elif player == c3 and npc == c1:
        print('O PYSábio ganhou!')
    elif player == c3 and npc == c2:
        print('Voce ganhou!')
    else:
        print('Empate!')
