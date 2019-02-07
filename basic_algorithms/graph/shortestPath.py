def minDistance(dist, sptSet, numOfVertices):
    minimum = float('inf')
    minIndex = 0
    for i in range(numOfVertices):
        if sptSet[i] == False and dist[i] <= minimum:
            minimum, minIndex = dist[i], i

    return minIndex



def dijkstra(graph, numOfVertices, src):
    dist, sptSet = [float('inf')] * numOfVertices, [False] * numOfVertices
    dist[src] = 0
    for i in range(numOfVertices - 1):
        u = minDistance(dist, sptSet, numOfVertices)
        sptSet[u] = True
        for v in range(numOfVertices):
            if sptSet[v] == False and graph[u][v] and dist[u] != float('inf') \
                and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    return dist


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
print dijkstra(graph, len(graph), 0)
