__author__ = 'Guilherme'


print("Bem vindo ao criptografador de Ceasar!")
ent = 1
while (ent != 0):

    print("Digite o nome do programa de entrada COM A EXTENSAO!")
    arq = input('->')

    file = open(arq, 'rb')
    leitura = file.read()
    file.close()

    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    chave = int(input('Digite a chave: '))
    file2 = open('SaidaCeasar.enc', 'wb')
    if(ent == 1):
        a = []
        for x in leitura:
            y = (x + chave)%256
            a.append(y)
        file2.write(bytes(a))


        #print ('Frase Original: ' + leitura )
        #print ('Frase Criptografada: ' + a )

    if (ent == 2):
        a = []
        for x in leitura:
            y = (x - chave)%256
            a.append(y)
        file2.write(bytes(a))

        #print ('Frase Original: ' + leitura )
        #print ('Frase Descriptografada:' + a)
    file2.close()
print('tchau')