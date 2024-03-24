input=open("Task-01(b)\input1b.txt","r")
output=open("Task-01(b)\output1b.txt","w")
a=input.readline().strip().split()
vertics=int(a[0])
edges=int(a[1])
dict={}

for i in range (vertics+1):
    dict[i]=[]
for i in range (edges):
    a=input.readline().strip().split()
    if int(a[0]) in dict:
        dict[int(a[0])].append(((int(a[1])), (int(a[2]))))
    else:
        dict[int(a[0])]=((int(a[1])), (int(a[2])))

for i in range (len(dict)):
    output.write(f"{i} : ")
    for j in (dict[i]):
        output.write(f"{j} ")
    output.write("\n")

input.close()
output.close()