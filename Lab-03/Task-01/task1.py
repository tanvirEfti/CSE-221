input=open('Task-01\input1.txt', "r") 
output=open('Task-01\output1.txt','w')
a=input.readlines()
size=int(a[0])
arr=a[1].strip().split()
 
def merge(a, b):
    i,j=0,0
    sorted_list=[]
    length=len(a)+len(b)
    for k in range(length):
        if i<len(a) and j<len(b):
            if int(a[i]) < int(b[j]):
                sorted_list.append(a[i])
                i+=1
            else:
                sorted_list.append(b[j])
                j+=1
        else:
            if i < len(a):
                sorted_list.append(a[i])
                i+=1
            else:
                sorted_list.append(b[j])
                j+=1
    return sorted_list

def mergeSort(arr):
    if len(arr)<= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[ :mid])
        a2 = mergeSort(arr[mid: ])
        return merge(a1, a2)

x=mergeSort(arr)
for i in x:
   output.write(str(i)+' ')
   
input.close()
output.close()