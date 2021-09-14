def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} golo(s) no campeonato.')


# Programa principal
nome = str(input('Nome do jogador: ')).strip().capitalize()
golos = str(input('Numero de golos: ')).strip()
if golos.isnumeric():
    golos = int(golos)
else:
    golos = 0
if nome == '':
    ficha(gol=golos)
else:
    ficha(nome, golos)
