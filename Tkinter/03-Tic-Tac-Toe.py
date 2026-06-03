from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        buttons[row][column]['text'] = player

        winner = check_winner()

        if winner is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn")

        elif winner is True:
            label.config(text=f"{player} wins!")

        else:
            label.config(text="It's a tie!")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True
    
def new_game():
    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

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