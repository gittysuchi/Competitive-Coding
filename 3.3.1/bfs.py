from collections import deque

def validPath(n, edges, source, destination):

    # Create adjacency list
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Queue for BFS
    queue = deque([source])

    # Keep track of visited nodes
    visited = [False] * n
    visited[source] = True

    while queue:
        node = queue.popleft()

        # Destination found
        if node == destination:
            return True

        # Visit neighbours
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False


n = int(input("Enter number of nodes: "))

m = int(input("Enter number of edges: "))
edges = []

for i in range(m):
    u, v = map(int, input("Enter edge: ").split())
    edges.append([u, v])

source = int(input("Enter source: "))
destination = int(input("Enter destination: "))

print(validPath(n, edges, source, destination))