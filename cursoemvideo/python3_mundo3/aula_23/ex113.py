def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu não informar os dados.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero real. \033[m')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu não informar os dados.')
            return 0
        else:
            return f


num = leiaint('Digite um numero inteiro: ')
num1 = leiafloat('Digite um numero real: ')
print(f'Digitou o numero inteiro {num} e o numero real {num1}')
