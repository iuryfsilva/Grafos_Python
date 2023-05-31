tamanhoAreaAPintar = float(input("Informe o tamanho da area a ser pintada em metros quadrados: "))
quantidadeLatas = (0.33 * tamanhoAreaAPintar)/18
print("Quantidade de latas de tinta = " + str(quantidadeLatas))
if quantidadeLatas % 2 != 0:
    quantidadeLatas += 1 

quantidadeLatas = int(quantidadeLatas)
print("Quantidade de latas de 18 litros necessárias = " + str(quantidadeLatas))
valorLata = float(input("Informe o Valor de cada lata de tinta: "))
print("Valor total R$ " + str(quantidadeLatas * valorLata))

    
