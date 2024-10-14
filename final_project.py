from tkinter import *


def main(dimensions):
    r=0
    c=0 
    
    base = Tk()
    base.title("Minesweeper")
    frame = Frame(base, width=1500, height=1500)
    frame.pack()
    base.geometry("1500x1500")


    def switch(b):
        b["bg"]="dark gray"
        b["state"] = DISABLED

    

    def create_grid():
        for x in range(dimensions):
            for j in range(dimensions):
                frame.grid(row=x, column=j)
        for x in range(int(dimensions)):
            for j in range(int(dimensions)):
                 if dimensions==9:
                     button = Button(frame, text="", width=12, height=4, command=lambda: switch(button))
                     button.grid(row=x, column=j)
                 elif dimensions==15:
                     button = Button(frame, text="", width=6, height=2,command=lambda: switch(button))
                     button.grid(row=x, column=j)
                 elif dimensions==25:
                    button = Button(frame, text="", width=3, height=1, command=lambda: switch(button))
                    button.grid(row=x, column=j)
    
    

    create_grid()
    frame.mainloop()




        