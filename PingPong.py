
from tkinter import *
from tkmacosx import * 
import time
import random

tk=Tk()

counter=0
count=0
tk.title("!Pong!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,height=500,width=600,bd=0,highlightthickness=0,bg="#D0D0D0")
canvas.pack()  
tk.update()

canvas.create_line(300,0,300,500,fill="white")

class Ball:

    def __init__(self,canvas,color,paddle,paddle1):
        self.canvas=canvas
        self.paddle=paddle
        self.paddle1=paddle1
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        for i in range(1,6):
            time.sleep(1)
        self.canvas.move(self.id,282,230)
        start=[-4,4]
        random.shuffle(start)
        self.x=start[0]
        self.y=start[1]
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                return True
            return False
    def hit_paddle1(self,pos):
        paddle_pos=self.canvas.coords(self.paddle1.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[2]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
                return True
            return False

    def score(self,val):
        global counter
        global count
        if val==True:
            a=self.canvas.create_text(225,40,text=counter,font=("Arial",50),fill="#D0D0D0")
            canvas.itemconfig(a,fill="#D0D0D0")
            counter+=1
            time.sleep(0.04)
            print("Player1 : ",counter)
            a=self.canvas.create_text(225,40,text=counter,font=("Arial",50),fill="White")
        elif val==False :
            a=self.canvas.create_text(380,40,text=count,font=("Arial",50),fill="#D0D0D0")
            canvas.itemconfig(a,fill="#D0D0D0")
            count+=1
            time.sleep(0.04)
            print("Player2 : ",count)
            a=self.canvas.create_text(380,40,text=count,font=("Arial",50),fill="White")    
    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)    # Output [x1,y1,x2,y2]
        if pos[1]<=0:
            self.y=4
        if pos[3]>=self.canvas_height:
            self.y=-4
        if pos[0]<=0:
            self.x=4
            self.score(True)
        if pos[2]>=self.canvas_width:
            self.x=-4
            self.score(False)
        if self.hit_paddle(pos)==True:
            self.x=4
        if self.hit_paddle1(pos)==True:
            self.x=-4

class Paddle:
    
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,25,260,fill=color)
        self.canvas.move(self.id,0,40)
        self.y=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.canvas.bind_all("<w>",self.move_up)
        self.canvas.bind_all("<z>",self.move_down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self. canvas.coords(self.id)    # Output [x1,y1,x2,y2]
        if pos[1]<=0:
            self.y=0
        if pos[3]>=self.canvas_height:
            self.y=0

    def move_up(self,evnt):
        self.y=-3
        
    def move_down(self,evnt):
        self.y=3

class Paddle1:
    
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(575,150,600,260,fill=color)
        self.canvas.move(self.id,0,40)
        self.y=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.canvas.bind_all("<KeyPress-Up>",self.move_left)
        self.canvas.bind_all("<KeyPress-Down>",self.move_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self. canvas.coords(self.id)    # Output [x1,y1,x2,y2]
        if pos[1]<=0:
            self.y=0
        if pos[3]>=self.canvas_height:
            self.y=0

    def move_left(self,evnt):
        self.y=-3
        
    def move_right(self,evnt):
        self.y=3


pad=Paddle(canvas,"Blue")
paddle=Paddle1(canvas,"Green")
ball=Ball(canvas,"Red",pad,paddle)

# Infinite loop 
while 1: 
    ball.draw() 
    paddle.draw()
    pad.draw()                           # Forever movement of the ball
    if counter==5:
        ball.x=0
        ball.y=0
        pad.y=0
        paddle.y=0
        canvas.create_text(280,200,text="Congrats! Player2-YOU WIN",font=("Times New Roman",30),fill="Green")
        canvas.create_text(280,240,text="Player1 score is : "+str(count),font=("",30),fill="Green")
    elif count==5:
        ball.x=0
        ball.y=0
        pad.y=0
        paddle.y=0
        canvas.create_text(280,200,text="Congrats! Player1-YOU WIN",font=("Times New Roman",30),fill="Blue")
        canvas.create_text(280,240,text="Player2 score is : "+str(counter),font=("",30),fill="Blue")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if(counter==5 or count==5):
        time.sleep(100000)
        
tk.mainloop()
