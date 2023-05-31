salarioPorHora = float(input("Informe seu salario por hora: "))
horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))
salarioBruto = salarioPorHora * horasTrabalhadas
quantiaInss = salarioBruto*(10/100)
quantiaSindicato = salarioBruto*(2/100)
quantiaImpostoRenda = salarioBruto*(15/100)

print("Salario bruto = " + str(salarioBruto))
print("Quantia Sindicato = " + str(quantiaSindicato))
print("Quantia Imposto de Renda = " + str(quantiaImpostoRenda))
print("Quantia INSS = " + str(quantiaInss))
print("Salario liquido = " + str(((salarioBruto - quantiaInss) - quantiaImpostoRenda) - quantiaInss))

