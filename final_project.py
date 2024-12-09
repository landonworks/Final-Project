from tkinter import *
import random



def main(dimensions, color):
    loser_count=0
    winner_count=0
    seconds=0
    stopper=False
    grid_bombs=[]
    list_of_buttons=[]
    first_click=0
    flagCount=0
    if dimensions==9:
        flagCount=15
        grid_bombs=[
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ]
    elif dimensions==15:
        flagCount=40
        grid_bombs=[
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
    elif dimensions==25:
        flagCount=100
        grid_bombs=[
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
    base = Tk()
    base.title("Minesweeper")
    frame = Frame(base, width=750, height=750)
    frame.grid(row=0, column=0)

    def timer():
        nonlocal seconds
        nonlocal stopper
        if stopper==False:
            seconds+=1
            timerLabel["text"]=seconds
            timerLabel.after(1000, timer)
        else:
            return
        
    def redox():
        base.destroy()
        main(dimensions, color)

    def clear():
        base.destroy()
    
    def directions():
        count=0
        for x in base.winfo_children():
            count+=1
        if count==14:
            direction_signal = Toplevel(width=500, height=120)
            direction_signal.title("Directions")
            directionLabel=Label(direction_signal, text="""
        1. Click anywhere on the grid to start
        2. Each tile with a number tells how many bombs surround it (diagonals included)
        3. If you think you know where a bomb is, right-click to place a flag
        4. If you hit a bomb, you lose the game!
        5. To win, clear all non-bomb tiles
        6. To restart, click the face!""")
            directionLabel.place(x=0,y=0)

    if dimensions==9:
        bottomBarLabel = Label(base, width=98, height=1, bg="black")
        bottomBarLabel.place(x=0, y=600)
        sideBarLabel = Label(base,width=2, height=41, bg="black")
        sideBarLabel.place(x=683, y=0)
        borderBarTop = Label(base, width=98, height=1, bg="black")
        borderBarTop.place(x=700, y=0)
        borderBarSideR=Label(base,width=10,height=48, bg="black")
        borderBarSideR.place(x=1250, y=0)
        borderBarBottom=Label(base, width=200, height=2, bg="black")
        borderBarBottom.place(x=0,y=700)
        borderBarSideL=Label(base, width=2, height=10, bg="black")
        borderBarSideL.place(x=0,y=600)
        menuLabel=Label(base, width=75, height=36, relief="sunken", bg="light gray", borderwidth=5)
        menuLabel.place(x=707,y=140)
        resetButton=Button(base,text="😃",font=("Times New Roman", 30), bg="light gray",fg="black", command=redox)
        resetButton.place(x=936,y=36)
        flagLabel = Label(base, text=f"🚩 {flagCount}", width=25, height=5, relief="sunken", bd=5, bg="light gray")
        flagLabel.place(x=707, y=33)
        timerLabel = Label(base, text=f"...", width=25, height=5, relief="sunken", bd=5, bg="light gray")
        timerLabel.place(x=1055, y=33)
        remarkLabel=Label(base,text="", width=92, height=3, relief="sunken", bd=5, bg="light gray")
        remarkLabel.place(x=35, y=632)
        exitButton=Button(base, text="              E x i t              ", font=("Calibri", 40, "bold"),command=clear)
        exitButton.place(x=730,y=500)
        direcButton=Button(base,text="     D i r e c t i o n s     ", font=("Calibri", 40,"bold"), command=directions)
        direcButton.place(x=730, y=300)
    elif dimensions==15:
        bottomBarLabel = Label(base, width=90, height=1, bg="black")
        bottomBarLabel.place(x=-2, y=552)
        sideBarLabel = Label(base,width=2, height=38, bg="black")
        sideBarLabel.place(x=615, y=-5)
        borderBarTop = Label(base, width=105, height=1, bg="black")
        borderBarTop.place(x=620, y=0)
        borderBarSideR=Label(base,width=10,height=48, bg="black")
        borderBarSideR.place(x=1250, y=0)
        borderBarBottom=Label(base, width=200, height=2, bg="black")
        borderBarBottom.place(x=0,y=700)
        borderBarSideL=Label(base, width=2, height=12, bg="black")
        borderBarSideL.place(x=0,y=555)
        menuLabel=Label(base, width=82, height=36, relief="sunken", bg="light gray", borderwidth=5)
        menuLabel.place(x=650,y=140)
        resetButton=Button(base,text="😃",font=("Times New Roman", 30), bg="light gray",fg="black", command=redox)
        resetButton.place(x=902,y=36)
        flagLabel = Label(base, text=f"🚩 {flagCount}", width=33, height=5, relief="sunken", bd=5, bg="light gray")
        flagLabel.place(x=650, y=33)
        timerLabel = Label(base, text=f"...", width=33, height=5, relief="sunken", bd=5, bg="light gray")
        timerLabel.place(x=993, y=33)
        remarkLabel=Label(base,text="", width=83, height=5, relief="sunken", bd=5, bg="light gray")
        remarkLabel.place(x=30, y=590)
        exitButton=Button(base, text="              E x i t              ", font=("Calibri", 40, "bold"),command=clear)
        exitButton.place(x=730,y=500)
        direcButton=Button(base,text="     D i r e c t i o n s     ", font=("Calibri", 40,"bold"), command=directions)
        direcButton.place(x=730, y=300)
    elif dimensions==25:
        bottomBarLabel = Label(base, width=98, height=1, bg="black")
        bottomBarLabel.place(x=-2, y=551)
        sideBarLabel = Label(base,width=2, height=39, bg="black")
        sideBarLabel.place(x=675, y=-19)
        borderBarTop = Label(base, width=105, height=1, bg="black")
        borderBarTop.place(x=690, y=0)
        borderBarSideR=Label(base,width=10,height=48, bg="black")
        borderBarSideR.place(x=1250, y=0)
        borderBarBottom=Label(base, width=200, height=2, bg="black")
        borderBarBottom.place(x=0,y=700)
        borderBarSideL=Label(base, width=2, height=12, bg="black")
        borderBarSideL.place(x=0,y=555)
        menuLabel=Label(base, width=76, height=36, relief="sunken", bg="light gray", borderwidth=5)
        menuLabel.place(x=700,y=140)
        resetButton=Button(base,text="😃",font=("Times New Roman", 30), bg="light gray",fg="black", command=redox)
        resetButton.place(x=930,y=35)
        flagLabel = Label(base, text=f"🚩 {flagCount}", width=25, height=5, relief="sunken", bd=5, bg="light gray")
        flagLabel.place(x=700, y=33)
        timerLabel = Label(base, text=f"...", width=25, height=5, relief="sunken", bd=5, bg="light gray")
        timerLabel.place(x=1055, y=33)
        remarkLabel=Label(base,text="", width=92, height=3, relief="sunken", bd=5, bg="light gray")
        remarkLabel.place(x=35, y=610)
        exitButton=Button(base, text="              E x i t              ", font=("Calibri", 40, "bold"),command=clear)
        exitButton.place(x=730,y=500)
        direcButton=Button(base,text="     D i r e c t i o n s     ", font=("Calibri", 40,"bold"), command=directions)
        direcButton.place(x=730, y=300)
    base.geometry("1500x1500")

    def switch(event, b):
        nonlocal flagCount
        if b["state"]==DISABLED:
            return
        if b["bg"]=="DarkOliveGreen2" or b["bg"]=="firebrick2" or b["bg"]=="chartreuse2" or b["bg"]=="MediumOrchid2" or b["bg"]=="medium turquoise":
            b["bg"]="PeachPuff2"
        else:
            b["bg"]="PeachPuff3"
        if b["text"]=="🚩":
            flagCount+=1
            flagLabel["text"]=f"🚩 {flagCount}"

        determine_value(b)
        counter=0
        for x in frame.winfo_children():
            if x["state"]==DISABLED:
                counter+=1
        if dimensions==9 and counter==66:
            for x in frame.winfo_children():
                x["state"]=DISABLED
                winner()
        elif dimensions ==15 and counter==185:
            for x in frame.winfo_children():
                x["state"]=DISABLED
                winner()
        elif dimensions==25 and counter==525:
            for x in frame.winfo_children():
                x["state"]=DISABLED
                winner()
    
    def flag(event, b):
        nonlocal flagCount
        if b["state"]==DISABLED:
            return
        if b["text"]=="🚩":
            b["text"]=""
            flagCount+=1
            flagLabel["text"]=f"🚩 {flagCount}"
        elif b["text"]=="" and flagCount>0:
            b["text"]="🚩"
            flagCount-=1
            flagLabel["text"]=f"🚩 {flagCount}"
    
    def winner():
        nonlocal stopper
        timerLabel["bg"]="green"
        resetButton["text"]="😎"
        stopper=True
        winner_remark()
    
    def reveal_bombs():
        nonlocal stopper
        stopper=True
        timerLabel["bg"]="red"
        resetButton["text"]="😵"
        loser_remark()
        for x in frame.winfo_children():
            if grid_bombs[x.grid_info()["row"]][x.grid_info()["column"]]==1:
                x["bg"]="red"
                x["fg"]="black"
                x["text"]="●"
                x["state"]="disabled"
        for x in frame.winfo_children():
            x["state"]=DISABLED

    def loser_remark():
        remarkLabel["fg"]="red"
        remarkLabel["text"]="Y           o        u                L        o        s        e        !"
            
    def winner_remark():
        nonlocal winner_count
        remarkLabel["fg"]="green"
        remarkLabel["text"]="Y        o        u                w        i        n        !"

    
    def determine_value(b):
        color_dict={"0":"black","1":"blue2", "2":"green3", "3":"red2", "4":"DarkOrchid3", "5":"chocolate1", "6":"cyan2", "7":"dark olive green", "8":"wheat3"}
        surrounding_bombs=0
        nonlocal first_click
        r= b.grid_info()["row"]
        c= b.grid_info()["column"]
        if first_click==0:
            timer()
            bomb_count=0
            if grid_bombs[r][c]==1:
                bomb_count+=1
            grid_bombs[r][c]=0
            
            try:
                if grid_bombs[r+1][c]==1:
                    grid_bombs[r+1][c]=0
                    bomb_count+=1
            except:
                pass
            try:
                if grid_bombs[r-1][c]==1:
                    grid_bombs[r-1][c]=0
                    bomb_count+=1
            except:
                pass
            try:
                if grid_bombs[r][c+1]==1:
                    grid_bombs[r][c+1]=0
                    bomb_count+=1
            except:
                pass
            try:
                if grid_bombs[r][c-1]==1:
                    grid_bombs[r][c-1]=0
                    bomb_count+=1
            except:
                pass
            try:
                if grid_bombs[r+1][c+1]==1:
                    grid_bombs[r+1][c+1]=0
                    bomb_count+=1
            except:
                pass
            try:
                if grid_bombs[r-1][c-1]==1:
                    grid_bombs[r-1][c-1]=0
                    bomb_count+=1
            except:
                pass
            try:
                if grid_bombs[r+1][c-1]==1:
                    grid_bombs[r+1][c-1]=0
                    bomb_count+=1
            except:
                pass
            try:
                if grid_bombs[r-1][c+1]==1:
                    grid_bombs[r-1][c+1]=0
                    bomb_count+=1
            except:
                pass
            if bomb_count>0:
                k=0
                while k<bomb_count:
                    row=random.randint(0,dimensions-1)
                    column=random.randint(0,dimensions-1)
                    if grid_bombs[row][column]==1 or row==r+1 or row==r-1 or row==r or column==c+1 or column==c-1 or column==c:
                        bomb_count+=1
                        k+=1
                        continue
                    grid_bombs[row][column]=1
                    k=k+1
        first_click+=1
            
        if grid_bombs[r][c]==1:
            reveal_bombs()
            return
        try:
            if grid_bombs[r+1][c]==1 and r+1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r-1][c]==1 and r-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r][c+1]==1:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r][c-1]==1 and c-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r-1][c-1]==1 and r-1>=0 and c-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r-1][c+1]==1 and r-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r+1][c-1]==1 and c-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r+1][c+1]==1:
                surrounding_bombs+=1
        except IndexError:
            pass
        if surrounding_bombs==0:
            zero_eval(list_of_buttons.index(b))
            
        else:
            surrounding_bombs=str(surrounding_bombs)
            b["text"]=surrounding_bombs
            b["disabledforeground"]=color_dict[surrounding_bombs]
            b["state"]=DISABLED

    def zero_eval(num):
        list_of_buttons[num]["state"]=DISABLED
        r=list_of_buttons[num].grid_info()["row"]
        c=list_of_buttons[num].grid_info()["column"]
        try:
            zero_switch(list_of_buttons[num+dimensions])
        except:
            pass
        try:
            if r>0:
                zero_switch(list_of_buttons[num-dimensions])
        except:
            pass
        try:
            if c<(dimensions-1):
                zero_switch(list_of_buttons[num+1])
        except:
            pass
        try:
            if c>0:
                zero_switch(list_of_buttons[num-1])
        except:
            pass
        try:
            if c<(dimensions-1):
                zero_switch(list_of_buttons[num+(dimensions+1)])
        except:
            pass
        try:
            if c>0:
                zero_switch(list_of_buttons[num+(dimensions-1)])
        except:
            pass
        try:
            if r>0 and c>0:
                zero_switch(list_of_buttons[num-(dimensions+1)])
        except:
            pass
        try:
            if r>0 and c<(dimensions-1):
                zero_switch(list_of_buttons[num-(dimensions-1)])
        except:
            pass

    def zero_switch(b):
        if b["state"]==DISABLED:
            return
        if b["bg"]=="DarkOliveGreen2" or b["bg"]=="firebrick2" or b["bg"]=="chartreuse2" or b["bg"]=="MediumOrchid2" or b["bg"]=="medium turquoise":
            b["bg"]="PeachPuff2"
        else:
            b["bg"]="PeachPuff3"
        zero_determine_value(b)
        counter=0
        for x in frame.winfo_children():
            if x["state"]==DISABLED:
                counter+=1
        if dimensions==9 and counter==66:
            for x in frame.winfo_children():
                x["state"]=DISABLED
                winner()
        elif dimensions ==15 and counter==185:
            for x in frame.winfo_children():
                x["state"]=DISABLED
                winner()
        elif dimensions==25 and counter==525:
            for x in frame.winfo_children():
                x["state"]=DISABLED
                winner()

    def zero_determine_value(b):
        color_dict={"0":"black","1":"blue2", "2":"green3", "3":"red2", "4":"DarkOrchid3", "5":"chocolate1", "6":"cyan2", "7":"dark olive green", "8":"wheat3"}
        surrounding_bombs=0
        is_bomb=0
        r= b.grid_info()["row"]
        c= b.grid_info()["column"]
        if grid_bombs[r][c]==1:
            is_bomb+=1
        try:
            if grid_bombs[r+1][c]==1 and r+1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r-1][c]==1 and r-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r][c+1]==1:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r][c-1]==1 and c-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r-1][c-1]==1 and r-1>=0 and c-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r-1][c+1]==1 and r-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r+1][c-1]==1 and c-1>=0:
                surrounding_bombs+=1
        except IndexError:
            pass
        try:
            if grid_bombs[r+1][c+1]==1:
                surrounding_bombs+=1
        except IndexError:
            pass
        if surrounding_bombs==0 and is_bomb==0:
            zero_eval(list_of_buttons.index(b))
            
        elif surrounding_bombs!=0 and is_bomb==0:
            surrounding_bombs=str(surrounding_bombs)
            b["text"]=surrounding_bombs
            b["disabledforeground"]=color_dict[surrounding_bombs]
            b["state"]=DISABLED
        elif is_bomb==1:
            return   

    def create_bombs(dimensions):
        
        if dimensions==9:
            bombs=15
        elif dimensions==15:
            bombs=40
        elif dimensions==25:
            bombs=100
        i=0
        while i<bombs:
            random_row=random.randint(0,dimensions-1)
            random_column=random.randint(0,dimensions-1)

            if grid_bombs[random_row][random_column]==1:
                bombs=bombs+1
                i=i+1
                continue
            grid_bombs[random_row][random_column]=1
            i=i+1


    def create_grid(color):
        nonlocal list_of_buttons
        what_button=0
        for x in range(dimensions):
            for j in range(dimensions):
                frame.grid(row=x, column=j)
        for x in range(int(dimensions)):
            for j in range(int(dimensions)):
                 if dimensions==9:
                     button = Button(frame, text="", width=10, height=4, relief="sunken", bd=0)
                     button.grid(row=x, column=j)
                     button.bind("<Button-1>", lambda event, what_button=what_button: switch(event, list_of_buttons[what_button]))
                     button.bind("<Button-3>", lambda event, what_button=what_button: flag(event, list_of_buttons[what_button]))
                     list_of_buttons.append(button)
                     what_button+=1

                 elif dimensions==15:
                     button = Button(frame, text="", width=5, height=2, relief="sunken", bd=0)
                     button.grid(row=x, column=j)
                     button.bind("<Button-1>", lambda event, what_button=what_button: switch(event, list_of_buttons[what_button]))
                     button.bind("<Button-3>", lambda event, what_button=what_button: flag(event, list_of_buttons[what_button]))
                     list_of_buttons.append(button)
                     what_button+=1

                 elif dimensions==25:
                     button = Button(frame, text="", width=3, height=1, relief="sunken", bd=0)
                     button.grid(row=x, column=j)
                     button.bind("<Button-1>", lambda event, what_button=what_button: switch(event, list_of_buttons[what_button]))
                     button.bind("<Button-3>", lambda event, what_button=what_button: flag(event, list_of_buttons[what_button]))
                     list_of_buttons.append(button)
                     what_button+=1
        for button in list_of_buttons:
            button["bg"]=color
            if color=="DarkOliveGreen2" or color=="DarkOliveGreen3":
                if color=="DarkOliveGreen2":
                    color="DarkOliveGreen3"
                else:
                    color="DarkOliveGreen2"
            elif color=="medium turquoise" or color=="turquoise":
                if color=="medium turquoise":
                    color="turquoise"
                else:
                    color="medium turquoise"
            elif color=="firebrick2" or color=="firebrick3":
                if color=="firebrick2":
                    color="firebrick3"
                else:
                    color="firebrick2"
            elif color=="chartreuse2" or color=="CadetBlue1":
                if color=="chartreuse2":
                    color="CadetBlue1"
                else:
                    color="chartreuse2"
            elif color=="MediumOrchid2" or color=="MediumOrchid3":
                if color=="MediumOrchid2":
                    color="MediumOrchid3"
                else:
                    color="MediumOrchid2"
            
    
    

    create_grid(color)
    create_bombs(dimensions)
    frame.mainloop()




        