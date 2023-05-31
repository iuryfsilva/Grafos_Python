tamanhoArquivo = float(input("Informe o tamanho do arquivo em MB: "))
velocidadeLinkInternet = float(input("Informe a velocidade do link de internet MBs: "))
if tamanhoArquivo > 0:
    print("Tempo aproximado de download = " + str((velocidadeLinkInternet/tamanhoArquivo)/60) + " minutos")
