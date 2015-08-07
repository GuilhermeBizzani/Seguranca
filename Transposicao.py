import math

__author__ = 'Guilherme'

file = open('entrada.txt', 'r')
leitura = file.read()

print(leitura)

print("Bem vindo ao primeiro criptografador!")
ent = ''
while 0 != ent:
    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    chave = int(input('Digite a chave: '))

    cols = math.ceil(len(leitura)/chave)
    mat = [''] * chave
    for i in range(0, chave):  #nao
        mat[i] = [''] * cols

    if ent == 1:
        pos = 0
        for j in range(0, cols):
            for i in range(0, chave):
                if pos < len(leitura):
                    mat[i][j] = leitura[pos]
                    pos += 1
                else:
                    mat[i][j] = ''
        a = ''
        for i in range(0, chave):
            for j in range(0, cols):
                a += mat[i][j]
        print('Frase Original: '+ leitura)
        print('Frase Criptografada: ' + a)

    if ent == 2:
        pos = 0
        for j in range(0, cols):
            for i in range(0, chave):
                if pos < len(leitura):
                    mat[i][j] = leitura[pos]
                    pos += 1
                else:
                    mat[i][j] = ''
        a = ''
        for i in range(0, cols):
            for j in range(0, chave):
                a += mat[j][i]
        print('Frase Original: '+ leitura)
        print('Frase Descriptografada: ' + a)


