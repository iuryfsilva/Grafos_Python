altura = float(input("Informe altura: "))
peso = float(input("Informe o peso em KG: "))
if altura != 0.00:
    imc = peso / (altura ** 2)

if imc >= 18.5 and imc <= 25.0:
    print("Peso NORMAL")
elif imc > 25.0:
    print("Sobrepeso")
elif imc < 18.5:
    print("Sobrepeso")
