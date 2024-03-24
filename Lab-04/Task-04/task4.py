def dfs(dic,i,visited,stack):
    visited[i]=True
    stack[i]=True
    for j in dic[i]:
        if not visited[j]:
            if dfs(dic,j,visited,stack):
                return True
        elif stack[j]:
            return True
    stack[i]=False
    return False
    
def isCyclic(dic):
    for i in range (len(dic)):
        if dfs(dic,i,visited,stack):
            return True
    return False
    
def graph(dic,lst):
    for i in range (len(lst)):
        if lst[i][0] not in dic:
            dic[lst[i][0]]=lst[i][1]
        else:
            dic[lst[i][0]].append(lst[i][1])
    return dic
        
input=open("Task-04\input4.txt","r")
output=open("Task-04\output4.txt","w")
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
visited=[False]*(path+1)
stack=[False]*(path+1)
a=isCyclic(graph_dic)
if a == True:
    output.write("YES")
else:
    output.write("NO")

input.close()
output.close()