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

input=open("Task-02\input2.txt","r")
output=open("Task-02\output2.txt","w")
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
b=input.readline().strip().split()
s1=int(b[0])
s2=int(b[1])

f1=djikstra(dic,s1)
f2=djikstra(dic,s2)
print(f1,f2)
time=math.inf
node=math.inf

for i in range (len(f1)):
    if f1[i] in [0,-1] or f2[i] in [0,-1]:
        continue
    max_time=max(f1[i],f2[i])
    if max_time<time:
        time=max_time
        node=i+1
        
if time == math.inf:
    output.write(f"IMPOSSIBLE")
else:
    output.write(f"Time {time} \nNode {node}")
    
input.close()
output.close()