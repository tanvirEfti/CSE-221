def dfs(dic,node):
    visited[node]=1
    final.append(node)
    for i in dic[node]:
        if  visited[i] != 1:
            dfs(dic,i)
    return final   
                
        
def graph(dic,lst):
    for i in range (len(lst)):
        if lst[i][0] not in dic:
            dic[lst[i][0]]=lst[i][1]
        else:
            dic[lst[i][0]].append(lst[i][1])
    return dic
        
input=open("Task-03\input3.txt","r")
output=open("Task-03\output3.txt","w")
a=input.readline().split()
path=int(a[0])
total=int(a[1])
lst=[]
for i in range (total):
    lst.append(list(map(int,(input.readline().split()))))
dic={}
for j in range (path+1):
    dic[j]=[]

graph_dic=graph(dic,lst)
visited=[0]*(path+1)
final=[]
dfs_final=dfs(graph_dic,lst[0][0])
output.write(" ".join(list(map(str, dfs_final))))

input.close()
output.close()