import numpy as np

n = 9
g = np.full((n, n), float('inf'))

paths = [
    (1, 2, 4), (1, 5, 1), (1, 7, 2),
    (2, 3, 7), (2, 6, 5),
    (3, 4, 1), (3, 6, 8),
    (4, 6, 6), (4, 7, 4), (4, 8, 3),
    (5, 6, 9), (5, 7, 10),
    (6, 9, 2),
    (7, 9, 8),
    (8, 9, 1),
    (9, 8, 7)
]

for a, b, w in paths:
    g[a - 1][b - 1] = w


def fmt(x):
    return ' inf' if x == float('inf') else f'{int(x):4d}'


matrix = np.array2string(g, formatter={'all': fmt}, separator=' ', max_line_width=120)

print("Adjacency Matrix for Undirected and Weighted Graph:")
print(matrix)


def prim(g, n, root):
    seen = [False] * n
    seen[root] = True
    tree = []
    cost = 0

    while len(tree) < n - 1:
        best = (float('inf'), -1, -1)
        for i in range(n):
            if seen[i]:
                for j in range(n):
                    if not seen[j] and g[i][j] < best[0]:
                        best = (g[i][j], i, j)

        w, a, b = best
        tree.append((a + 1, b + 1, w))
        cost += w
        seen[b] = True

    return tree, cost


class Sets:
    def __init__(self, n):
        self.p = list(range(n))
        self.h = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def join(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.h[rx] > self.h[ry]:
                self.p[ry] = rx
            elif self.h[rx] < self.h[ry]:
                self.p[rx] = ry
            else:
                self.p[ry] = rx
                self.h[rx] += 1


def kruskal(g, n):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if g[i][j] != float('inf'):
                edges.append((g[i][j], i, j))

    edges.sort()
    sets = Sets(n)
    tree = []
    cost = 0

    for w, a, b in edges:
        if sets.find(a) != sets.find(b):
            sets.join(a, b)
            tree.append((a + 1, b + 1, w))
            cost += w

    return tree, cost


start = int(input("\nEnter the root node for Prim's algorithm: ")) - 1

p_tree, p_cost = prim(g, n, start)
k_tree, k_cost = kruskal(g, n)

print("\nPrim's Algorithm MST:")
for a, b, w in p_tree:
    print(f"Edge: {a} - {b}, Weight: {w}")
print(f"Total weight of MST: {p_cost}")

print("\nKruskal's Algorithm MST:")
for a, b, w in k_tree:
    print(f"Edge: {a} - {b}, Weight: {w}")
print(f"Total weight of MST: {k_cost}")