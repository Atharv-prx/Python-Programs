from tkinter import *
import random

def next_turn(row, column):
    pass

def check_winner():
    pass

def empty_spaces():
    pass
def new_game():
    pass

def main():
    global window
    global players
    global player
    global buttons
    global label

    window = Tk()

    window.title("Tic Tac Toe")

    players = ["X", "O"]
    player = random.choice(players)

    buttons = [[0,0,0],
               [0,0,0],
               [0,0,0]]

    label = Label(text=player + " turn",
                  font=('consolas', 40))
    label.pack(side="top")

    reset_button = Button(text="Restart",
                          font=('consolas', 20),
                          command=new_game)
    reset_button.pack(side="top")

    frame = Frame(window)
    frame.pack()

    for x in range(3):
        for y in range(3):
            buttons[x][y] = Button(
                frame,
                text="",
                font=('consolas', 40),
                width=5,
                height=2,
                command=lambda row=x, column=y: next_turn(row, column)
            )
            buttons[x][y].grid(row=x, column=y)

    window.mainloop()

if __name__ == "__main__":
    main()