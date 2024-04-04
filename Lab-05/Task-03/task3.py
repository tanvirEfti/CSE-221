def transpose_graph(dic):
    transposed = {}
    for i in dic:
        for neighbor in dic[i]:
            if neighbor not in transposed:
                transposed[neighbor] = [i]
            else:
                transposed[neighbor].append(i)
        if i not in transposed: 
            transposed[i] = []
    return transposed

def dfs(dic, visited, node, stack):
    visited[node] = True
    for neighbor in dic.get(node, []):
        if not visited[neighbor]:
            dfs(dic, visited, neighbor, stack)
    stack.append(node)

def dfs_reverse(dic, visited, node, scc):
    visited[node] = True
    scc.append(node)
    for neighbor in dic.get(node, []):
        if not visited[neighbor]:
            dfs_reverse(dic, visited, neighbor, scc)

def kosaraju(graph):
    visited = {}
    for node in graph:
        visited[node] = False
    stack = []
    for node in graph:
        if not visited[node]:
            dfs(graph, visited, node, stack)
    transposed = transpose_graph(graph)
    visited = {}
    for node in transposed:
        visited[node] = False
    scc_lst = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs_reverse(transposed, visited, node, scc)
            scc_lst.append(scc)
    return scc_lst

def graph(dic,lst):
    for i in range (len(lst)):
        if lst[i][0] in dic:
            dic[lst[i][0]].append(lst[i][1])
        else:
            dic[lst[i][0]]=(lst[i][1])
    return dic

input = open("Task-03\input3.txt", "r")
output = open("Task-03\output3.txt", "w")
a=input.readline().split()
vertics=int(a[0])
edges=int(a[1])
dic={}
lst=[]
for i in range (edges):
    lst.append(list(map(int,(input.readline().split()))))
for i in range (1,vertics+1,1):
    dic[i]=[]
graph_dic=graph(dic,lst)
scc_result = kosaraju(graph_dic)

for scc in scc_result:
    output.write(" ".join(map(str, scc)) + "\n")

input.close()
output.close()