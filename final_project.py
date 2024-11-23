from tkinter import *
import random


def main(dimensions, color):
    grid_bombs=[]
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
    def redox():
        base.destroy()
        main(dimensions, color)
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
        flagBottomLabel = Label(base, width=35, height=1, bg="black")
        flagBottomLabel.place(x=700,y=110)
        flagRightLabel=Label(base,width=2, height=7, bg="black")
        flagRightLabel.place(x=950, y=20)
        menuLabel=Label(base, width=75, height=36, relief="sunken", bg="light gray", borderwidth=5)
        menuLabel.place(x=707,y=140)
        resetButtonFrame=Frame(base,width=200, height=200, bg="light gray")
        resetButtonFrame.place(x=880,y=300)
        resetButton=Button(resetButtonFrame,width=200, height=200, bg="dark gray", command=redox)
        resetButton.place(x=0,y=0)

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
        flagBottomLabel = Label(base, width=50, height=1, bg="black")
        flagBottomLabel.place(x=630,y=110)
        flagRightLabel=Label(base,width=2, height=7, bg="black")
        flagRightLabel.place(x=980, y=20)
        menuLabel=Label(base, width=82, height=36, relief="sunken", bg="light gray", borderwidth=5)
        menuLabel.place(x=650,y=140)
        resetButtonFrame=Frame(base,width=200, height=200, bg="light gray")
        resetButtonFrame.place(x=850 ,y=300)
        resetButton=Button(resetButtonFrame,width=200, height=200, bg="dark gray", command=redox)
        resetButton.place(x=0,y=0)
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
        flagBottomLabel = Label(base, width=439, height=1, bg="black")
        flagBottomLabel.place(x=690,y=110)
        flagRightLabel=Label(base,width=2, height=7, bg="black")
        flagRightLabel.place(x=950, y=20)
        menuLabel=Label(base, width=76, height=36, relief="sunken", bg="light gray", borderwidth=5)
        menuLabel.place(x=700,y=140)
        resetButtonFrame=Frame(base,width=200, height=200, bg="light gray")
        resetButtonFrame.place(x=880 ,y=300)
        resetButton=Button(resetButtonFrame,width=200, height=200, bg="dark gray", command=redox)
        resetButton.place(x=0,y=0)
    flagLabel = Label(base, text=f"🚩 {flagCount}", width=25, height=5)
    flagLabel.place(x=730, y=25)
    base.geometry("1500x1500")

    def switch(event, b):
        if b["state"]==DISABLED:
            return
        if b["bg"]=="DarkOliveGreen2" or b["bg"]=="firebrick2" or b["bg"]=="chartreuse2" or b["bg"]=="MediumOrchid2" or b["bg"]=="medium turquoise":
            b["bg"]="PeachPuff2"
        else:
            b["bg"]="PeachPuff3"
        determine_value(b)
        b["state"] = DISABLED
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
        pass
    
    def determine_value(b):
        color_dict={"0":"black","1":"blue2", "2":"green3", "3":"red2", "4":"DarkOrchid3", "5":"chocolate1", "6":"cyan2", "7":"dark olive green", "8":"wheat3"}
        surrounding_bombs=0
        nonlocal first_click
        r= b.grid_info()["row"]
        c= b.grid_info()["column"]
        if grid_bombs[r][c]==1 and first_click==0:
            def move_bomb():
                grid_bombs[r][c]=0
                while True:
                    row = random.randint(0, dimensions-1)
                    column=random.randint(0, dimensions-1)
                    if grid_bombs[row][column]==0:
                        grid_bombs[row][column]=1
                        return
            move_bomb()
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
        while surrounding_bombs==0:
            b["text"]=""
            
        else:
            surrounding_bombs=str(surrounding_bombs)
            b["text"]=surrounding_bombs
            b["disabledforeground"]=color_dict[surrounding_bombs]
                

    def reveal_bombs():
        for x in frame.winfo_children():
            if grid_bombs[x.grid_info()["row"]][x.grid_info()["column"]]==1:
                x["bg"]="red"
                x["fg"]="black"
                x["text"]="●"
                x["state"]="disabled"
        for x in frame.winfo_children():
            x["state"]=DISABLED


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
        list_of_buttons=[]
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




        