__author__ = 'Guilherme'

arq = open("outputs/pg1342.txt.enc",'rb')
entrada = arq.read()
print("Arquivo lido!")
arq.close()

chave = 0

dic = open('dicionario.txt','r')
dics =[]
dick = set()
linhas = dic.readlines()
for linha in linhas:
    aux = linha
    aux = aux.replace('\n','')
    dics.append(aux)
dic.close()

for i in range(len(dics)):
    dick.add(dics[i])

key = 0
tot = 0
qnts = 0
maior = -1
while chave < 20:
    chave += 1
    saida = []
    for i in range(len(entrada)):
        saida.append(0)

    p = 0
    at =0

    for c in entrada:
        if p >= len(entrada):
            at += 1
            p = at
        saida[p] = c
        p += chave

    achou = 0

    hue = ''.join([chr(c) for c in saida])
    hue = hue.split()

    for i in hue:
        if i in dick:
            achou += 1
    if achou > maior:
        maior = achou
        key = chave
        qnts = achou
        tot = len(hue)
        NomSai = "DecifradoTransposicao.txt"
        SaiArq = open(NomSai,"wb")
        SaiArq.write(bytes(saida))
        SaiArq.close()

    print('Total eq: ',achou,' com a chave ',chave)

print("Possivel chave: ",key," com acerto de: ",(qnts/tot)*100,"%.")