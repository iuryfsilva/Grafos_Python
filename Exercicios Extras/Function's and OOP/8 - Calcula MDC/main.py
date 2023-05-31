def calculaMDC(valor1, valor2):
    while valor2 != 0:
        resto = valor1 % valor2
        valor1 = valor2
        valor2 = resto
    return valor1

valor1 = int(input("Informe o valor 1: "))
valor2 = int(input("Informe o valor 2: "))
print("Valor do MDC = " + str(calculaMDC(valor1, valor2)))
    