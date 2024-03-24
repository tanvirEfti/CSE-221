#!/usr/bin/env python
# coding: utf-8

# In[8]:


input_text=open("input4.txt","r")
output_text=open("output4.txt","w")
n=int(input_text.readline())
a=input_text.readlines()
string=[]
train_name=[]
time=[]
for i in range(0,n):
    t=a[i].strip()
    string.append(t)
    train_name.append(t.split()[0])
    time.append(t.split()[-1])
 
for i in range(len(train_name)):
    for j in range(len(train_name)-i-1):
        if train_name[j] > train_name[j+1]:
            train_name[j], train_name[j+1] = train_name[j+1], train_name[j]
            string[j], string[j+1] = string[j+1], string[j]

        if train_name[j] == train_name[j+1]:
            if time[j] > time[j+1]:
                time[j], time[j+1] = time[j+1], time[j]
                string[j], string[j+1] = string[j+1], string[j]    
for i in range(n):
    output_text.write(f"{string[i]}\n")



# In[ ]:





# In[ ]:




