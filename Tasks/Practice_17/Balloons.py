import tkinter
import random
import math

cSize = 800
n = 30

balloons = []

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white', width = cSize, height = cSize)

def Draw(index):
    canvas.coords(balloons[index][0], 
                  balloons[index][1][0] - n, balloons[index][1][1] - n, 
                  balloons[index][1][0] + n, balloons[index][1][1] + n)

def MoveAll():
    for i in range(len(balloons)):
        Move(i)
    main.after(5, MoveAll)

def Move(index):
    coords = balloons[index][1]
    move = balloons[index][2]
    
    coords[0] += move[0]
    coords[1] += move[1]
    
    if (coords[0] + n >= cSize or coords[0] - n <= 0):
        move[0] = -move[0]
    if (coords[1] + n >= cSize or coords[1] - n <= 0):
        move[1] = -move[1]
    
    for j in range(len(balloons)):
        if (j != index):
            otherCoords = balloons[j][1]
            if (abs(coords[1] - otherCoords[1]) <= 5 and 
               (abs(coords[0] + 2 * n - otherCoords[0]) <= 2 or 
                abs(coords[0] - 2 * n - otherCoords[0]) <= 2)):
                move[0] = -move[0]
            if (abs(coords[0] - otherCoords[0]) <= 5 and 
               (abs(coords[1] + 2 * n - otherCoords[1]) <= 2 or 
                abs(coords[1] - 2 * n - otherCoords[1]) <= 2)):
                move[1] = -move[1]   
    Draw(index)
    
def AddBalloon(mousePos):
    global balloons
    move_x = random.random()
    move_y = math.sqrt(1 - move_x**2)    
    
    balloons.append([canvas.create_oval(mousePos.x - n, mousePos.x - n, mousePos.x + n, mousePos.y + n, fill = 'red'),
                    [mousePos.x, mousePos.y], [move_x, move_y]])
    
    for i in range(len(balloons)):
        print(balloons[i])
    

canvas.pack()
canvas.bind('<Button>', AddBalloon)
MoveAll()

main.mainloop()
