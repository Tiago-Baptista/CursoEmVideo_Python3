frase = str(input('Escreva uma frase: ')).strip()
x = (frase.upper().count('A'))
y = (frase.upper().find('A')+1)
w = (frase.upper().rfind('A')+1)
print('Nessa frase o A aparece {} vezes'.format(x))
print('Nessa frase o primeiro A aparece na posição {}'.format(y))
print('Nessa frase o ultimo A aparece na posição {}'.format(w))
