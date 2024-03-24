input= open("Task4\input4.txt", "r")
output=open("Task4\output4.txt", "w")
start=[]
end=[] 
a=input.readline()
b=a.split()
task=int(b[0]) 
person=int(b[1]) 
a=input.readlines()   

for i in range(0, task, 1):
    c=a[i].split(" ")
    start.append(int(c[0]))
    end.append(int(c[1].strip()))
      
for i in range(task):
    for j in range(task-i-1):
        if end[j] > end[j+1]:
            end[j], end[j+1] = end[j+1], end[j]
            start[j], start[j+1] = start[j+1], start[j]
   
final_list=[]
for i in range(0,len(start)):
    final_list.append((int(start[i]), int(end[i])))

available=[0]*person 
index=[]
count=0
for i in range(task):
    for j in range(person):
        for k in range(i,task):
            if final_list[k][0] == available[j] and i not in index:
                available[j] = final_list[i][1]
                count+=1  
                index.append(i)
                break        
        if final_list[i][0] > available[j] and i not in index:
            available[j] = final_list[i][1]
            count+=1  
            index.append(i)
            break     
output.write(f'{count}\n')
print(final_list)
