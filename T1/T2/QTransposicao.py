__author__ = 'Guilherme'


file1 = open("inputs/pg11.txt", "rb")
certo = file1.read()
file1.close()

file2 = open("saidaTrans.txt", "rb")
errado = file2.read()
file2.close()

binda = 99999999
chave = 1
while chave < binda:
    chave += 1
    mat = []
    cont = 0
    coluna = []
    total = 1
    for x in certo:
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


    flag = 0
    for i in range(len(aux)):
        if(aux[i] != errado[i]):
            flag = 1
            break

    if(flag == 0):
        print("Deu certo!!!! Chave: "+str(chave))
        break
    else:
        print("Chave "+str(chave)+" nao deu certo!")
