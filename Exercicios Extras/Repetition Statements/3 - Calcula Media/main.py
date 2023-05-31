numeros = []
controle = 0
while controle < 5:
    numeros.append(float(input("Informe o numero [" + str(controle) +"]: "))) 
    controle += 1

soma = 0
for numero in numeros:
    soma += numero

print("Soma: " + str(soma) + "\nMedia: " + str(soma/controle))
