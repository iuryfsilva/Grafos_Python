salarioBase = float(input("Informe seu salario: "))
if salarioBase <= 1903.98:
    print("Salario = " + str(salarioBase))
else:    
    aliquota = 0
    deducao = 0
    if salarioBase >= 1903.99 and salarioBase <= 2826.65:
        aliquota = 7.5
        deducao = 142.80
    elif salarioBase >= 2826.66 and salarioBase <= 3751.05:
        aliquota = 15.0
        deducao = 354.80
    elif salarioBase >= 3751.06 and salarioBase <= 4664.68:
        aliquota = 22.5
        deducao = 636.13
    elif salarioBase > 4664.69:
        aliquota = 27.5
        deducao = 869.36
        
    print("Salario = " + str((salarioBase * (aliquota/100)) - deducao))

