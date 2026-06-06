from tkinter import *

# ---------------------------------------------------
# CONSTANTS
# ---------------------------------------------------
GAME_WIDTH = 700
GAME_HEIGHT = 700

# ---------------------------------------------------
# GLOBALS
# ---------------------------------------------------
window = None
mode_var = None

# ---------------------------------------------------
# START/RESTART GAME
# ---------------------------------------------------
def start_game():
    print("Testing")

# ---------------------------------------------------
# UI BUILDING
# ---------------------------------------------------
def build_menu_frame(parent):

    global mode_var

    frame = Frame(parent, 
                  bg= "#0a0a0a")
    
    Label(
        frame,
        text="Rock🪨 Paper📃 Scissors✂️",
        font=("Consolas", 30, "bold"),
        fg= "#00FF00",
        bg= "#0a0a0a"
    ).pack()
    
    Label(
        frame,
        text= "Be sure to tell me if you find any bugs",
        font= ("Consolas", 14),
        fg= "#3a7a3a",
        bg= "#0a0a0a"
    ).pack(pady=(0,30))
    
    # Mode selection
    Label(
        frame,
        text= "Choose mode",
        font=("Consolas", 13, "bold"),
        fg="#888888",
        bg="#0a0a0a",
    ).pack()

    mode_frame = Frame(frame,
                       bg="#0a0a0a")
    mode_frame.pack(pady=(0,30))
    
    for n in ["Single-Player","Multi-Player"]:
        Radiobutton(
            mode_frame,
            text=str(n),
            variable=mode_var,
            value=n,
            font=("Consolas", 14, "bold"),
            fg="#00FF00", 
            bg="#0a0a0a",
            activebackground="#0a0a0a",
            activeforeground="#00FF00",
            selectcolor="#1a1a1a",
            indicatoron=True,
        ).pack(anchor="w",
               pady=3)
    
    # Start Button 
    start_button = Button(
        frame,
        text="▶  START GAME",
        font=("Consolas", 18, "bold"),
        fg="#000000", 
        bg="#00FF00",
        activebackground="#00cc00",
        activeforeground="#000000",
        relief=FLAT,
        padx=24, 
        pady=10,
        cursor="hand2",
        command= start_game
    )
    start_button.pack()
    
    # Sublte Footer
    Label(
        frame, 
        text="Free free to give me ideas about improving this program :)",
        font=("Consolas", 10),
        fg="#333333", 
        bg="#0a0a0a",
    ).pack(side=BOTTOM, pady=14)

    return frame

def main():
    
    global window

    window = Tk()
    window.title("Rock Paper Scissors")
    window.resizable(False, False)
    window.configure(bg="#000000")
    
    menu_frame = build_menu_frame(window)
    menu_frame.pack(padx=20, pady=20)

    window.mainloop()

if __name__=="__main__":
    main()