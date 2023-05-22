import funcoes_grafos
grafo_lista = [[],
							 [2,3],
							 [1,3],
							 [1,2]]
grafo_matriz = [[0,0,0,0],
								[0,0,1,1],
								[0,1,0,1],
								[0,1,1,0]]

#Verificar se o 1 e ligado ao 3 
eh_vizinho = False

#Faz o mesmo que o for seguinte
#print(3 in grafo_lista[1])
for no in grafo_lista[1]
	if no == 3:
		eh_vizinho = True
		break
print(eh_vizinho)

#Verificar se o 1 e ligado ao 3
#Faz o memso que as validações Seguintes
#print(grafo_matriz[1][3] == 1)
if grafo_matriz[1][3] == 1:
	print("True")
else:
	print("False")

#Para Grafos orientados
#Armazena um lista somente com os sucessores
grafo_orientado_lista = [[],
							 					 [3],
							 					 [1,3],
							 					 [2]]
grafo_orientado_matriz = [[0,0,0,0],
													[0,0,1,1],
													[0,1,0,1],
													[0,1,1,0]]

#Para Grafos orientados Ponderado
#Armazena um lista somente com os sucessores
grafo_orientado_lista_Dicionario = {"Bia" : [],
												 "Caio" : ["Alex"],
							 					 "Liz" : ["Caio", "Alex"],
												 "Alex" : ["Liz"]}


print(grafo_orientado_lista_Dicionario.keys())
grafo_orientado_lista_Dicionario["Luiz"] = ["Bia", "Liz"]#adicionar esse elemento no dic de dados
print(grafo_orientado_lista_Dicionario)

grafo_orientado_matriz = [[0,0,0,0],
													[0,0,1,1],
													[0,1,0,1],
													[0,1,1,0]]

