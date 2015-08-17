__author__ = 'Guilherme'


file1 = open("teste1.txt","rb")
leit1 = file1.read()
file1.close()


file2 = open("outputs/pg174.txt.enc","rb")
leit2 = file2.read()
file2.close()


a = len(leit1)

print(a)

