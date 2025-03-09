from typing import List
class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]
    def add_edge(self, u: int, v: int):
        if self.no_edge(u, v):
            self.adjacency_list[u].append(v)
    def no_edge(self, u: int, v: int):
        return v not in self.adjacency_list[u]
class WCC:
    def __init__(self, directed_graph: Graph):
        self.directed_graph = directed_graph
    def connected_components(self, undirected_graph: Graph):
        connected_components = []
        is_visited = [False for _ in range(undirected_graph.vertices)]
        for i in range(undirected_graph.vertices):
            if not is_visited[i]:
                component = []
                self.find_connected_component(i, is_visited, component, undirected_graph)
                connected_components.append(component)
        return connected_components
    def find_connected_component(self, src: int, is_visited: List[bool], component: List[int], undirected_graph: Graph):
        is_visited[src] = True
        component.append(src)
        for v in undirected_graph.adjacency_list[src]:
            if not is_visited[v]:
                self.find_connected_component(v, is_visited, component, undirected_graph)
    def weakly_connected_components(self):
        undirected_graph = Graph(self.directed_graph.vertices)
        for u in range(self.directed_graph.vertices):
            for v in self.directed_graph.adjacency_list[u]:
                undirected_graph.add_edge(u, v)
                undirected_graph.add_edge(v, u)
        return self.connected_components(undirected_graph)
class SCC:
    def __init__(self, directed_graph: Graph):
        self.directed_graph = directed_graph
    def dfs(self, curr, des, adj, vis):
        if curr == des:
            return True
        vis[curr] = 1
        for x in adj[curr]:
            if not vis[x]:
                if self.dfs(x, des, adj, vis):
                    return True
        return False
    def is_path(self, src, des, adj):
        vis = [0] * (len(adj))
        return self.dfs(src, des, adj, vis)
    def find_scc(self):
        n = self.directed_graph.vertices
        ans = []
        is_scc = [0] * n
        adj = self.directed_graph.adjacency_list
        for i in range(n):
            if not is_scc[i]:
                scc = [i]
                for j in range(i + 1, n):
                    if not is_scc[j] and self.is_path(i, j, adj) and self.is_path(j, i, adj):
                        is_scc[j] = 1
                        scc.append(j)
                ans.append(scc)
        return ans
def build_graph_from_adjacency_matrix(matrix: List[List[int]]) -> Graph:
    vertices = len(matrix)
    graph = Graph(vertices)
    for i in range(vertices):
        for j in range(vertices):
            if matrix[i][j] == 1:
                graph.add_edge(i, j)
    return graph

adjacency_matrix = [
[0, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0, 1],
[0, 0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 0, 1, 1],
[0, 0, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
]
directed_graph = build_graph_from_adjacency_matrix(adjacency_matrix)
weakly_connected_components = WCC(directed_graph).weakly_connected_components()
for index, component in enumerate(weakly_connected_components, start=1):
    print("Weakly Connected Component {}: {}".format(index, component))
strongly_connected_components = SCC(directed_graph).find_scc()
print("\nStrongly Connected Components:")
for index, component in enumerate(strongly_connected_components, start=1):
    print(f"Component {index}: {[node + 1 for node in sorted(component)]}")
