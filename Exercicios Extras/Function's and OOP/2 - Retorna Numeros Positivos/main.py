def numerosPositivos(numeros):
    positivos = []
    for numero in numeros:
        if numero > 0:
            positivos.append(numero)
    return positivos 

numeros = []
while True:
    numero = float(input("Informe um numero ou 0 para sair: ")) 
    if numero != (0):
        numeros.append(numero)
    else:
        break

print("Numeros Informados: " + str(numeros) + "\n" + "Positivos: " + str(numerosPositivos(numeros)))
