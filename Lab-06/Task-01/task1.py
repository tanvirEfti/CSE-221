import math
import heapq as hp

def djikstra(dic,s):
    queue=[]
    dist=[math.inf]*len(dic)
    dist[s]=0
    hp.heappush(queue,(dist[s],s))
    visited=[False]*len(dic)
    prev=[None]*len(dic)   

    while queue:
        loc,val=hp.heappop(queue)
        if visited[val]==True:
            continue
        visited[val]=True
        for v,c in dic[val]:
            alt = dist[val] + c
            if alt<dist[v]:
                dist[v] = alt
                prev[v] = val
                hp.heappush(queue, (dist[v], v))

    dist.pop(0)
    while math.inf in dist:
        idx = dist.index(math.inf)
        dist[idx] = -1
    return dist

input=open("Task-01\input1.txt","r")
output=open("Task-01\output1.txt","w")
a=input.readline().strip().split(" ")
node=int(a[0])
edge=int(a[1])
dic={i:[] for i in range (node+1)}
lst=[]
for i in range (edge):
    lst.append(list(map(int,(input.readline().split()))))
for i in range (len(lst)):
    if lst[i][0] in dic:
        dic[lst[i][0]].append([lst[i][1],lst[i][2]])
source=int(input.readline())
f=djikstra(dic,source)
 
output.write(" ".join(list(map(str,f))))

input.close()
output.close()