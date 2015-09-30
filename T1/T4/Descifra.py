__author__ = 'Guilherme'


arqCif = open("outputs/pg76.txt.enc", "rb")
cifrado = arqCif.read()
arqCif.close()

arqTab = open("tabela1.txt", "r")
tabela = arqTab.read()
arqTab.close()

saida = ""

for x in cifrado:
    saida = saida + str(tabela[x])

arqSai = open("FIM.txt", "w")
arqSai.write(saida)
