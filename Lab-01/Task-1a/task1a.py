input_text=open("Task-1a\input1a.txt", "r")
output_text=open("Task-1a\output1a.txt", "w")

loop_time=int(input_text.readline())

for i in range (loop_time):
    odd_even=""
    number=int(input_text.readline())
    if number%2==0:
        odd_even=f"{number} is an Even number.\n"
    else:
        odd_even=f"{number} is an Odd number.\n"
    output_text.write(odd_even)
        






