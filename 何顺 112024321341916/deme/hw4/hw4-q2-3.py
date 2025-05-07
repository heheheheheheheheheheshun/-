#借助大模型
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root


def find_bottleneck_spanning_tree(G):
    # Step 1: Collect all edges and sort by weight
    edges = []
    for u in G:
        for (v, w) in G[u]:
            if u < v:  # Avoid duplicate edges
                edges.append((w, u, v))
    edges.sort()  # O(|E| log |E|), but can be O(|E|) with radix sort

    # Step 2: Kruskal-like algorithm to find BST
    uf = UnionFind(len(G))
    max_weight = 0
    for w, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            max_weight = w
            if sum(uf.find(u) == u for u in range(len(G))) == 1:
                break  # All connected
    return max_weight


#e.g
G = {0: [(1, 1), (2, 3)], 1: [(0, 1), (2, 2)], 2: [(0, 3), (1, 2)]}
print(find_bottleneck_spanning_tree(G))