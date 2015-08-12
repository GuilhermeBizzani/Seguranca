import math

__author__ = 'Guilherme'

file = open('TransSaidaaaa.txt', 'r')
leitura = file.read()

print(leitura)

print("Bem vindo ao criptografador de Transposicao!")
ent = ''
while 0 != ent:
    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    chave = int(input('Digite a chave: '))
    saida = open("TransSaidaaaabbb.txt", "w")
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
        #print('Frase Original     : '+ leitura)
        #print('Frase Criptografada: ' + a)
        saida.write(a)

    if ent == 2:
        pos = 0
        for j in range(0, chave):
            for i in range(0, cols):
                if pos < len(leitura):
                    mat[j][i] = leitura[pos]
                    pos += 1
                else:
                    mat[j][i] = ''
        a = ''
        for i in range(0, cols):
            for j in range(0, chave):
                a += mat[j][i]
        #print('Frase Original        :' + leitura)
        #print('Frase Descriptografada:' + a)
        saida.write(a)

    saida.close()

