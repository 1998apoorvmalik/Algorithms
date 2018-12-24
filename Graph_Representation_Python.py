nodes, edges = map(int, input().split())

adj_list = []
for _ in range(nodes):
    adj_list.append([])
    
for _ in range(edges):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)
