input=open("Task-02\input2.txt","r")
output=open("Task-02\output2.txt","w")
item=int(input.readline())
list=input.readline().strip().split()

for i in range (item):
    list[i]=int(list[i])

def merge(arr):
    if len(arr)<=1:
        return int(arr[0])
    else:
        mid=(len(arr))//2
        a1 = merge(arr[ :mid])
        a2 = merge(arr[mid: ])
        if int(a1) > int(a2):
            return a1
        else:
            return a2

sort=merge(list)

output.write(str(sort))

input.close()
output.close()