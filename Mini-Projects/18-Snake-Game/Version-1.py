from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class snake:
    pass

class food:
    pass

def next_turn(snake, food):
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass   

def game_over():
    pass

def main():
    window = Tk()

    window.title("Snake Game")
    window.resizable(False, False) # Prevents the window from being resized
    
    score = 0
    direction = 'down'

    score_label = Label(window, text="Score: {}".format(score), font=('consolas', 20)) # .format(score) is used to insert the value of score into the string
    score_label.pack()
    
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update() # Updates the window to show the canvas

    window_width = window.winfo_width() # Gets the width of the window
    window_height = window.winfo_height() # Gets the height of the window
    screen_width = window.winfo_screenwidth() # Gets the width of the screen
    screen_height = window.winfo_screenheight() # Gets the height of the screen

    x = int((screen_width / 2) - (window_width / 2)) # Calculates the x coordinate to center the window
    y = int((screen_height / 2) - (window_height / 2)) # Calculates the y coordinate to center the window

    window.geometry(f"{window_width}x{window_height}+{x}+{y}") # Sets the geometry of the window to the calculated values

    snake = Snake()
    food = Food()

    window.mainloop()

if __name__ == "__main__":
    main()