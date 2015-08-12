import math
import random

__author__ = 'Guilherme'

file = open('pg11.txt', 'r')
leitura = file.read()
file.close()

print("escrever")
listC = open("lista.bin", "wb")
print("Arquivo criado com sucesso!")
a = bytes()
aux = []
for i in range(256):
    aux.append(i)
for i in range(256):
    rand = random.randint(0, (len(aux)-1))
    a = a + bytes(list(range(aux[rand], aux[rand]+1)))
    aux.remove(aux[rand])

#a = bytes(list(range(256)))
listC.write(a)
print("Deu")
listC.close()

print("ler")
listR = open("lista.bin", "rb")
print("Arquivo lido com sucesso!")
oi = listR.read()
listR.close()
arq = open("exit.bin", "wb")

for i in oi:
    try:
        print(i)
        print(chr(oi[i]))
    except:
        arq.write(bytes(list(range(i, i+1))))
        print("zoou")
print(len(oi))
a = ''
for i in leitura:
    y = ord(i)

