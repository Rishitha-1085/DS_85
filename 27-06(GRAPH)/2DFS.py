# DEPTH FIRST SEARCH(DFS)
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':['H'],
    'F':[],
    'G':[],
    'H':[],
}                               
print(graph)
visited=set()   # set to keep track of visited
def dfs(visited,graph,node):
    if node not in visited:
        visited.add(node)
        print(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)  # recursive call

dfs(visited,graph,'A')  #calling function