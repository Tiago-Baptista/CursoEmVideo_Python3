frase = 'Curso em Video Python'
print(len(frase))
print(frase[3])
print(frase[:5])
print(frase[15:])
print(frase[9:14])
print(frase[9:14:2])
print(frase[9::3])
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.split())
print('-'.join(frase))
