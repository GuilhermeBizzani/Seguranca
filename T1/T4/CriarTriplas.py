__author__ = 'Guilherme'
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

class Tripla():
    def __init__(self, atrip, aqtd):
        self.trip = []
        self.trip = atrip
        self.qtd = aqtd


arq = open("dicionario.txt",'rb')
entrada = arq.read()
entrada = entrada[0:10000]
print("Arquivo lido!")
arq.close()

out = open("sai.txt", "wb")
triplas = []
for i in range(len(entrada)-3):
    aux = entrada[i:i+3]
    triplas.append(aux)


