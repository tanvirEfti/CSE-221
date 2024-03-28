def dfs(dic,i,v,arr):
    v.append(i)
    final.append(i)
    for j in dic[i]:
        arr[j] -= 1
        if j not in visited and arr[j] == 0:
            dfs(dic, j, visited, arr)
   
    
def graph(dic,lst):
    for i in range (len(lst)):
        if lst[i][0] in dic:
            dic[lst[i][0]].append(lst[i][1])
        else:
            dic[lst[i][0]]=(lst[i][1])
    return dic

input=open("Task-01(a)\input1a.txt","r")
output=open("Task-01(a)\output1a.txt","w")
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
arr=[0]*(vertics+1)
visited=[]
final=[]
for i in range (len(lst)):
    arr[lst[i][1]] = arr[lst[i][1]] + 1
    
for i in range(1,vertics+1):
    if arr[i] == 0 and i not in visited:
        dfs(graph_dic,i,visited,arr)
if len(final)<vertics:
    output.write ("IMPOSSIBLE")   
else:
    output.write(" ".join(list(map(str,final))))
