def fibonacci(n):
    if lst[n]:
        return lst[n]
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
      c=fibonacci(n-1) + fibonacci(n-2)
      lst[n]=c 
      return c
   


input=open("Task-03\input3.txt","r")
output=open("Task-03\output3.txt","w")
a=int(input.readline())
lst={i:[] for i in range (a+2)}
f1=fibonacci(a+1)
output.write((str(f1)))

