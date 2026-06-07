from tkinter import *

# ---------------------------------------------------
# CONSTANTS
# ---------------------------------------------------
GAME_WIDTH = 700
GAME_HEIGHT = 700
BACKGROUND_COLOR = "#000000"

# ---------------------------------------------------
# GLOBALS
# ---------------------------------------------------
window              = None
mode_var            = None
score_label         = None
restart_button      = None
player_1_score      = 0
player_2_score      = 0
computer_score      = 0
player_1_choice     = None
player_2_choice     = None
computer_choice     = None

# ---------------------------------------------------
# Frame switching 
# ---------------------------------------------------
def show_frame(frame):
    frame.tkraise()

# ---------------------------------------------------
# GAME LOGIC
# ---------------------------------------------------
# nothing yet 😭

# ---------------------------------------------------
# START/RESTART GAME
# ---------------------------------------------------
def start_game():
    show_frame(game_frame)
    _launch_game()

def restart_game():
    _launch_game()

def _launch_game():
    global score

    score = 0

    score_label.config(text=f"Score: {score}")

    canvas.delete("all")

    restart_button.place_forget()

def go_to_menu():
    show_frame(menu_frame)

# ---------------------------------------------------
# UI BUILDING
# ---------------------------------------------------
def build_menu_frame(parent):

    global mode_var

    frame = Frame(parent, 
                  bg= "#0a0a0a",
                  )
    
    Label(
        frame,
        text="==> Rock Paper Scissors <==",
        font=("Consolas", 30, "bold"),
        fg= "#00FF00",
        bg= "#0a0a0a"
    ).pack(pady=(60,4))
    
    Label(
        frame,
        text= "Be sure to read keybinds",
        font= ("Consolas", 14),
        fg= "#3a7a3a",
        bg= "#0a0a0a"
    ).pack(pady=(0,40))
    
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
    
    # keybind description
    Label(
        frame,
        text=(
            "\n---> Keybinds <---\n\n"
            "1. Single Player\n\n"
            "   A = Rock, S = Paper, D = Scissors\n\n"
            "2. Multi Player\n\n"
            "   A/S/D = Player 1\n"
            "   J/K/L = Player 2"
        ),
        font=("Consolas", 15),
        fg="#00FF00",
        bg="#0a0a0a",
    ).pack()

    # Sublte Footer
    Label(
        frame, 
        text="Free free to give me ideas about improving this program :)",
        font=("Consolas", 10),
        fg="#333333", 
        bg="#0a0a0a",
    ).pack(side=BOTTOM, pady=14)

    return frame

def build_game_frame(parent):
    
    # Score label + canvas + hidden restart button + menu button 
    global canvas, score_label, restart_button 

    frame = Frame(parent,
                  bg= "#000000")
    
    # This bar would contain menu button and score label
    top_bar = Frame(frame, 
                    bg="#111111")
    top_bar.pack(fill=X)
    
    # Menu button at top left
    menu_button = Button(
        top_bar,
        text="MENU",
        font=("Consolas", 12),
        fg="#00FF00", 
        bg="#111111",
        activebackground="#222222",
        activeforeground="#00FF00",
        relief=FLAT, 
        padx=10, 
        pady=4,
        cursor="hand2",
        command=go_to_menu
    )
    menu_button.pack(side=LEFT,
                     padx=6,
                     pady=4)
    
    # Score label at top right
    score_label = Label(
        top_bar,
        text="Score: 0",
        font=("Consolas", 18, "bold"),
        fg="#00FF00", 
        bg="#111111"
    )    
    score_label.pack(side=RIGHT, 
                     padx=16, 
                     pady=4)
    
    # Canvas
    canvas = Canvas(
        frame,
        bg=BACKGROUND_COLOR,
        height=GAME_HEIGHT,
        width=GAME_WIDTH,
        highlightthickness=0
    )
    canvas.pack()

    # Hidden restart button 
    restart_button = Button(
        canvas,
        text="Restart",
        font=("Consolas", 18, "bold"),
        fg="#000000", 
        bg="#00FF00",
        activebackground="#00cc00",
        relief=FLAT,
        padx=20, pady=8,
        cursor="hand2",
        command=restart_game
    )

    return frame

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------
def main():
    
    global window, menu_frame, game_frame, mode_var

    window = Tk()
    window.title("Rock Paper Scissors")
    window.resizable(False, False)
    window.configure(bg="#000000")

    container = Frame(window, bg="#000000")
    container.pack(fill=BOTH, expand=True) 
    # fill=BOTH  --> "Stretch horizontally and vertically to fill any available space."
    # expand = True --> "If the window gets larger, give the extra space to this widget."

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    # grid_****configure basically means that "This row/column is allowed to expand."

    menu_frame = build_menu_frame(container)
    game_frame = build_game_frame(container)

    for frame in (menu_frame, game_frame):
        frame.grid(row=0, column=0, sticky= 'nsew')
    
    show_frame(menu_frame)

    # Key bindings in future here

    # Center window
    window.update()
    w, h = window.winfo_width(), window.winfo_height()
    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
    # width x height + x_position + y_position
    
    window.mainloop()

if __name__=="__main__":
    main()