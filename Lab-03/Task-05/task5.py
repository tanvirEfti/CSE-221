input=open("Task-05\input5.txt","r")
output=open("Task-05\output5.txt","w")
a=input.readlines()
size=int(a[0].strip())
arr=list(map(int,a[1].split()))

def partition(arr,l,h):
    pivot = arr[h]
    x = l - 1
    for i in range(l,h):
        if arr[i] <= pivot:
                x+=1
                arr[x],arr[i] = arr[i],arr[x]
    arr[x+1],arr[h] = arr[h],arr[x+1]
    return x+1
      
def quicksort(arr, l, h):
    if l < h:
        p = partition(arr,l,h)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,h)

quicksort(arr,0,size-1)   

for i in range (len(arr)):
    output.write(f"{arr[i]} ")

input.close()
output.close()