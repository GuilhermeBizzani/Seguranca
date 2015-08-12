import math

__author__ = 'Guilherme'

file = open('pg11.txt', 'r')
leitura = file.read()

print(leitura)

print("Bem vindo ao criptografador de Vigenere!")
ent = ''
while (ent != 0):
    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    chave = input('Digite a chave: ')
    chav = ''

    qnt = math.ceil(len(leitura) / len(chave))
    for i in range(1, qnt):
        chav = chav + chave

    print('Chav: ' + chav)
    a = ''
    if(ent == 1):

        for x in range(0, len(chav)):
            le = ord(leitura[x])
            ch = ord(chav[x])
            lee = chr(le + ch)
            a += lee

        print('Frase Original: '+ leitura)
        print('Frase Criptografada: ' + a)

    if(ent == 2):

        for x in range(0, len(chav)):
            le = ord(leitura[x])
            ch = ord(chav[x])
            lee = chr(le - ch)
            a += lee

        print('Frase Original: ' + leitura)
        print('Frase Descriptografada:' + a)


print ('tchau')

