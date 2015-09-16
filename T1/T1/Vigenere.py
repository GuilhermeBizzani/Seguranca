__author__ = 'Guilherme'

import math


file = open("outputs/pg11", 'rb')
leitura = file.read()
file.close()

while len(chave) < 4:

    a = []

    cont = 0
    cont = 0
    for x in leitura:
        y = (x - int(chave[cont])) % 256
        cont+=1
        if cont == (len(chave)-1):
            cont = 0
        a.append(y)



print ('tchau')

