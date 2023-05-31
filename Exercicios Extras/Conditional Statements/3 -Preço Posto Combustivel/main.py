tipoCombustivel = input("Informe o tipo de combustivel: A-Alcool, G-Gasolina \n")
litrosVendidos = float(input("Informe a quantidade de litros vendidos: "))
desconto = 0
    
if tipoCombustivel.upper() == "A":
    precoAlcool = 2.80
    if litrosVendidos > 20.00:
        desconto = 5/100
    elif litrosVendidos <= 20.00:
        desconto = 3/100
    print("Preço total = " + str((litrosVendidos * precoAlcool) - (litrosVendidos * precoAlcool * desconto)))

elif tipoCombustivel.upper() == "G":
    precoGasolina = 4.20
    if litrosVendidos > 20.00:
        desconto = 6/100
    elif litrosVendidos <= 20.00:
        desconto = 4/100
    print("Preço total = " + str((litrosVendidos * precoGasolina) - (litrosVendidos * precoGasolina * desconto)))

else:
    print("Opps, tipo de combustivel inválido!")