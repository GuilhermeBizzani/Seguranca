__author__ = 'Guilherme'

file = open('pg11.txt', 'rb')
leitura = file.read()
file.close()


print("Bem vindo ao criptografador de Ceasar!")
ent = ''
while (ent != 0):
    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    chave = int(input('Digite a chave: '))
    file2 = open('outraSaidaaaaa.enc', 'wb')
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
print ('tchau')