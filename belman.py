def bellman_ford(graph, num_vertices, start_vertex):

    distances = [float('inf')] * num_vertices
    distances[start_vertex] = 0

    for _ in range(num_vertices - 1):
        for u, v, w in graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in graph:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return "Граф содержит отрицательный цикл"

    return distances

if __name__ == "__main__":
    graph = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    num_vertices = 5
    start_vertex = 0
    result = bellman_ford(graph, num_vertices, start_vertex)
    if isinstance(result, str):
        print(result)
    else:
        print("Кратчайшие расстояния от вершины", start_vertex, ":")
        for i, d in enumerate(result):
            print(f"Вершина {i}: {d}")
