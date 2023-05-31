import re 
from collections import Counter

def contaVogaisNaString(palavra):
    resultado = Counter(re.sub('[^aeiouAEIOU]', '', palavra)) 
    return resultado

palavra = input("Informe uma palavra: ")
print("A palavra possui as seguintes vogais e suas respectivas quantidades: " + str(contaVogaisNaString(palavra)))