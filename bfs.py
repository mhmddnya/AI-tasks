from queue import Queue

def bfs(graph, start):
    q = Queue()
    q.put(start)
    visited = {node: False for node in graph}
    visited[start] = True
    parent = {start: None}

    while not q.empty():
        node = q.get()

        path = []
        temp = node
        while temp is not None:
            path.append(temp)
            temp = parent[temp]
        path.reverse()
        print("Path to", node, ":", path)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                q.put(neighbor)


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

bfs(graph, 0)
