numeros = []
controle = 0
while controle < 10:
    numeros.append(float(input("Informe o numero [" + str(controle) +"]: "))) 
    controle += 1

pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Numeros pares: " + str(pares) + "\nNumeros impares: " + str(impares))
print("Quantidade pares: " + str(len(pares)) + "\nQuantidade impares: " + str(len(impares)))

