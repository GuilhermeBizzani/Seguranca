__author__ = 'Guilherme'

import itertools
import time

ini = time.time()

file = open("outputs/pg174.txt.enc", 'rb')
leitura = file.read()
file.close()

leitura = leitura[0:10]

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

'''
#aqui cria o vetor de chaves:
vetChaves = []
strtemp = ""

#Preenchimento do vetor de chaves
for i in range(ord('0'), ord('6')+1):
    #print (chr(i))
    vetChaves.append(str(chr(i)))

for i in range(ord('0'), ord('6')+1):
    for j in range(ord('0'), ord('6')+1):
        strtemp = ""
        strtemp += str(chr(i))
        strtemp += str(chr(j))
        #print (strtemp)
        vetChaves.append(strtemp)

for i in range(ord('0'), ord('6')+1):
    for j in range(ord('0'), ord('6')+1):
        for k in range(ord('0'), ord('6')+1):
            for l in range(ord('0'), ord('6')+1):
                for m in range(ord('0'), ord('6')+1):
                    for n in range(ord('0'), ord('6')+1):
                        strtemp = ""
                        strtemp += str(chr(i))
                        strtemp += str(chr(j))
                        strtemp += str(chr(k))
                        strtemp += str(chr(l))
                        strtemp += str(chr(m))
                        strtemp += str(chr(n))
                        #print (strtemp)
                        vetChaves.append(strtemp)

#fim de criar as chaves.
'''

vetChaves = itertools.product('abcdefghijklmnopqrstuvxz',repeat=3)

#vetChaves = itertools.product('123456',repeat=6)

maior = -1
key = ""

for chave2 in vetChaves:
    chave = ""
    for i in chave2:
        chave += i

    tam = len(chave)
    atual = 0
    saida = []
    for x in leitura:
        saida.append((x - ord(chave[atual]))%256)
        atual+=1
        if atual == tam:
            atual = 0


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

#print("Possivel chave: ",key," com acerto de: ",(qnts/tot)*100,"%.")
fim = time.time()

print("Tempo total: ",fim-ini)
