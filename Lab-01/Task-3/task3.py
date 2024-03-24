
input_text=open("input3.txt","r")
output_text=open("output3.txt","w")

a=input_text.readlines()
loop=int(a[0])
ids=a[1].split(" ")
numbers=a[2].split(" ")

for i in range (loop):
    ids[i]=int(ids[i])
for i in range (loop):
    numbers[i]=int(numbers[i])

for i in range (loop):
    min = i 
    for j in range (i+1,loop):
        if numbers[min]<numbers[j]:
            min = j
        if numbers[min]==numbers[j]:
            if ids[min] > ids[j]:
                min = j
    numbers[i],numbers[min]= numbers[min], numbers[i]
    ids[i], ids[min] = ids[min], ids[i]

for i in range (loop):
    output_text.write(f"ID:{ids[i]} Mark:{numbers[i]}\n")


# In[ ]:





# In[ ]:




