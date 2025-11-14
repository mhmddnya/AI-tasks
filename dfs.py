def dfs(graph, start):
    visited = {node: False for node in graph}
    parent = {start: None}
    stack = [start]

    while stack:
        current = stack.pop()
        if not visited[current]:
            path = []
            temp = current
            while temp is not None:
                path.append(temp)
                temp = parent[temp]
            path.reverse()
            print("Path to", current, ":", path)

            visited[current] = True
            
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    parent[neighbor] = current
                    stack.append(neighbor)


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

dfs(graph, 0)
