
graph = {
    1: [2],
    2: [1, 5],
    3: [6],
    4: [6, 7],
    5: [2],
    6: [3, 4, 7],
    7: [4, 6]
}

def is_path_exist(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return True
    visited.add(start)
    for neighbor in  graph.get(start, []):
        if neighbor not in visited:
            if is_path_exist(graph, neighbor, end, visited):
                return True

    return False



start_node = int(input("Start : "))
end_node = int(input("End : "))

if start_node not in graph or end_node not in graph:
    print("Either start node or end node not exist")

else:
    if is_path_exist(graph, start_node, end_node):
        print("True")
    else:
        print("False")