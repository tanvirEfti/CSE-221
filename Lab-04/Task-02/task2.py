def bfs(dic,node):
    visited=[]
    queue=[]
    final=[]
    queue.append(node)
    visited.append(node)
    while len(queue)!=0:
        elem=queue.pop(0)
        final.append(elem)
        for i in dic[elem]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return final
        
def graph(dic,lst):
    for i in range (len(lst)):
        if lst[i][0] not in dic:
            dic[lst[i][0]]=lst[i][1]
        else:
            dic[lst[i][0]].append(lst[i][1])
    return dic
        
input=open("Task-02\input2.txt","r")
output=open("Task-02\output2.txt","w")
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

bfg_list=bfs(graph_dic,lst[0][0])
output.write(" ".join(list(map(str, bfg_list))))

input.close()
output.close()