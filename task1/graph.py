class Graph:
    """Undirected graph using adjacency list."""

    def __init__(self):
        self._adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self._adjacency:
            self._adjacency[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self._adjacency[u].append(v)
        self._adjacency[v].append(u)

    def get_neighbors(self, vertex):
        return self._adjacency.get(vertex, [])

    def bfs(self, start):
        """Breadth‑first search returning traversal order."""
        visited = set()
        queue = [start]
        result = []
        if start in self._adjacency:
            visited.add(start)
            while queue:
                node = queue.pop(0)
                result.append(node)
                for neighbor in self._adjacency[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return result
