from collections import deque

def depth_first_search(graph, start_node):
    visited = set()
    
    def dfs(node):
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)

    dfs(start_node)

def breadth_first_search(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

example_graph = {'1': {'3', '4'}, '2': {'1', '3'}, '3': {'4'}, '4': {'1', '2'}}

print("Depth First Search: ")

depth_first_search(example_graph, '1')

print("\n")

print("Breadth First Search: ")

breadth_first_search(example_graph, '1')