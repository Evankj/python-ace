from Graph import Graph
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

