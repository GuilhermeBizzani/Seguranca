import math

__author__ = 'Guilherme'

#print(leitura)

fileC = open("chaveVigenere.txt", "rb")
chave = fileC.read()
fileC.close()

print("Bem vindo ao criptografador de Vigenere!")
ent = 1
while (ent != 0):

    print("Digite o nome do programa de entrada COM A EXTENSAO!")
    arq = input('->')

    file = open(arq, 'rb')
    leitura = file.read()
    file.close()

    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    if ent == 0:
        break
    #chave = input('Digite a chave: ')

    file2 = open("ChaveVigenere.txt", "rb")
    chave = file2.read()
    file2.close()

    saida = open('SaidaVigenere.enc','wb')
    a = []
    if(ent == 1):
        cont = 0
        for x in leitura:
            y = (x + int(chave[cont])) % 256
            cont+=1
            if cont == (len(chave)-1):
                cont = 0
            a.append(y)
            #le = ord(leitura[x])
            #ch = ord(chav[x])
            #lee = chr(le + ch)
            #a += lee

        #print('Frase Original: '+ leitura)
        #print('Frase Criptografada: ' + a)
        saida.write(bytes(a))

    if(ent == 2):
        cont = 0
        for x in leitura:
            y = (x - int(chave[cont])) % 256
            cont+=1
            if cont == (len(chave)-1):
                cont = 0
            a.append(y)

        #print('Frase Original: ' + leitura)
        #print('Frase Descriptografada:' + a)
        saida.write(bytes(a))

    saida.close()

print ('tchau')

