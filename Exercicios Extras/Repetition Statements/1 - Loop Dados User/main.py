nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))
salario = float(input("Informe o salario: "))
sexo = input("Informe o sexo: ")
estadoCivil = input("Informe o estado civil: ")
while True:
    if len(nome) < 3:
        nome = input("Informe o nome: ")
    elif idade > 0 and idade <= 150:
        idade = int(input("Informe a idade: "))
    elif salario < 0.00:
        salario = float(input("Informe o salario: "))
    elif sexo.upper() != "F" and sexo.upper() != "M":
        sexo = input("Informe o sexo: ")
    elif estadoCivil.upper() != "S" and estadoCivil.upper() != "C" and estadoCivil.upper() != "V" and estadoCivil.upper() != "D":
        estadoCivil = input("Informe o estado civil: ")
    else:
        break
