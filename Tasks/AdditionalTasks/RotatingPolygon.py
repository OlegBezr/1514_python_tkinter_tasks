import tkinter
from math import *
CANVAS_SIZE = 800
n = int(input("Input nodes count: "))
r = int(input("Input circle radius: "))

# nodes - ��� ������� ����������� n-���������
nodes = [(CANVAS_SIZE // 2 + r * cos(2 * pi * i / n),
          CANVAS_SIZE // 2 + r * sin(2 * pi * i / n))
          for i in range(n)]

#������ ���� ���� ������� �������������
center = [CANVAS_SIZE // 2, CANVAS_SIZE // 2]

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white', width = CANVAS_SIZE, height = CANVAS_SIZE)

count = len(nodes)
canvas.create_polygon(*nodes, width = 3, outline = 'red', fill = 'white')
    
#���� ��������
alpha = 3
#������� � �������
alpha = alpha / 180 * pi

#�������� ������� ������������ ������ ����� (dote1) 
def RotateSegment(dote1, dote2, angle):
    return [dote1[0] + (dote2[0] - dote1[0]) * cos(angle) + (dote1[1] - dote2[1]) * sin(angle),
            dote1[1] + (dote2[0] - dote1[0]) * sin(angle) + (dote2[1] - dote1[1]) * cos(angle)]    

def Rotate():
    global nodes
    #������� �����
    canvas.delete('all')
    
    #������ �������� ������� �������������� � ���������
    nodes = [RotateSegment(center, nodes[i], alpha) for i in range(n)]    
    
    #����������� ����� ��������������
    canvas.create_polygon(*nodes, width = 3, outline = 'red', fill = 'white')
    
    main.after(100, Rotate)

Rotate()

canvas.pack()
main.mainloop()