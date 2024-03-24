def shortestPath(dic, start, end):
    paths = [[start]]
    visited = [start]
    if start == end:
        return [start]
        
    while len(paths)>0:
        current = paths[0]
        last = current[-1]
        paths.pop(0)
        nexts = dic[last]
        
        if end in nexts:
            current.append(end)
            return current
       
        for node in nexts:
            if not node in visited:
                new_path = list(current)
                new_path.append(node)
                paths.append(new_path)
                visited.append(node)
    return []


def graph(dic,lst):
    for i in range(len(lst)):
       dic[lst[i][0]].append(lst[i][1])
       dic[lst[i][1]].append(lst[i][0])
    return dic


input=open("Task-05\input5.txt","r")
output=open("Task-05\output5.txt","w")
a=input.readline().strip().split()
cities=int(a[0])
roads=int(a[1])
dest=int(a[2])
dic={}
for i in range (cities+1):
    dic[i]=[]
lst=[]

for i in range(roads):
    lst.append(list(map(int,(input.readline().split()))))
graph_dic=graph(dic,lst)

path = shortestPath(graph_dic, 1, dest)

output.write("TIME: "+str(len(path)-1)+"\n")
output.write("Shortest Path: "+" ".join(list(map(str, path))))

input.close()
output.close()