def dfs(graph, visited, node):
    visited[node] = True
    for nextNode in graph[node]:
        if visited[nextNode]:
            continue
        dfs(graph, visited, nextNode)

def topologicalSort(graph):
    numOfComponets = 0
    numOfNodes = len(graph)
    visited = [False] * numOfNodes
    for i in range(numOfNodes):
        if visited[i] == False:
            dfs(graph, visited, i)
            numOfComponets += 1
    return numOfComponets

def buildGraph(n, connections):
    graph = [[] for _ in range(n)]
    for connection in connections:
        graph[connection[0]].append(connection[1])
        graph[connection[1]].append(connection[0])

    return graph


n = 5
connections = [[0,2], [1,3],[3,4]]
graph = buildGraph(n, connections)
print topologicalSort(graph)
