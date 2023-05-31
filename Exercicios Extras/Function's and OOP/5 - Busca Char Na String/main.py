def buscaCharNaString(palavra, letra):
    contador = 0
    for caracter in palavra:
        if caracter == letra:
            contador += 1
    
    return contador

palavra = input("Informe a palavra: ")
letra = input("Informe o caracter: ")

print("O caracter aparece na palavra " + str(buscaCharNaString(palavra, letra)) + " vezes")