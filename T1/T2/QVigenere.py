__author__ = 'Guilherme'


file1 = open("inputs/pg174.txt", "rb")
certo = file1.read()
file1.close()

file2 = open("outputs/pg174.txt.enc", "rb")
errado = file2.read()
file2.close()

file3 = open("chaveVigenere.txt","wb")


if len(certo) != len(errado):
    print("aa sao iguais")

a = []

for i in range(len(certo)):
    a.append((errado[i] - certo[i]) % 256)

file3.write(bytes(a))
file3.close()

print("Acabou!")
