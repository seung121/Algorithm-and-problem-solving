parent = dict()
rank = dict()

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return sorted(minimum_spanning_tree)

graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
'edges': set([
(7, 'A', 'B'),
(5, 'A', 'H'),
(8, 'A', 'J'),
(9, 'B', 'C'),
(7, 'B', 'F'),
(8, 'B', 'G'),
(5, 'B', 'I'),
(5, 'C', 'D'),
(9, 'C', 'F'),

(6, 'C', 'H'),
(7, 'D', 'E'),
(5, 'D', 'G'),
(7, 'E', 'F'),
(8, 'F', 'G'),
(9, 'G', 'H'),
(6, 'G', 'J'),
(8, 'H', 'I'),
(11, 'I', 'J'),
(9, 'J', 'B'),
])
}
print(kruskal(graph))