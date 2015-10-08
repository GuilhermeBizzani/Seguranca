__author__ = 'Guilherme'

quantos = 10

arqCript = open("DICDec1.txt", "r")
arqLivro = open("DICLivro1.txt", "r")

leCript = arqCript.readlines()
leLivro = arqLivro.readlines()

arqCript.close()
arqLivro.close()

tabelaSai = open("tabela1.txt", "wb")

dez = 0

aux1 = []
for i in range(quantos):
    aux1.append([])
for line in leCript:
    splitado = str.split(str(line),' ')
    aux1[dez].append(splitado[0])
    aux1[dez].append(splitado[1])
    aux1[dez].append(splitado[2])
    dez+=1
    if dez == quantos:
        break

dez = 0
aux2 = []
for j in range(quantos):
    aux2.append([])
for line in leLivro:
    splitado = str.split(str(line),' ')
    aux2[dez].append(splitado[0])
    aux2[dez].append(splitado[1])
    aux2[dez].append(splitado[2])
    dez+=1
    if dez == quantos:
        break

tabela = []

for k in range(256):
    tabela.append(63)


for l in range(quantos):
    if tabela[int(aux1[l][0])] == 63 and int(aux2[l][0]) not in tabela:
       tabela[int(aux1[l][0])] = int(aux2[l][0])

    if tabela[int(aux1[l][1])] == 63 and int(aux2[l][1]) not in tabela:
       tabela[int(aux1[l][1])] = int(aux2[l][1])

    if tabela[int(aux1[l][2])] == 63 and int(aux2[l][2]) not in tabela:
       tabela[int(aux1[l][2])] = int(aux2[l][2])

total = 0
for x in tabela:
    if x != 63:
        total +=1

tabelaSai.write(bytes(tabela))

print("Achou ",total," letras dif")
