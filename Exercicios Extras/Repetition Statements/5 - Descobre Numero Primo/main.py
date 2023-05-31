numero = int(input("Informe o numero inteiro: ")) 
multiplos = 0

for contador in range(2,numero):
    if (numero % contador == 0):
        multiplos += 1

if(multiplos == 0):
    print("É numero primo")
else:
    print("Quantidade de multiplos contando com 1 e ele proprio: " + str(multiplos + 2))