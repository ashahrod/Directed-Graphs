from os import read
import sys
from collections import defaultdict

class Graph:
  
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.numVertices = vertices
        self.visitNum = 0
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def addDirected(self, u, v):
        self.graph[u].append(v)

def makeGraph(edges, numVertices):
    graph = Graph(numVertices)
    for edge in edges:
        graph.addEdge(edge[0], edge[1])
    return graph

def makeDir(edges, numVertices):
    graph = Graph(numVertices)
    for edge in edges:
        graph.addDirected(edge[0], edge[1])
    return graph

def read_file(file_name):
    f = open(file_name, 'r')
    edges = [] 
    seen = []
    for line in f.readlines():
    #need to make the strings ints
        # print(line)
        mapped = map(int, line.split(", "))
        temp_list = list(mapped)
        edges.append(temp_list)
        if temp_list[0] not in seen:
            seen.append(temp_list[0])
        if temp_list[1] not in seen:
            seen.append(temp_list[1])
    edges = sorted(edges, key=lambda x: x[0])
    # print(edges)
    # print(seen)
    # print(len(seen))
    return edges, len(seen)

def callBipartite(graph, num_vertices):
    visited = [0 for vertex in range(num_vertices + 1)]
    color = [0 for vertex in range(num_vertices+ 1)]
    color[1] = 0
    visited[1] = True
    if (checkBipartite(graph.graph , 1, visited, color) is True):
        print("Bipartite; no odd-length cycles.", end='')
        return False
    else:
        print("Not bipartite; odd-length cycle:")
        return True

def checkBipartite(graph, v, visited, color):
 
    for u in graph[v]:
        if (visited[u] == False):
            visited[u] = True
            color[u] = not color[v]
            if (not checkBipartite(graph, u,
                                visited, color)):
                return False  
        elif (color[u] == color[v]):
            return False
    return True

def dfs(graph, start, end):
    stream = [(start, [])]
    while stream:
        node, path = stream.pop()
        if path and node == end:
            yield path
            continue
        for next_node in graph.get(node, []):
            if next_node in path:
                continue
            stream.append((next_node, path+[next_node]))

def main():
    edges, num_vertices = read_file(sys.argv[1])
    graph = makeGraph(edges, num_vertices)
    hasOddCycle = callBipartite(graph, num_vertices)
    # print(graph.graph)
    if (hasOddCycle is True):
        dir_graph = makeDir(edges, num_vertices)
        # graph = { 1: [0], 2: [1], 3: [2], 4: [3, 5], 5: [1], 0: [3, 4] }
        cycles = [[node]+path  for node in dir_graph.graph for path in dfs(dir_graph.graph, node, node)]
        for cycle in cycles:
            if(len(cycle) % 2 == 0):
                odd = cycle
                i = 1
                for vertex in odd:
                    print(str(vertex), end='')
                    if (len(cycle) != i):
                        print(", ", end='')
                    i += 1
                break
             
main()