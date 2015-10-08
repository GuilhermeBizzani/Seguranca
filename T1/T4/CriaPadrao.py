__author__ = 'Guilherme'


import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

class Padrao():
    def __init__(self,vpal, vpadrao, vqnt):
        self.pal = []
        self.pal = vpal
        self.padrao = []
        self.padrao = vpadrao
        self.qnt = vqnt

arq = open("dicionario.txt","rb")
dic = arq.read()
dic = dic[0:1000]
arq.close()

dic = dic.split()

print("hue")

padrao = [Padrao]
semRepeticoes = [Padrao]
semRepeticoes.clear()
padrao.clear()

for pal in dic:

    padr = []
    for i in range(len(pal)):
        padr.append(-1)

    a = 1
    padr[0] = 1
    j=0
    while j < (len(pal)-1):
        j+=1
        flag = 0
        for k in range(j):
            if pal[j] == pal[k]:
                padr[j] = padr[k]
                flag = 1
                break
        if flag == 0:
            a += 1
            padr[j] = a

    padrao.append((pal, padr, 1))
    b = [Padrao]
    b.append((pal, padr, 1))

    if b[1] not in semRepeticoes:
        semRepeticoes.append(b[1])
    b.clear()

final = [Padrao]
final.clear()
for x in semRepeticoes:
    tot = padrao.count(x)
    final.append((x[0], x[1], tot))

final.sort(key=lambda x: x[2])

#aqui comeca a parte com o arquivo cifrado.

arq2 = open("outputs/pg76.txt.enc", "rb")
leita = arq2.read()
arq2.close()
leit = []
for f in leita:
    leit.append(f)
tab = open("tabela.txt","rb")
tabelaa = tab.read()
tab.close()

tabela = []
for g in tabelaa:
    tabela.append(g)
cont = 0

for x in final:
    print("oi")
    cont += 1
    if cont == 10:
        break
    for n in range(len(leit)-len(x[1])):
        aux = leit[n:n+len(x[1])]

        padr = []
        for m in range(len(aux)):
            padr.append(-1)

        a = 1
        padr[0] = 1
        j=0
        while j < (len(aux)-1):
            j+=1
            flag = 0
            for k in range(j):
                if aux[j] == aux[k]:
                    padr[j] = padr[k]
                    flag = 1
                    break
            if flag == 0:
                a += 1
                padr[j] = a

        if padr == x[1]:
            aux2 = x[0]

            for h in range(len(x[0])):
                tabela[aux[h]] = aux2[h]

tab2 = open("tabela22.txt","wb")
tab2.write(bytes(tabela))
tab2.close()

print("fim", final)