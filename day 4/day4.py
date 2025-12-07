file = 'input.txt'
inp = []
with open(file) as f:
    inp = f.read().splitlines()
   
maze = [[0]*len(inp[0]) for _ in range(len(inp))]
UPPER_THRESHOLD, LEFT_THRESHOLD = 0, 0
LOWER_THRESHOLD = len(maze)-1
RIGHT_THRESHOLD = len(maze[0])-1

rolls, rolls2 = 0,0
for idx, row in enumerate(inp):
    for idy, ch in enumerate(''. join(row)):
        maze[idx][idy] = ch
    
for idx, row in enumerate(maze):
    for idy, ch in enumerate(row):
        count = 0
        if ch == '.':
            continue
        if idx> UPPER_THRESHOLD and maze[idx-1][idy] == '@':
            count+=1
        if idx< LOWER_THRESHOLD and maze[idx+1][idy] == '@':
            count+=1
        if idy> LEFT_THRESHOLD and maze[idx][idy-1] == '@':
            count+=1
        if idy< RIGHT_THRESHOLD and maze[idx][idy+1] == '@':
            count+=1
        if idx> UPPER_THRESHOLD and idy> LEFT_THRESHOLD and maze[idx-1][idy-1] == '@':
            count+=1
        if idx> UPPER_THRESHOLD and idy< RIGHT_THRESHOLD and maze[idx-1][idy+1] == '@':
            count+=1
        if idx< LOWER_THRESHOLD and idy> LEFT_THRESHOLD and maze[idx+1][idy-1] == '@':
            count+=1
        if idx< LOWER_THRESHOLD and idy< RIGHT_THRESHOLD and maze[idx+1][idy+1] == '@':
            count+=1
            
        if count<4:
            rolls += 1

for idx, row in enumerate(inp):
    for idy, ch in enumerate(''. join(row)):
        maze[idx][idy] = ch
for _ in range(100):    
    for idx, row in enumerate(maze):
        for idy, ch in enumerate(row):
            count = 0
            if ch == '.':
                continue
            if idx> UPPER_THRESHOLD and maze[idx-1][idy] == '@':
                count+=1
            if idx< LOWER_THRESHOLD and maze[idx+1][idy] == '@':
                count+=1
            if idy> LEFT_THRESHOLD and maze[idx][idy-1] == '@':
                count+=1
            if idy< RIGHT_THRESHOLD and maze[idx][idy+1] == '@':
                count+=1
            if idx> UPPER_THRESHOLD and idy> LEFT_THRESHOLD and maze[idx-1][idy-1] == '@':
                count+=1
            if idx> UPPER_THRESHOLD and idy< RIGHT_THRESHOLD and maze[idx-1][idy+1] == '@':
                count+=1
            if idx< LOWER_THRESHOLD and idy> LEFT_THRESHOLD and maze[idx+1][idy-1] == '@':
                count+=1
            if idx< LOWER_THRESHOLD and idy< RIGHT_THRESHOLD and maze[idx+1][idy+1] == '@':
                count+=1
                
            if count<4:
                rolls2 += 1
                maze[idx][idy] = '.'

print(rolls)
print(rolls2)