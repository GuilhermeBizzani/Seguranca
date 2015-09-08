__author__ = 'Guilherme'


file1 = open("inputs/pg11.txt", "rb")
certo = file1.read()
file1.close()

file2 = open("outputs/pg11.txt.enc", "rb")
errado = file2.read()
file2.close()

list = []
for i in range(256):
    list.append(0)

for i in range(len(certo)):
    list[errado[i]] = certo[i]

file3 = open("ListaSubs.txt", "wb")

file3.write(bytes(list))
