input=open("Task-04\input4.txt","r")
output=open("Task-04\output4.txt","w")
size=int(input.readline().strip())
a=input.readlines()
arr=list(map(int,a[0].strip().split()))
def get_max(arr):
    if len(arr) == 2:
        return arr[0] + (arr[1])**2 
    elif len(arr) == 1:
        return float('-inf')
    mid=len(arr)//2
    left_val = get_max(arr[ :mid])
    right_val = get_max(arr[mid: ])

    left_arr = arr[ :mid]
    right_arr = arr[mid:]
    left_max = max(left_arr)
            
    for i in range(len(right_arr)):
        right_arr[i] = right_arr[i]**2  
    right_max = max(right_arr)
    total = left_max + right_max 
    return max(left_val,right_val,total)

output.write(f"{str(get_max(arr))}")

input.close()
output.close()