def verifica_vizinhos_grafo_lista(no1, no2, grafo):
	return no2 in grafo[no1]

def verifica_vizinhos_grafo_matriz(no1, no2, grafo):
	return grafo[no1][no2] == 1