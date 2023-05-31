tamanho = int(input("Informe o tamanho do triangulo: ")) 
for linha in range(1, tamanho):
    for coluna in range(1, linha + 1):
        print("*", end = " ")
    print()
    