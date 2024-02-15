def dfs(graph,visited,start): 
    nodes =  ['A','B','C','D','E','F']
    visited[start] = True
    print(nodes[start],end=" ")
    for i in range(len(graph)):
        if graph[start][i]==1 and not visited[i]:
            dfs(graph,visited,i)
graph = [
    [ 1, 0, 1, 0, 0, 1],
    [ 0, 0, 0, 1, 1, 1],
    [ 0, 0, 1, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 1],
    [ 1, 1, 1, 1, 0, 0],
    [ 0, 1, 0, 1, 0, 1]
]
visited = [False] * len(graph)

dfs(graph,visited,0)