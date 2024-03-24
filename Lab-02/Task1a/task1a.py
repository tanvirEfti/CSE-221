input=open("Task1a\input1a.txt","r")
output=open("Task1a\output1a.txt","w")

string=[]
a=input.readline().split()
loop=int(a[0])
target=int(a[1])
b=input.readline().split()
for i in range (loop):
    b[i]=int(b[i])
    

for i in range (0, len(b), 1):
    left=b[i]
    for j in range (i+1, len(b), 1):
        if left + b[j] ==  target:
            string.append(i+1)
            string.append(j+1)
            break
        else:
            continue
    if string == []:
        continue
    else:
        break

if string == []:
    output.write("IMPOSSIBLE")
else:
    for i in string:
        output.write(str(i) + " ")
            
input.close()
output.close() 
