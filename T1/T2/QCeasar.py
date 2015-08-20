__author__ = 'Guilherme'

file1 = open("inputs/pg1232.txt", "rb")
certo = file1.read()
file1.close()

file2 = open("outputs/pg1232.txt.enc", "rb")
errado = file2.read()
file2.close()

a = len(errado)
deumerda = 0
chaveachada = (errado[0] - certo[0]) % 256

for i in range (0,a):
    if chaveachada != (errado[i] - certo[i]) % 256 :
        deumerda = 1


print("Chave eh "+ str(chaveachada))
if deumerda:
    print("Deu merda")
else:
    print("Deu Boa!")


print("Acabou")