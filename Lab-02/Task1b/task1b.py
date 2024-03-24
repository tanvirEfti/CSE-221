input=open("Task1b\input1b.txt","r")
output=open("Task1b\output1b.txt","w")

string=[]
a=input.readline().split()
loop=int(a[0])
target=int(a[1])
b=input.readline().split()
for i in range (loop):
    b[i]=int(b[i])
i=0
j=(len(b))-1
while (i < j and i!=j):
    if i == j:
        output.write('IMPOSSIBLE')         
        break
    if b[i] + b[j] == target:
        string.append(i+1)
        string.append(j+1)
        break
    if b[i] + b[j] < target:
        i+=1
    if b[i] + b[j] > target:
        j-=1


if string==[]:
    output.write("IMPOSSIBLE")
else:
    for j in string:
        output.write(str(j) + " ")

input.close()
output.close() 

        
    
