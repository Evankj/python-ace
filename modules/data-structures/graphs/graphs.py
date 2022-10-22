from Graph import Graph
from directed_graph import DirectedGraph
from Queue import MyQueue
from Stack import MyStack

# Challenge 1: Implement BFS
def bfs_traversal(g, source):
    # source == an index in the adjacency list g
    result = str(source)
    queue = MyQueue()
    level_linked_list = g.array[source]
    queue.enqueue(level_linked_list)
    while not queue.is_empty():
        visit = queue.dequeue()
        if visit:
            visit = visit.get_head()
        while visit:
            result += str(visit.data)
            queue.enqueue(g.array[visit.data])
            visit = visit.next_element
    return result



# Challenge 2: Implement DFS
# O(2n) as we traverse the graph, then check if each vertex has been visited and appened them if not
def dfs_traversal(g, source):
    result = ""
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        visit = stack.pop()
        visited[visit] = True
        result += str(visit)
        visit = g.array[visit].get_head()
        while visit:
            stack.push(visit.data)
            visit = visit.next_element
    for i in range(len(visited)):
        if not visited[i]:
            result += str(i)
    return result


# Challenge 3: Detect Cycle in a Directed Graph
# Approach: Make list of visited vertices full of False 
# while there are un-visited nodes, conduct DFS from that node
# If a node is found twice in the DFS, it means there is a loop
def detect_cycle(g):
    if g.vertices <= 0:
        return False
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push(0)
    
    dfs_checked = {}
    while not stack.is_empty():
        visit = stack.pop()
        visited[visit] = True
        if dfs_checked.get(visit):
            return True
        else:
            dfs_checked[visit] = True
        visit = g.array[visit].get_head()
        while visit:
            stack.push(visit.data)
            visit = visit.next_element

    return False
        
# Challenge 4: Find a "Mother Vertex" in a Directed Graph
# Approach: DFS through graph. Increment a counter every time a new vertex is reached.
# if this counter is equal to the number of vertices in the graph, the source vertex for that DFS is a
# mother vertex
def dfs_count(g, source):
    count = 0
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        visit = stack.pop()
        visited[visit] = True
        count += 1
        visit = g.array[visit].get_head()
        while visit:
            stack.push(visit.data)
            visit = visit.next_element
    return count + 1

def find_mother_vertex(g):
    if g.vertices <= 0:
        return None
    for i in range(g.vertices):
        if dfs_count(g, i) == g.vertices:
            return i
    return -1

# Challenge 5: Count Number of Edges in an Undirected Graph
# Approach: Iterate through all linked lists in graph representation and increment count every time.
# divide this count by 2 as edges are bidirectional
def num_edges(g):
    edges = 0
    for i in range(g.vertices):
        head = g.array[i].get_head()
        while head:
            edges += 1
            head = head.next_element
    return edges / 2

# Challenge 6: Check if a Path Exists Between Two Vertices
# Approach: DFS from source; if destination is visited, return true, else return false
def check_path(g, source, destination):
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        visit = g.array[stack.pop()]
        vertex = visit.get_head()
        while vertex:
            if vertex.data == destination:
                return True
            stack.push(vertex.data)
            vertex = vertex.next_element
    return False

# Challenge 7: Check if a Given Undirected Graph is a Tree or not
# Approach: DFS from all vertices. If we find a 
# Issue: How do we know where to start? It seems inefficient to iterate through all vertices until we find one where all nodes are visited via BFS/DFS
def dfs_check(g, source, visited):
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        visit = stack.pop()
        visited[visit] = True
        visit = g.array[visit].get_head()
        while visit:
            stack.push(visit.data)
            visit = visit.next_element
    return visited

def is_tree(g):
    if g.vertices <= 0:
        return False

    visited = [False] * g.vertices


    for i in range(g.vertices):
        # if we haven't visited a node yet, conduct a DFS from it
        if not visited[i]:
            visited = dfs_check(g, i, visited)

    # Now check if all nodes have been visited
    return visited.count(False) <= 0


# Challenge 8: Find the Shortest Path Between Two Vertices
def find_min(g, source, destination):
    stack = MyStack()
    stack.push(source)
    shortest_path_edge_count = int('inf')
    edge_count = 0
    while not stack.is_empty():
        visit = g.array[stack.pop()]
        vertex = visit.get_head()
        edge_count += 1
        while vertex:
            if vertex.data == destination:
                if edge_count < shortest_path_edge_count:
                    shortest_path_edge_count = edge_count
            stack.push(vertex.data)
            vertex = vertex.next_element
    return False

# Challenge 9: Clone a Directed Graph
# Not a good approach, potentially O(n^2) or worse with the "find_vertex_by_data" calls...
def clone(graph):
  if len(graph.nodes) <= 0:
    return None

  # Clone nodes
  clone_graph = DirectedGraph()
  nodes = graph.nodes
  for node in nodes:
    clone_graph.add_vertex(node.data)


  # Hashmap to keep record of visited nodes
  nodes_completed = {}
  # Creating new graph
  first_node = graph.nodes[0].data 
  stack = [first_node]
  # nodes_completed[first_node] = True
  # dfs to clone edges
  while len(stack) > 0:
    node = stack.pop()
    if not nodes_completed.get(node, False):
      neighbors = graph.find_vertex_by_data(node).neighbors
      for neighbor in neighbors:
        stack.append(neighbor.data)
        clone_graph.add_edge(node, neighbor.data)
      nodes_completed[node] = True
  # Return deep copied graph
  return clone_graph
