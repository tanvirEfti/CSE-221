input=open("Task-01\input4.txt","r")
output=open("Task-01\output4.txt","w")
a=input.readline().strip().split()
vertics=int(a[0])
edges=int(a[1])

matrix= [[0]*(vertics+1) for i in range (vertics+1)]

for i in range (edges):
    a=input.readline().strip().split()
    x=int(a[0])
    y=int(a[1])
    matrix[x][y]=int(a[2])
for i in range (vertics+1):
    for j in range (vertics+1):
        output.write(f"{matrix[i][j]} " )
    output.write("\n")
    
input.close()
output.close()