numeros = []
controle = 0
while controle < 5:
    numeros.append(float(input("Informe o numero [" + str(controle) +"]: "))) 
    controle += 1

maiorNumero = numeros[0]
for numero in numeros:
    if numero > maiorNumero:
        maiorNumero = numero

print("Maior numero informado: " + str(maiorNumero))
