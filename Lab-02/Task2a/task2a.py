input=open("Task2a\input2a.txt","r")
output=open("Task2a\output2a.txt","w")
size1=int(input.readline())
list1=input.readline().split()
size2=int(input.readline())
list2=input.readline().split()
new_list=[]

for i in range(size1):
    list1[i] =int(list1[i])
for j in range(size2):
    list2[j] =int(list2[j])

for i in range (len(list1)):
    new_list.append(list1[i])
for j in range (len(list2)):
    new_list.append(list2[j])
new_list.sort()
for k in new_list:
    output.write(str(k) + " ")
    
input.close()
output.close() 



