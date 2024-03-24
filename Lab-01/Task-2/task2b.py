#!/usr/bin/env python
# coding: utf-8

# In[2]:


input_text=open("input2b.txt","r")
output_text=open("output2b.txt", "w")

a=input_text.readlines()
b=a[1].split(" ")

for i in range (int(a[0])):
    b[i]=int(b[i])

def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag=False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag=True
        if flag == False:
            break
    return arr

for i in (bubbleSort(b)):
    output_text.write(f"{i} ")


# In[ ]:




