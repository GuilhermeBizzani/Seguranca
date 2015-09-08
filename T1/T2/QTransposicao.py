__author__ = 'Guilherme'
import gc
gc.disable()

file1 = open("inputs/pg1342.txt", "rb")
certo = file1.read()
file1.close()

file2 = open("outputs/pg1342.txt.enc", "rb")
errado = file2.read()
file2.close()

binda = 99999999
chave = 1
while chave < binda:
    #print('Chave Atual: ',chave)

    saida = []
    for i in range(len(errado)):
        saida.append(0)

    p = 0
    at =0

    for c in errado:
        if p >= len(errado):
            at += 1
            p = at
        saida[p] = c
        p += chave

    dif = 0
    for s in range(len(certo)):
        if saida[s] != certo[s]:
            dif = 1
            break

    if dif == 0:
        print("Decifrado com sucesso utilizando a chave ",chave," !")
        NomSai = "SaiTrans.txt"
        SaiArq = open(NomSai,"wb")
        SaiArq.write(bytes(saida))
        SaiArq.close()
        break
    else:
        chave += 1

print("\nProcesso Finalizado!")

