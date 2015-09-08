__author__ = 'Guilherme'

arq = open("outputs/pg1232.txt.enc",'rb')
entrada = arq.read()
entrada = entrada[0:200]
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

while chave < 255:
    chave += 1
    saida = []
    for c in entrada:
        saida.append((c - chave) % 256)

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
        NomSai = "DecifradoCesar.txt"
        SaiArq = open(NomSai,"wb")
        SaiArq.write(bytes(saida))
        SaiArq.close()
    print('Total eq: ',achou,' com a chave ',chave)

print("Possivel chave: ",key," com acerto de: ",(qnts/tot)*100,"%.")