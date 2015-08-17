import math

__author__ = 'Guilherme'


print("Bem vindo ao criptografador de Transposicao!")
ent = 1
while 0 != ent:

    print("Digite o nome do programa de entrada COM A EXTENSAO!")
    arq = input('->')

    file = open(arq, 'rb')
    leitura = file.read()
    file.close()

    print("Menu:\n1 - Criptografar frase\n2 - Descriptografar frase.\n0 - Sair.")
    ent = int(input('Opcao: '))
    if ent == 0:
        break
    chave = int(input('Digite a chave: '))
    saida = open("saidaTrans.txt", "wb")

    cols = math.ceil(len(leitura)/chave)

    if ent == 1:
        mat = []
        cont = 0
        coluna = []
        total = 1
        for x in leitura:
            if cont == chave:
                mat.append(coluna)
                ##print(coluna)
                coluna = []
                cont = 0
                total += 1
            ##print(chr(x))
            coluna.append(x)
            cont += 1
        if len(coluna) < chave:
            for k in range(len(coluna),chave):
                coluna.append(158)
        mat.append(coluna)
        ##print(mat)
        aux = []
        for i in range(chave):
            for j in range(total):
                aux.append(mat[j][i])
        ##print(aux)
        saida.write(bytes(aux))

    if ent == 2:
        mat = []
        cont = 0
        coluna = []
        total = 1
        for x in leitura:
            if cont == cols:
                mat.append(coluna)
                ##print(coluna)
                coluna = []
                cont = 0
                total += 1
            ##print(chr(x))
            coluna.append(x)
            cont += 1
        if len(coluna) < chave:
            for k in range(len(coluna),chave):
                coluna.append(0)
        mat.append(coluna)
        ##print(mat)
        aux = []
        for i in range(cols):
            for j in range(total):
                if mat[j][i] == 158:
                    mat[j][i] = 0
                aux.append(mat[j][i])
        ##print(aux)
        saida.write(bytes(aux))

    saida.close()

