input_text=open("input1b.txt","r")
output_text=open("output1b.txt","w")

loop=int(input_text.readline())

for i in range (loop):
    calc=0
    final=""
    line=input_text.readline().split()
    if line[2]=="+":
        calc= int(line[1]) + int(line[3].strip())
    elif line[2]=="-":
        calc= int(line[1]) - int(line[3].strip())
    elif line[2]=="/":
        calc= int(line[1]) / int(line[3].strip())
    elif line[2]=="*":
        calc= int(line[1]) * int(line[3].strip())
    final=f"The result of {line[1]} {line[2]} {line[3]} is {calc} \n"
    output_text.write(final)


