import heapq as h

def p(d, c):
    P = []
    while c in d:
        P.append(c)
        c = d[c]
    P.append(c)
    return P[::-1]

def a(g, s, z, H):
    G = {n: float('inf') for n in g}
    G[s] = 0
    F = {n: float('inf') for n in g}
    F[s] = H[s]
    Q = [(F[s], s)]
    D = {}

    while Q:
        f, u = h.heappop(Q)

        if u == z:
            return p(D, u), G[u]

        for v, w in g.get(u, []):
            t = G[u] + w

            if t < G.get(v, float('inf')):
                D[v] = u
                G[v] = t
                F[v] = t + H.get(v, 0)
                h.heappush(Q, (F[v], v))

    return None, float('inf')

# Example Graph
G_DATA = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 2), ('C', 1)],
    'C': [('E', 3)],
    'D': [('G', 1)],
    'E': [('G', 1)],
    'G': []
}

# Heuristic
H_DATA = {
    'A': 5, 'B': 4, 'C': 3, 'D': 1, 'E': 1, 'G': 0
}

S = 'A'
Z = 'G'

path, cost = a(G_DATA, S, Z, H_DATA)

if path:
    print(f"Path: {' -> '.join(path)}, Cost: {cost}")
else:
    print("Path not found.")