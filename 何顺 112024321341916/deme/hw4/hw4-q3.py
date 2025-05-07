#借助大模型
def find_optimal_road(G, E_prime):
    # Step 1: Compute all-pairs shortest paths in G using Floyd-Warshall
    n = len(G.V)
    d = [[float('inf')] * n for _ in range(n)]
    for u in G.V:
        d[u][u] = 0
    for (u, v, l) in G.E:
        d[u][v] = l

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    # Step 2: Iterate over all candidate roads (u, v) in E'
    max_reduction = 0
    best_s, best_t = None, None
    best_road = None

    for (u, v, l_prime) in E_prime:
        for s in G.V:
            for t in G.V:
                new_dist = d[s][u] + l_prime + d[v][t]
                if new_dist < d[s][t]:
                    reduction = d[s][t] - new_dist
                    if reduction > max_reduction:
                        max_reduction = reduction
                        best_s, best_t = s, t
                        best_road = (u, v)

    return (best_s, best_t, best_road, max_reduction)