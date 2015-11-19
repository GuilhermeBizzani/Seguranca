__author__ = 'Guilherme'


print("Bem vindo ao programa de calculos de BIG INTEGER.\n")

file = open("entrada.txt", "r")

leit = file.readlines()

n1 = leit[0]
n2 = leit[1]
print(n1)
print(n2)
n1 = n1.replace("\n","")
n2 = n2.replace("\n","")

file.close()

num1 = []
i = 0
aux = len(n1)%8
num1.append(n1[i:aux])
while i < len(n1)-8:
    num1.append(int(n1[i:i+8]))
    i+=8

num2 = []
i = 0
aux = len(n2)%8
num2.append(n2[i:aux])
while i < len(n2)-8:
    num2.append(int(n2[i:i+8]))
    i+=8

num1.reverse()
num2.reverse()

print("Qual operacao deseja?\n1 - Soma\n2 - Multiplicacao\n3 - Exponensiacao\n->")
opcao = input()

print(opcao)

if opcao == "1":
    print("n1: ",num1)
    print("n2: ",num2)

    if len(num1) > len(num2):
        tam = len(num1)+1
    else:
        tam = len(num2)+1

    a = len(num1)
    while a < tam:
        num1.append(int(0))
        a+=1
    a = len(num2)
    while a < tam:
        num2.append(int(0))
        a+=1

    result = []
    for i in range(tam):
        result.append(int(0))

    for i in range(tam):
        aux = int(num1[i]) + int(num2[i])
        if(aux > 100000000):
            aux = aux - 100000000
            result[i+1] += 1
        result[i] += aux

    result.reverse()

print("result: ")
i = 0
if result[0] == 0:
    i = 1
while i < len(result):
    print(result[i], end="")
    i+=1
