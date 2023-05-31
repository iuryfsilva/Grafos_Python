def inverteString(palavra):
    return palavra[::-1]

def testaPalindromo(palavra):
    return inverteString(palavra) == palavra

print("A palavra é um palindromo? " + str(testaPalindromo(input("Informe uma palavra: "))))