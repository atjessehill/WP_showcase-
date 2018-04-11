#created by jesse hill for comp 157
from collections import deque
import time
def printm():
    for i in range(len(maze)):
        print(maze[i])

def clean():
    for i in range(len(maze)):
        maze[i] = maze[i].strip()
        maze[i] = list(maze[i])

def determine():
    row = len(maze)
    col = len(maze[0])
    print("ROW "+str(row) + " COL "+ str(col))
    if(x < col/2):
        print("right")
    elif(x>col/2):
        print("left")
    if(y < row/2):
        print("down")
    elif(y>row/2):
        print("up")

def searchs():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 's':
                return (i, j)

def search2(x, y):
    if(maze[x][y] == 'e'):
        return True
    maze[x][y] = '$'
    if (y < len(maze[0]) and maze[x][y+1] != '*' and maze[x][y+1] != '$'):
        dq.append([x, y+1])
    if (y > 0 and maze[x][y-1] != '*' and maze[x][y-1] != '$'):
        dq.append([x, y-1])
    if (x < len(maze) and maze[x+1][y] != '*' and maze[x+1][y] != '$'):
        dq.append([x+1, y])
    if (x > 0 and maze[x-1][y] != '*' and maze[x-1][y] != '$'):
        dq.append([x-1, y])
    return False


#needs to be manually implemented
with open("mazes/maze6.txt") as fileobj:
    maze = fileobj.readlines()

dq = deque()
clean()

x, y  = searchs()

search2(x, y)
moves = 0
Found = False

start = time.time()

while Found == False:
    moves = moves+1
    i, j = dq.popleft()
    Found = search2(i,j)
    if(len(dq)== 0):
        print("There is no solution")
        break;

end = time.time()

print("this took " + str(moves) + " moves")
print("Time: "+ str(end-start))
printm()
