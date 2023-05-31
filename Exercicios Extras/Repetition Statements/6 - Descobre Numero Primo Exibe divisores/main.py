numero = int(input("Informe o numero inteiro: ")) 
multiplos = 0

for contador in range(2,numero):
    if (numero % contador == 0):
        print("Múltiplo: " + str(contador))
        multiplos += 1

if(multiplos == 0):
    print("Divisores 1 e " + str(numero))
else:
    print("Quantidade de multiplos contando com 1 e ele proprio: " + str(multiplos + 2))