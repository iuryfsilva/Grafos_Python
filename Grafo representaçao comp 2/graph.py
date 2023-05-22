class Graph:
	def __init__(self):
		self.adj_list = {}
		self.node_count = 0
		self.edge_count = 0

  def __str__(self):
		output += "Nodes: " + str(self.node_count) + "\n"
    output += "Edges: " + str(self.edge_count) + "\n"
    output += str(self.adj_list)
    return output

  def add_node(self, node):
		if node in self.adj_list:
			print("WARN: Node", node, "already exists")
			return
		self.adj_list[node] = []
		self.node_count += 1

  def add_edge(self, node1, node2):
		try:
		  self.adj_list[node1].append(node2)#Add elemento no final de uma lista
		  self.edge_count += 1
		except KeyError as e:
			print("WARN: Node", e, "does not exist in the graph")

  def add_nodes(self, nodes):
     for node in nodes:
			 self.add_node(node)
    
  def add_two_way_edge(self, node1, node2):
		self.add_edge(node1, node2)
		self.add_edge(node2, node1)

  def remove_edge(self, node1, node2):
    self.adj_list[node1].remove(node2)
		self.edge_count -= 1


	def remove_node(self, node):
		if node in self.adj_list:
			self.adj_list.pop(node)
	  	self.node_count -= 1
		  for node in self.adj_list:
				self.adj_list.remove(
		  return
		print("WARN: Node", node, "does not exist")
		
		
