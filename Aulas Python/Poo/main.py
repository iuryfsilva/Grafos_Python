from aluno import Aluno
a1 = Aluno("Bia", 19, 9.2, 0.8)
a2 = Aluno("Bruna", 17, 7.2, 8.8)

print(a1.nome, a1.idade)
print(a2.nome, a2.idade)

a2.nota = 10.0
print(a2.nota)
