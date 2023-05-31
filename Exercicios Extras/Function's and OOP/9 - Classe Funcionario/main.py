from funcionario import Funcionario

empregado = Funcionario(input("Informe o nome: "), float(input("Informe o salario: ")))
print("Funcionario criado: " + "\nNome: " + empregado.nome + "\nSalario: " + empregado.salario)