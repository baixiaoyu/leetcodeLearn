# def toStr(n,base):
#     convertString = "0123456789ABCDEF"
#     if n < base:
#         return convertString[n]
#     else:
#         return toStr(n//base, base) + convertString[n%base]
#
# print(toStr(769,2))


# from turtle import *
#
# myTurtle = Turtle()
# myWin = myTurtle.getscreen()
#
# def drawSpiral(myTurtle, linelen):
#     if linelen > 0:
#         myTurtle.forward(linelen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle, linelen-5)
#
# drawSpiral(myTurtle, 100)
# myWin.exitonclick()

# def hannuota(heigh,start, mid, end):
#     if heigh == 1:
#         print(start ,"===>", end) #是否使用return，取决于上一步中是否需要利用下一步计算产生的结果，有用到就return，没有用到，可以打印一些信息即可或者是，终止
#        # return
#     else:
#         hannuota(heigh-1,start,end,mid)
#         print(start ,"===>", end)
#         hannuota(heigh-1,mid,start,end)
#
# hannuota(3,"a","b","c")
#
#
# def move(n, a, b, c):
#     if n==1:
#         print(a,'==>',c)#只有一块的时候直接从A到C即可
#     else:
#         move(n-1,a,c,b)#把n-1块从a先移到B
#         print(a,'==>',c)#把第n块先从a先到c
#         move(n-1,b,a,c)#再把原来从a移到B上的n-1块，从B移到c,
#
# move(3, 'A', 'B', 'C')


import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def dropBreadcrumb(self,color):
        self.t.dot(10,color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col,row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self,row,col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1 )

    def __getitem__(self,idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('maze2.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)

