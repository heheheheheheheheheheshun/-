#借助大模型
from collections import deque


def has_bst_with_max_b(G, b):
    # G: adjacency list, e.g., {u: [(v, w), ...]}
    # Step 1: Build subgraph with edges where w <= b
    subgraph = {u: [] for u in G}
    for u in G:
        for (v, w) in G[u]:
            if w <= b:
                subgraph[u].append(v)

    # Step 2: Check connectivity via BFS
    if not subgraph:
        return False
    visited = set()
    queue = deque([next(iter(subgraph))])
    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.add(u)
            for v in subgraph[u]:
                if v not in visited:
                    queue.append(v)
    return len(visited) == len(G)


# Example usage
G = {0: [(1, 1), (2, 3)], 1: [(0, 1), (2, 2)], 2: [(0, 3), (1, 2)]}
print(has_bst_with_max_b(G, 2))
print(has_bst_with_max_b(G, 1))