# NON LINEAR DATASTRUCTURE-GRAPH
# BREADTH FIRST SEARCH(BFS)

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':['H'],
    'F':[],
    'G':[],
    'H':[],
}                               # graph data is represented using dictionary

visited=[]   #list to keep track of visited nodes
queue=[]    # Initialize a queue
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:            # loop executes until queue is empty
        s=queue.pop(0)
        print(s,'->',end=' ')
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited,graph,'A')   #calling function
