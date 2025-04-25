graph = {
    'A': [('B', 2), ('C', 1)],          
    'B': [('E', 6), ('D', 4), ('A', 2)],
    'C': [('G', 2), ('F', 5), ('A', 1)],
    'D': [('H', 3), ('B', 4)],
    'E': [('I', 2), ('B', 6)],
    'F': [('C', 5)],
    'G': [('J', 7), ('C', 2)],
    'H': [('D', 3)],
    'I': [('K', 1), ('J', 4), ('E', 2)],
    'J': [('I', 4), ('G', 7)],
    'K': [('I', 1)]
}

def dfs_custom(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        if current == goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor, _ in reversed(graph[current]): 
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        for neighbor, weight in graph[path[i]]:
            if neighbor == path[i + 1]:
                cost += weight
                break
    return cost

# Run DFS
start_node = 'A'
goal_node = 'K'
path = dfs_custom(graph, start_node, goal_node)

if path:
    total_cost = calculate_path_cost(graph, path)
    print("DFS Path from A to K:", " -> ".join(path))
    print(" Path Cost:", total_cost)
else:
    print(f"No path found from {start_node} to {goal_node}.")