nodes = int(input())
edges = []
queue = []
order = []
vis = [False for i in range(nodes+1)]

for i in range(nodes - 1):
    edges.append([int(i) for i in input().split()])
    
lvl = int(input())

def BFS(edges, source):
    queue.append(source)
    vis[source] = True
    order.append(source)
    
    while(len(queue) != 0):
        next_node = queue.pop(0)
        for i in edges:
            if next_node in i:
                i.pop(i.index(next_node))
                temp = i.pop()
                
                if vis[temp] == False:
                    vis[temp] == True
                    queue.append(temp)
                    order.append(temp)
                
BFS(edges, 1)
print(order)
