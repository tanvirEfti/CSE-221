input=open("Task-01\input1.txt","r")
output=open("Task-01\output1.txt","w")
a=input.readline().strip().split()
people=int(a[0])
queries=int(a[1])
lst=[]

for i in range (people):
    lst.append(i)
    
lst2=[1]*(people+1)

def path(a):
    if lst[a]==a:
        return a
    return path(lst[a])

def union(a,b):
    u=path(a)
    v=path(b)
    if u!= v:
        lst[u]=v
        lst2[v]+=lst2[u]
    output.write(f"{lst2[v]} \n")

for i in range (queries):
    a,b=[int(i) for i in input.readline().split(" ")]
    union(a,b)   

