tamanho = int(input("Informe o tamanho do quadrado: ")) 

for linha in range(1, tamanho + 1):
    for coluna in range(1, tamanho + 1):
        if linha == 1 or linha == tamanho or coluna == 1 or coluna == tamanho:
            print("*", end = " ")
        else: 
            print(" ", end = " ")
    print()
    