input=open("Task2b\input2a.txt","r")
output=open("Task2b\output2b.txt","w")
size1=int(input.readline())
list1=input.readline().strip().split()
size2=int(input.readline())
list2=input.readline().strip().split()
new_list=[]

for i in range(size1):
    list1[i] =int(list1[i])
for j in range(size2):
    list2[j] =int(list2[j])

i=0
j=0    
while i<size1 and j<size2:
    if list1[i]<list2[j]:
        new_list.append(list1[i])
        i+=1
    elif list1[i]>list2[j]:
        new_list.append(list2[j])
        j+=1
    elif list1[i]==list2[j]:
        new_list.append(list1[i])
        new_list.append(list2[j])
        i+=1
        j+=1
while i<=size1-1 or j<=size2-1: 
    if i<=size1-1:
        new_list.append(list1[i])
        i+=1
    elif j<=size2-1:
        new_list.append(list2[j])
        j+=1
        
for k in new_list:
    output.write(str(k)+ ' ')   

input.close()
output.close() 


