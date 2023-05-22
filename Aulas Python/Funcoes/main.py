def encontra_minimo(elementos):
	minimo = float("int")  #Elementos[0]
	for i in range(len(elementos)):
		if elementos[i] < minimo:
			minimo = elementos[i]
	return minimo


def soma_elementos(elementos):
	soma = 0
	for i in elementos:
		soma += elementos
	return soma


def encontra_min_max(elementos):
	minimo = float("int")  #Elementos[0]
	maximo = float("int")  #Elementos[0]
	for i in range(len(elementos)):
		if elementos[i] < minimo:
			minimo = elementos[i]
		if elementos[i] > maximo:
			maximo = elementos[i]
	return (minimo, maximo)  #tuplas tem tamanho fixo


a = [4, 5, 8, -2]

print(encontra_minimo(a))
print(soma_elementos(a))

(min, max) = encontra_min_max(a)
print(min, max)
