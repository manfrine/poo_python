
from aluno import Aluno

nome = x1 = (input("Digite um nome: "))
x1 = (float(input("Digite a nota 1: ")))
x2 = (float(input("Digite a nota 1: ")))

a1 = Aluno(nome, x1, x2)
a1.calcMedia()

nome = x1 = (input("Digite um nome: "))
x1 = (float(input("Digite a nota 1: ")))
x2 = (float(input("Digite a nota 1: ")))

a2 = Aluno(nome, x1, x2)
a2.calcMedia()


print(f"Aluno: {a1.getNome()} | Média: {a1.getMedia()} | Status: {a1.getStatus()}")
print(f"Aluno: {a2.getNome()} | Média: {a2.getMedia()} | Status: {a2.getStatus()}")