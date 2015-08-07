__author__ = 'Guilherme'

file = open('entrada.txt', 'r')
leitura = file.read()

print(leitura)

print("Bem vindo ao primeiro criptografador!")
ent = ''
while (ent != 0):
    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    chave = int(input('Digite a chave: '))
    if(ent == 1):
        a = ''
        for x in leitura:
            y = ord(x)
            if (y < chave):
                aux = y - chave
                y = 256 + aux
            else:
                z = chr(y - chave)
            a = a+z

        print ('Frase Original: ' + leitura )
        print ('Frase Criptografada: ' + a )

    if (ent == 2):
        a = ''
        for x in leitura:

            y = ord(x)
            if(y > 256-chave):
                y = (y + chave)%256
            else:
                z = chr(y + chave)

            a = a+z

        print ('Frase Original: ' + leitura )
        print ('Frase Descriptografada:' + a)


print ('tchau')

