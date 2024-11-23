from tkinter import *
import final_project

def start():

    if buttonCosmic["state"]==DISABLED or buttonFire["state"]==DISABLED or buttonAquatic["state"]==DISABLED or buttonTropical["state"]==DISABLED:
        if buttonEasy["state"]==DISABLED or buttonMedium["state"]==DISABLED or buttonHard["state"]==DISABLED:

            dimensions=return_dimensions()
            color=return_color()
            main.destroy()
            final_project.main(dimensions, color)

def return_dimensions():
    if buttonEasy["state"]==DISABLED:
        dimensions=9
        return dimensions
    if buttonMedium["state"]==DISABLED:
        dimensions=15
        return dimensions
    if buttonHard["state"]==DISABLED:
        dimensions=25
        return dimensions
def return_color():
    if buttonCosmic["state"]==DISABLED and secretButton["state"]!=DISABLED:
        return "MediumOrchid2"
    if buttonTropical["state"]==DISABLED and secretButton["state"]!=DISABLED:
        return "chartreuse2"
    if buttonFire["state"]==DISABLED and secretButton["state"]!=DISABLED:
        return "firebrick2"
    if buttonAquatic["state"]==DISABLED and secretButton["state"]!=DISABLED:
        return "medium turquoise"
    if secretButton["state"]==DISABLED:
        return "DarkOliveGreen2"

def exit():
    main.destroy()

def selected(button):
    if button==buttonEasy:
        button["state"]=DISABLED
        buttonMedium["state"]="normal"
        buttonHard["state"]="normal"
    elif button==buttonMedium:
        button["state"]=DISABLED
        buttonEasy["state"]="normal"
        buttonHard["state"]="normal"
    elif button==buttonHard:
        button["state"]=DISABLED
        buttonEasy["state"]="normal"
        buttonMedium["state"]="normal"
def color_select(b):
    if b==buttonAquatic:
        b["state"]=DISABLED
        buttonFire["state"]="normal"
        buttonTropical["state"]="normal"
        buttonCosmic["state"]="normal"
    elif b==buttonFire:
        b["state"]=DISABLED
        buttonAquatic["state"]="normal"
        buttonTropical["state"]="normal"
        buttonCosmic["state"]="normal"
    elif b==buttonTropical:
        b["state"]=DISABLED
        buttonAquatic["state"]="normal"
        buttonFire["state"]="normal"
        buttonCosmic["state"]="normal"
    elif b==buttonCosmic:
        b["state"]=DISABLED
        buttonAquatic["state"]="normal"
        buttonFire["state"]="normal"
        buttonTropical["state"]="normal"
def decoration(b):
    b["state"]=DISABLED
    b["bg"]="dark gray"
    if b==decorationL or b==decorationLR or b==decorationR or b==decorationRL:
        b["text"]="1"
    elif b==decorationLB or b==decorationRB:
        b["text"]="●"
def secret():
    secretButton["bg"]="dark grey"
    secretButton["state"]=DISABLED

main=Tk()
main.geometry("1500x1500")
main.config(bg="light gray")

title=Label(main, text="MINESWEEPER", font=("Arial", 50,"bold"),fg="maroon", bg="light gray")
title.pack()
buttonStart = Button(main, text="START", font=("Arial", 30, "bold"), bg="light gray", fg="maroon", command=start)
buttonEnd = Button(main, text="EXIT", font=("Arial", 30, "bold"), bg="light gray", fg="maroon", command=exit)
buttonStart.place(x=555, y=400)
buttonEnd.place(x=580, y=600)
buttonEasy=Button(main, text="EASY", font=("Arial", 30, "bold"), bg="light gray", fg="maroon", command=lambda:selected(buttonEasy))
buttonEasy.place(x=380, y=500)
buttonMedium=Button(main, text="MEDIUM", font=("Arial", 30, "bold"), bg="light gray", fg="maroon", command=lambda:selected(buttonMedium))
buttonMedium.place(x=538, y=500)
buttonHard=Button(main, text="HARD", font=("Arial", 30, "bold"), bg="light gray", fg="maroon", command=lambda:selected(buttonHard))
buttonHard.place(x=750, y=500)

buttonAquatic = Button(main, text="●", font=("Arial", 30, "bold"),bg="light gray", fg="medium turquoise", width=3, height=1, command= lambda:color_select(buttonAquatic))
buttonAquatic.place(x=380, y=200)
buttonFire = Button(main, text="●", font=("Arial", 30, "bold"), bg="light gray", fg="firebrick2", width=3, height=1, command=lambda:color_select(buttonFire))
buttonFire.place(x=820, y=200)
buttonTropical = Button(main, text="●", font=("Arial", 30, "bold"), bg="light gray", fg="chartreuse2", width=3, height=1, command=lambda:color_select(buttonTropical))
buttonTropical.place(x=520, y=200)
buttonCosmic = Button(main, text="●", font=("Arial", 30, "bold"), bg="light gray", fg="MediumOrchid2", width=3, height=1, command=lambda:color_select(buttonCosmic))
buttonCosmic.place(x=670, y=200)

decorationL = Button(main, bg="light gray", width=7, height=3, command=lambda:decoration(decorationL))
decorationL.place(x=3, y=2)
decorationLR=Button(main, bg="light gray", width=7, height=3, command=lambda:decoration(decorationLR))
decorationLR.place(x=3, y=60)
decorationLB=Button(main,bg="light gray", disabledforeground="red", width=7, height=3, command=lambda:decoration(decorationLB))
decorationLB.place(x=65, y=2)

decorationR=Button(main, bg="light gray", width=7, height=3, command=lambda:decoration(decorationR))
decorationR.place(x=1210, y=665)
decorationRL=Button(main, bg="light gray", width=7, height=3, command=lambda:decoration(decorationRL))
decorationRL.place(x=1210, y=607)
decorationRB=Button(main, bg="light gray", disabledforeground="red", width=7, height=3, command=lambda:decoration(decorationRB))
decorationRB.place(x=1148, y=665)

secretButton = Button(main, text="🚩", bg="light gray", width=7, height=3, command=secret)
secretButton.place(x=1210, y=0)






main.mainloop()
            