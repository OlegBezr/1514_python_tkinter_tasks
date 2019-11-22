import tkinter
import random

main = tkinter.Tk()
main.title('smth')
sSize = 800
canvas = tkinter.Canvas(main, bg = "white", height = sSize, width = sSize)
canvas.pack()

R = 20
speed = 5
circle = canvas.create_oval((sSize / 2 - R, sSize / 2 - R), (sSize / 2 + R, sSize / 2 + R), fill = 'red')

coords = [sSize / 2, sSize / 2]

label = tkinter.Label(main, text = "x: y:")
label.pack()

def Action(event):
    typ = event.keycode
    #print(typ)
    color(typ)
    move(typ)
    
def color(typ):
    if (typ == 49):
        canvas.itemconfig(circle, fill = 'red')
    elif (typ == 50):
        canvas.itemconfig(circle, fill = 'blue')
    elif (typ == 51):
        canvas.itemconfig(circle, fill = 'green') 
    elif (typ == 67):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        tk_rgb = "#%02x%02x%02x" % (r, g, b)
        canvas.itemconfig(circle, fill = tk_rgb)

def move(typ):
    if (typ == 38 or typ == 87):
        coords[1] -= speed
    elif (typ == 40 or typ == 83):
        coords[1] += speed
    elif (typ == 37 or typ == 65):
        coords[0] -= speed
    elif (typ == 39 or typ == 68):
        coords[0] += speed
    elif (typ == 80):
        coords[0] = random.randint(0, sSize)
        coords[1] = random.randint(0, sSize)
        
    coords[0] %= sSize
    coords[1] %= sSize
    label.config(text = 'x:' + str(coords[0])  + ' y:' + str(coords[1]))
    canvas.coords(circle, coords[0] - R, coords[1] - R, coords[0] + R, coords[1] + R)    
        

main.bind("<KeyPress>", Action)

main.mainloop()



    