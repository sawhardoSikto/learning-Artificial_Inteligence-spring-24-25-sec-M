from collections import deque


graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('A', 2), ('D', 4), ('E', 6)],
    'C': [('A', 1), ('F', 5), ('G', 2)],
    'D': [('B', 4), ('H', 3)],
    'E': [('B', 6), ('I', 2)],
    'F': [('C', 5)],
    'G': [('C', 2), ('J', 7)],
    'H': [('D', 3)],
    'I': [('E', 2), ('J', 4), ('K', 1)],
    'J': [('G', 7), ('I', 4)],
    'K': [('I', 1)]
}

def bfs(graph, start, goal):
    queue = deque([(start, [start])])  
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        
        visited.add(current)
        for neighbor, _ in graph[current]:
            if neighbor not in visited and neighbor not in [p[0] for p in queue]:
                queue.append((neighbor, path + [neighbor]))
    
    return None

def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        for neighbor, weight in graph[path[i]]:
            if neighbor == path[i+1]:
                cost += weight
                break
    return cost


start_node = 'A'
goal_node = 'K'
path = bfs(graph, start_node, goal_node)

if path:
    total_cost = calculate_path_cost(graph, path)
    print("Path from A to K:", " -> ".join(path))
    print("Total path cost:", total_cost)
else:
    print("No path found from", start_node, "to", goal_node)