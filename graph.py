
from collections import deque

# Create Graph
class Graph:
    def __init__(self):
        self.graph = {
            "L": ["A", "P"],
            "A": ["L", "I", "Z"],
            "P": ["L", "Z"],
            "I": ["A", "Z"],
            "Z": ["A", "I", "P"]
        }

    # Display Graph
    def display_graph(self):
        print("Graph Connections:")

        for vertex in self.graph:
            neighbors = sorted(self.graph[vertex])
            print(vertex, "->", neighbors)

    # BFS - Breadth First Search
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        visited.add(start)

        print("BFS Traversal:", end=" ")

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in sorted(self.graph[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()

    # DFS - Depth First Search
    def dfs(self, vertex, visited):
        visited.add(vertex)

        print(vertex, end=" ")

        for neighbor in sorted(self.graph[vertex]):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# MAIN METHOD
def main():
    g = Graph()

    print("GRAPH - LAPIZ")
    print("-------------")

    g.display_graph()

    print()

    g.bfs("L")

    print("DFS Traversal:", end=" ")
    g.dfs("L", set())

    print()


if __name__ == "__main__":
    main()
