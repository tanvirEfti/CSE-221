input=open("input.txt","r")
output=open("output.txt","w")
size=int(input.readline())
arr=list(map(int,input.readline().split()))
total_queries=int(input.readline())
queries=[]

def partition(A,p,r):
    pivot = A[r]
    i = p - 1
    for j in range(p,r):    
        if A[j]<=pivot:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def Quickselect(A,p,r,k):
    if p<=r:
        q=partition(A,p,r)
        if q==k-1: 
            return A[q]
        elif q>k-1:
            return Quickselect(A,p,q-1,k)
        else:
            return Quickselect(A,q+1,r,k)

for i in range(total_queries):
    queries.append(int(input.readline()))

for i in queries:
    kth_smallest=Quickselect(arr,0,size-1,i) 
    output.write(f"{kth_smallest}\n")

input.close()
output.close()
