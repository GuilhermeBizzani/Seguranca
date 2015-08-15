import math

__author__ = 'Guilherme'

file = open('Vigen.txt', 'rb')
leitura = file.read()

#print(leitura)

print("Bem vindo ao criptografador de Vigenere!")
ent = ''
while (ent != 0):
    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    chave = input('Digite a chave: ')

    #qnt = math.ceil(len(leitura) / len(chave))
    #for i in range(1, qnt):
    #    chav = chav + chave
    #print('Chav: ' + chav)



    saida = open('Vigen.txt','wb')
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

