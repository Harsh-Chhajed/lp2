from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def bfs(self, v):
        visited = [False] * len(self.graph)
        queue = [v]
        visited[v] = True

        while queue:
            curr_node = queue.pop(0)
            print(curr_node, end=' ')

            for neighbor in self.graph[curr_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("Depth-First Search (DFS):")
g.dfs(0, [False] * len(g.graph))

print("\n\nBreadth-First Search (BFS):")
g.bfs(0)
