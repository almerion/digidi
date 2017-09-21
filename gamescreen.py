import tkinter as tk
from tkinter import ttk
import turtle  #needs for start screen

#creates game's screen

class GameScreen:
    
    def __init__(self):
        gameWindow = tk.Tk()
        
        gameWindow.title("digidi")
        gameWindow.geometry("500x500")
        start_button = tk.Button(gameWindow, text = "Start", command = self.createStartScreen)

        start_button.pack()
        gameWindow.mainloop()

        
    def createStartScreen(self):
        wn = turtle.Screen()
        wn.bgcolor("black")

        alex = turtle.Turtle()
        alex.pensize(3)
        alex.color("red")


        for i in range(50, 275):
            alex.circle(i)
            i += 15
            

        wn.exitonclick()

