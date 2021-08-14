numero = int(input('Escreva um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
   print('A conversão de {} para Binário é: {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
   print('A conversão de {} para Octal é: {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
   print('A conversão de {} para Hexadecimal é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Escolha uma opção correcta!!!')
