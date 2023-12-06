# go through the paths for each vertice, and when you see a vertice twice check if the path(now a cycle) and if odd length
# when "fixing" the edge check if there are multiple that need to be fixed. When (if) you sub them for alternative paths, when finished subbing them all
# you will have a long path and go through till you see a vertex twice again and then same thing check if odd length
  
# Function to store the connected nodes
def addEdge(adj, u, v):
 
    adj[u].append(v)
    adj[v].append(u)
 
def isBipartite(adj, v, visited, color):
    cycle = []
    for u in adj[v]:
        # If vertex u is not explored before
        if (visited[u] == False):
            cycle.append(u)

            # Mark present vertic as visited
            visited[u] = True
  
            # Mark its color opposite to its parent
            color[u] = not color[v]
  
            # If the subtree rooted at vertex v
            # is not bipartite
            if (not isBipartite(adj, u,
                                visited, color)):
                return False, cycle
                 
        # If two adjacent are colored with
        # same color then the graph is not
        # bipartite
        elif (color[u] == color[v]):
            return False, cycle
    return True, cycle
 
# Driver Code
def main():
    # No of nodes
    N = 6
  
    # To maintain the adjacency list of graph
    adj = [[] for i in range(N + 1)]
  
    # To keep a check on whether
    # a node is discovered or not
    visited = [0 for i in range(N + 1)]
  
    # To color the vertices
    # of graph with 2 color
    color = [0 for i in range(N + 1)]
  
    # Adding edges to the graph
    addEdge(adj, 2, 1)
    addEdge(adj, 1, 0)
    addEdge(adj, 0, 2)
    print(adj)
    # Marking the source node as visited
    visited[1] = True
  
    # Marking the source node with a color
    color[1] = 0
  
    # Function to check if the graph
    # is Bipartite or not
    boolean, path = isBipartite(adj, 1, visited, color)
    if (boolean):
        print("Graph is Bipartite")
    else:
        print("Graph is not Bipartite")
        print(path)
        print(color)
        print(visited)
main()