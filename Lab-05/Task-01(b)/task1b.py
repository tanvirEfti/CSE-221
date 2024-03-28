def bfs(dic,arr):
    count=0
    queue=[]
    final=[]
    for i in dic:
       if arr[i]==0:
           queue.append(i)
    while queue:
        elem=queue.pop(0)
        count+=1
        final.append(elem)
        for j in dic[elem]:
            arr[j]=arr[j]-1
            if arr[j]==0:
                queue.append(j)
            
        
    if count != len(dic):
        return("IMPOSSIBLE")
    else:
        return final         
    
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
print(dic)
arr=[0]*(vertics+1)
for i in range (len(lst)):
    arr[lst[i][1]] = arr[lst[i][1]] + 1
f=bfs(dic,arr)
output.write(" ".join(list(map(str,f))))
