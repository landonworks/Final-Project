from tkinter import *
import final_project

def start():
    
    if buttonEasy["state"]=="normal" and buttonMedium["state"]=="normal" and buttonHard["state"]=="normal":
        return
    dimensions=return_dimensions()
    main.destroy()
    final_project.main(dimensions)

def return_dimensions():
    if buttonEasy["state"]==DISABLED:
        dimensions=9
        return dimensions
    elif buttonEasy["state"]=="normal" and buttonHard["state"]=="normal":
        dimensions=15
        return dimensions
    elif buttonEasy["state"]=="normal" and buttonMedium["state"]=="normal":
        dimensions=25
        return dimensions

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

main.mainloop()
            