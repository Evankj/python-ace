from directed_graph_node import *

class DirectedGraph:   
    def __init__(self):
        self.nodes = []
        
    def add_vertex(self, data):
        obj_node = Node(data)
        self.nodes.append(obj_node)
    
    def find_vertex_by_data(self, data):
        for node in self.nodes:
            if node.data == data:
                return node 
        return None

    def count(self):
      return len(self.nodes)
    
    def add_edge(self, start_node, end_node):
        start = self.find_vertex_by_data(start_node)
        end = self.find_vertex_by_data(end_node)

        if start and end:
            start.neighbors.append(end)
        else:
            print("Node not found\n")

    def print_graph(self):
        for node in self.nodes:
            print(str(node.data) + " -> {  ", end="")
            for n in node.neighbors:
                print(str(n.data) + "  ", end="")
            print("}")

    # vertex insert
    def add_vertex_in_nodes(self, node):
        self.nodes.append(node)

    def delete_edge(self, node, neighbor):
      for v in self.nodes:
        if v.data == node:
            for n in v.neighbors:
                if (n.data == neighbor):
                    v.neighbors.remove(n) 
