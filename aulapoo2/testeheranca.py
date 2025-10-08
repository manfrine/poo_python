
from aluno import Aluno
from alunofacul import AlunoFacul

nome = x1 = (input("Digite um nome: "))
x1 = (float(input("Digite a nota 1: ")))
x2 = (float(input("Digite a nota 2: ")))

a1 = Aluno(nome, x1, x2)
a1.calcMedia()

nome = x1 = (input("Digite um nome: "))
x1 = (float(input("Digite a nota 1: ")))
x2 = (float(input("Digite a nota 2: ")))
x3 = (float(input("Digite a nota 3: ")))

a2 = AlunoFacul(nome, x1, x2, x3)
a2.calcMedia()


print(f"Aluno: {a1.getNome()} | Média: {a1.getMedia()} | Status: {a1.getStatus()}")
print(f"Aluno Facul: {a2.getNome()} | Média: {a2.getMedia()} | Status: {a2.getStatus()}")
