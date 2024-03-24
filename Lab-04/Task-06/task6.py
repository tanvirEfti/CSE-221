def DFS_FloodFill(r, c, rows, cols, lst):
    if r < 0 or r >= rows or c < 0 or c >= cols or lst[r][c] == '#':
        return 0

    count = 0
    if lst[r][c] == 'D':
        count += 1

    lst[r][c] = '#'

    count += DFS_FloodFill(r + 1, c, rows, cols, lst)
    count += DFS_FloodFill(r - 1, c, rows, cols, lst)
    count += DFS_FloodFill(r, c + 1, rows, cols, lst)
    count += DFS_FloodFill(r, c - 1, rows, cols, lst)

    return count

def countdiamonds(rows, cols, lst):
    maxDiamonds = 0
    for r in range(rows):
        for c in range(cols):
            if lst[r][c] == '.':
                diamond = DFS_FloodFill(r, c, rows, cols, lst)
                maxDiamonds = max(maxDiamonds, diamond)
    return maxDiamonds


input = open("Task-06\input6.txt", "r")
output = open("Task-06\output6.txt", "w")
a=input.readline().strip().split()
R=int(a[0])
H=int(a[1])
lst=[]

for i in range (R):
    a=input.readline().strip()
    lst+=[list(a)]
result = countdiamonds(R, H, lst)

output.write(str(result))

input.close()
output.close()