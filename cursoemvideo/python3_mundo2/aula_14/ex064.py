print('\033[33mPara terminar o programa digite \033[1m\033[4m999\033[m')
c = -1
n = 0
soma = -999
while n != 999:
    n = int(input('Escreva um numero inteiro: '))
    c += 1
    soma += n
print('\033[31mForam digitados {} numeros e a sua soma é de {}!'.format(c, soma))
