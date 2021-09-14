from urllib import request
try:
    site = request.urlopen('https://www.abola.pt/')
except:
    print('\033[1;31mO site não está acessivel...\033[m')
else:
    print('\033[1;33mO site esta acessivel para leitura.\033[m')

