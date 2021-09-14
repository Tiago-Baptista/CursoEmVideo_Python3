try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except:                                                  #generico
 #   print('Infelizmente tivemos um problema!')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados inseridos.')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero.')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, obrigado!')

