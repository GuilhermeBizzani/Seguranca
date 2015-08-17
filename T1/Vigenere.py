import math

__author__ = 'Guilherme'

#print(leitura)

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
    chave = input('Digite a chave: ')

    #qnt = math.ceil(len(leitura) / len(chave))
    #for i in range(1, qnt):
    #    chav = chav + chave
    #print('Chav: ' + chav)



    saida = open('SaidaVigenere.enc','wb')
    a = []
    if(ent == 1):
        cont = 0
        for x in leitura:
            y = (x + int(ord(chave[cont]))) % 256
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
            y = (x - int(ord(chave[cont]))) % 256
            cont+=1
            if cont == (len(chave)-1):
                cont = 0
            a.append(y)

        #print('Frase Original: ' + leitura)
        #print('Frase Descriptografada:' + a)
        saida.write(bytes(a))

    saida.close()

print ('tchau')

