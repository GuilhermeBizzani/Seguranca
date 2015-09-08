import math
import random

__author__ = 'Guilherme'

'''
print("Criar Listas novas:")
listC = open("lista.bin", "wb")
list2 = open("lista2.bin", "wb")
print("Arquivo criado com sucesso!")
a = bytes()
b = []
aux = []
for i in range(256):
    aux.append(i)
for i in range(256):
    b.append(i)
for i in range(256):
    rand = random.randint(0, (len(aux)-1))
    a = a + bytes(list(range(aux[rand], aux[rand]+1)))
    b[aux[rand]] = len(a)-1
    aux.remove(aux[rand])
listC.write(a)
list2.write(bytes(b))
listC.close()
list2.close()
print("Listas criadas com sucesso")
'''
while 1:

    print("Digite o nome do arquivo de entrada COM A EXTENSAO!")
    arq = input('->')

    file = open(arq, 'rb')
    leitura = file.read()
    file.close()

    file2 = open("ListaSubs.txt", "rb")
    listR = file2.read()
    file2.close()

    file3 = open("ListaSubs.txt", "rb")
    listR2 = file3.read()
    file3.close()

    saida = open('saidaSubs.enc', 'wb')

    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    if ent == 0:
        break

    if(ent==1):
        a = []
        for x in leitura:
            nov = listR[x]
            a.append(nov)

        saida.write(bytes(a))

    if ent==2:
        a = []
        for x in leitura:
            nov = listR2[x]
            a.append(nov)

        saida.write(bytes(a))

    saida.close()
    print("Fim.")