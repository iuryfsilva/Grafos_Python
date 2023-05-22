#importar a classe Graph e criar o grafo de esquerda num objeto dessa classe
from graph import Graph
g = Graph()

g.add_node("Bia")#Self é o g que é passado para a funcao chamada
g.add_node("Caio")
g.add_node("Liz")
g.add_node("Alex")

g.add_edge("Caio","Liz") 
g.add_edge("Liz","Caio")
g.add_edge("Alex","Liz")
g.add_edge("Caio","Alex")

print(g.adj_list)
