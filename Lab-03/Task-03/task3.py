input=open("Task-03\input3.txt","r")
output=open("Task-03\output3.txt","w")
alien=int(input.readline())
list=input.readline().strip().split()

for i in range (alien):
    list[i]=int(list[i])
    
pair_count=0

def compare(a, b):
    if a>b:
        return 0
    else:
        return 1
    
def mergeSort(arr, ref):
    if len(arr) <= 1:
        return compare(arr[0], ref)
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid],ref) 
        a2 = mergeSort(arr[mid:],ref)
        return a1+a2

for i in range(0,alien-1,1):
    pair_count+=mergeSort(list[i+1:],list[i])
output.write(str(pair_count))

input.close()
output.close()