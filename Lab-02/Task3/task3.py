input=open("Task3\input3.txt","r")
output=open("Task3\output3.txt","w")
loop=int(input.readline())
start=[]
end=[]
a=input.readlines()
for i in range (0, loop, 1):
    b=a[i].split(" ")
    start.append(int(b[0]))
    end.append(int((b[1]).strip()))

for i in range(0,loop):   
    min = i
    for j in range(i+1, loop):    
        if end[min] > end[j]:     
            min = j
        if end[min] == end[j]:
            if start[min] < start[j]:
                min = j
    end[i], end[min] = end[min], end[i]
    start[i], start[min] = start[min], start[i]

last_time=0
final_list=[]
for i in range (loop):
    if i == loop-1:
        if last_time<=start[i]:
            final_list.append( [start[i],end[i]])
        else:
            pass        
    elif end[i]<=end[i+1]:
        if last_time<=start[i]:
            final_list.append( [start[i],end[i]])
            last_time=end[i]
        else:
            pass
           
output.write(f'{len(final_list)}\n')     
for k in range  (len(final_list)):
    output.write (f'{final_list[k][0]} {final_list[k][1]} \n')
           