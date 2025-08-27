import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start] # Initialize the path
    
    if start == goal:
        return path #If start is goal, return the path
    
    if start not in graph:
        return None #If start is not in graph, retunr None
    
    for node in graph[start]:
        if node not in path: #Avoid cycles
            new_path = path + [node] #Append mode to the path
            result = dfs(graph, node, goal, new_path) #Recursive call
            
            if result is not None:
                return result #If a path is found, return it
            
    return None # If no path is found, return None

#Example graph represented as an adjancency list

graph = {
    'A': ['B','L'],
    'L': ['O','Q'],
    'O': [],
    'Q': [],
    'B': ['C','X'],
    'C': ['E'],
    'E': ['Z'],
    'Z': [],
    'X': ['Y'],
    'Y': ['J'],
    'J': ['N','M'],
    'N' :[],
    'M': ['G'],
    'G': []
}

start_node = 'A'
end_node = 'G'
print("DFS Path:", dfs(graph, start_node, end_node))
path = dfs(graph, start_node, end_node)

# Crear un objeto dirigido de networkx
G = nx.DiGraph()

# Añadir nodos y aristas al grafo
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Dibujar el grafo
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))

# Dibujar nodos y aristas
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Resaltar el camino si existe
if path:
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='lightcoral', node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, arrows=True)
    plt.title(f"Trayectoria DFS de {start_node} a {end_node}\nCamino: {' -> '.join(path)}")
else:
    plt.title("No se encontró un camino")

plt.axis('off')
plt.show()