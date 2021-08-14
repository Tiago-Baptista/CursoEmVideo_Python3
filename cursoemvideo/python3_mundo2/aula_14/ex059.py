opção = 0
while opção != 1 and opção != 2 and opção != 3 and opção != 5:
    n = float(input('Escreva um numero: '))
    n1 = float(input('Escreva outro numero: '))
    print('''Escolha o que fazer com esses dois numeros:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair do programa''')
    opção = int(input('Sua opção: '))
    if opção == 1:
        soma = n + n1
        print(' A soma é igual a {}'.format(soma))
    elif opção == 2:
        multi = n * n1
        print('A multiplicação desses dois numeros é {}'.format(multi))
    elif opção == 3:
        if n < n1:
            print('O numero maior é {}'.format(n1))
        elif n > n1:
            print('O numero maior é {}'.format(n))
        else:
            print('Os dois numeros são iguais')
    elif opção == 4:
        while opção != 1 and opção != 2 and opção != 3 and opção != 5:
            n = float(input('Escreva um numero: '))
            n1 = float(input('Escreva outro numero: '))
            print('''Escolha o que fazer com esses dois numeros:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair do programa''')
            opção = int(input('Sua opção: '))
            if opção == 1:
                soma = n + n1
                print(' A soma é igual a {}'.format(soma))
            elif opção == 2:
                multi = n * n1
                print('A multiplicação desses dois numeros é {}'.format(multi))
            elif opção == 3:
                if n < n1:
                    print('O numero maior é {}'.format(n1))
                elif n > n1:
                    print('O numero maior é {}'.format(n))
                else:
                    print('Os dois numeros são iguais')
            elif opção == 5:
                print('Acabou')
            else:
                print('Escolha uma opção válida!')
    elif opção == 5:
        print('Acabou')
    else:
        print('Escolha uma opção válida!')
        while opção != 1 and opção != 2 and opção != 3 and opção != 5:
            n = float(input('Escreva um numero: '))
            n1 = float(input('Escreva outro numero: '))
            print('''Escolha o que fazer com esses dois numeros:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair do programa''')
            opção = int(input('Sua opção: '))
            if opção == 1:
                soma = n + n1
                print(' A soma é igual a {}'.format(soma))
            elif opção == 2:
                multi = n * n1
                print('A multiplicação desses dois numeros é {}'.format(multi))
            elif opção == 3:
                if n < n1:
                    print('O numero maior é {}'.format(n1))
                elif n > n1:
                    print('O numero maior é {}'.format(n))
                else:
                    print('Os dois numeros são iguais')
            elif opção == 5:
                print('Acabou')
            else:
                print('Escolha uma opção válida!')
