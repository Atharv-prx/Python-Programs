from tkinter import *

# ---------------------------------------------------
# CONSTANTS
# ---------------------------------------------------
GAME_WIDTH = 700
GAME_HEIGHT = 700
BACKGROUND_COLOR = "#000000"

CHOICES = ["Rock", "Paper", "Scissors"]
KEY_MAP = {
    "a": "Rock", "s": "Paper", "d": "Scissors",   # P1
    "j": "Rock", "k": "Paper", "l": "Scissors",   # P2
}
WINS_AGAINST = {
    "Rock":     "Scissors",
    "Paper":    "Rock",
    "Scissors": "Paper",
}

# ---------------------------------------------------
# GLOBALS
# ---------------------------------------------------
window              = None
canvas              = None
mode_var            = None
score_label         = None
restart_button      = None

player_1_score      = 0
player_2_score      = 0
computer_score      = 0

# Waiting for both players' input in multiplayer
p1_choice_pending    = None # will hold p1 choice until p2 also presses 

game_state = "waiting"

# ---------------------------------------------------
# Helpers 
# ---------------------------------------------------
def show_frame(frame):
    frame.tkraise()

def get_mode():
    return mode_var.get()

# ---------------------------------------------------
# Canvas Drawing
# ---------------------------------------------------
def draw_waiting():
    canvas.delete("all")
    mode = get_mode()

    # Dashed border
    _draw_border()

    canvas.create_text(
        GAME_WIDTH // 2, 120,
        text="ROCK  PAPER  SCISSORS",
        font=("Consolas", 22, "bold"),
        fill="#00FF00"
    )

    if mode == "Single-Player":
        canvas.create_text(
            GAME_WIDTH // 2, 240,
            text="Waiting for choice...",
            font=("Consolas", 16),
            fill="#888888"
        )
        canvas.create_text(
            GAME_WIDTH // 2, GAME_HEIGHT - 60,
            text="A = Rock     S = Paper     D = Scissors",
            font=("Consolas", 13),
            fill="#3a7a3a"
        )
    else:
        canvas.create_text(
            GAME_WIDTH // 2, 200,
            text="Player 1: waiting...",
            font=("Consolas", 16),
            fill="#888888",
            tags="p1_status"
        )
        canvas.create_text(
            GAME_WIDTH // 2, 260,
            text="Player 2: waiting...",
            font=("Consolas", 16),
            fill="#888888",
            tags="p2_status"
        )
        canvas.create_text(
            GAME_WIDTH // 2, GAME_HEIGHT - 80,
            text="Player 1:  A / S / D",
            font=("Consolas", 13),
            fill="#3a7a3a"
        )
        canvas.create_text(
            GAME_WIDTH // 2, GAME_HEIGHT - 50,
            text="Player 2:  J / K / L",
            font=("Consolas", 13),
            fill="#3a7a3a"
        )

def draw_result_single(player_choice, comp_choice, outcome):
    canvas.delete("all")
    _draw_border()

    # Title
    canvas.create_text(
        GAME_WIDTH // 2, 100,
        text="ROCK  PAPER  SCISSORS",
        font=("Consolas", 22, "bold"),
        fill="#00FF00"
    )

    # Choices
    canvas.create_text(
        GAME_WIDTH // 2, 230,
        text=f"You chose:   {player_choice.upper()}",
        font=("Consolas", 18),
        fill="#ffffff"
    )
    canvas.create_text(
        GAME_WIDTH // 2, 290,
        text=f"Computer:    {comp_choice.upper()}",
        font=("Consolas", 18),
        fill="#aaaaaa"
    )

    # Outcome
    color, label = _outcome_style(outcome)
    canvas.create_text(
        GAME_WIDTH // 2, 400,
        text=label,
        font=("Consolas", 32, "bold"),
        fill=color
    )

    # Next round hint
    canvas.create_text(
        GAME_WIDTH // 2, GAME_HEIGHT - 60,
        text="Press Enter for next round  (or A/S/D to pick immediately)",
        font=("Consolas", 13),
        fill="#3a7a3a"
    )

def draw_result_multi(p1_choice, p2_choice, outcome):

    canvas.delete("all")
    _draw_border()

    canvas.create_text(
        GAME_WIDTH // 2, 100,
        text="ROCK  PAPER  SCISSORS",
        font=("Consolas", 22, "bold"),
        fill="#00FF00"
    )

    canvas.create_text(
        GAME_WIDTH // 2, 230,
        text=f"Player 1:   {p1_choice.upper()}",
        font=("Consolas", 18),
        fill="#00ccff"
    )
    canvas.create_text(
        GAME_WIDTH // 2, 290,
        text=f"Player 2:   {p2_choice.upper()}",
        font=("Consolas", 18),
        fill="#ff9900"
    )

    if outcome == "p1":
        label = "PLAYER 1 WINS!"
        color = "#00ccff"
    elif outcome == "p2":
        label = "PLAYER 2 WINS!"
        color = "#ff9900"
    else:
        label = "DRAW!"
        color = "#ffff00"

    canvas.create_text(
        GAME_WIDTH // 2, 400,
        text=label,
        font=("Consolas", 32, "bold"),
        fill=color
    )

    canvas.create_text(
        GAME_WIDTH // 2, GAME_HEIGHT - 60,
        text="Press Enter for next round  (or any key to pick immediately)",
        font=("Consolas", 13),
        fill="#3a7a3a"
    )

def _draw_border():
    pad = 20
    canvas.create_rectangle(
        pad, pad, GAME_WIDTH - pad, GAME_HEIGHT - pad,
        outline="#00FF00", width=1, dash=(6, 4)
    )

def _outcome_style(outcome):
    if outcome == "win":
        return "#00FF00", "YOU WIN!"
    elif outcome == "lose":
        return "#FF4444", "YOU LOSE!"
    else:
        return "#ffff00", "DRAW!"

# ---------------------------------------------------
# Game Logic
# ---------------------------------------------------
def resolve_single(player_choice):
    pass

def resolve_multi(p1, p2):
    pass

# ---------------------------------------------------
# Key Handling 
# ---------------------------------------------------
def handle_key(event):

    global game_state, p1_choice_pending

    # Only handle keys when on game frame
    if get_mode() == "Single-Player":

        if event.keysym == "Return":

            if game_state == "result":
                game_state = "waiting"
                draw_waiting()
            return

        choice = KEY_MAP.get(event.keysym)
        if choice is None:
            return

        if game_state == "waiting":
            resolve_single(choice)

        elif game_state == "result":
            # Choice key from result: go straight into next round
            game_state = "waiting"
            draw_waiting()
            resolve_single(choice)

    elif get_mode() == "Multi-Player":
        p1_keys = {"a", "s", "d"}
        p2_keys = {"j", "k", "l"}
        key = event.keysym

        if key == "Return":

            if game_state == "result":
                game_state = "waiting"
                p1_choice_pending = None
                draw_waiting()
            return

        if game_state == "result":
            # Any game key resets to waiting, then falls through to register choice
            game_state = "waiting"
            p1_choice_pending = None
            draw_waiting()

        if game_state == "waiting":

            if key in p1_keys:
                p1_choice_pending = KEY_MAP[key]
                # Update canvas to show P1 has locked in
                canvas.delete("p1_status")
                canvas.create_text(
                    GAME_WIDTH // 2, 200,
                    text=f"Player 1: LOCKED IN ✓",
                    font=("Consolas", 16),
                    fill="#00ccff",
                    tags="p1_status"
                )

                if p1_choice_pending and _p2_locked:
                    pass   # handled below

            elif key in p2_keys:
                p2_choice = KEY_MAP[key]

                if p1_choice_pending is not None:
                    resolve_multi(p1_choice_pending, p2_choice)
                    p1_choice_pending = None

                else:
                    # P2 pressed before P1 — store temporarily via tag
                    canvas.delete("p2_status")
                    canvas.create_text(
                        GAME_WIDTH // 2, 260,
                        text=f"Player 2: LOCKED IN ✓",
                        font=("Consolas", 16),
                        fill="#ff9900",
                        tags="p2_status"
                    )
                    # store p2 choice so when p1 presses we can resolve
                    handle_key._p2_pending = p2_choice

            # Check if we had a stored p2 and now p1 just pressed
            if key in p1_keys and hasattr(handle_key, "_p2_pending"):
                resolve_multi(KEY_MAP[key], handle_key._p2_pending)
                del handle_key._p2_pending
                p1_choice_pending = None

# Sentinel used above (cleaner than another global)
_p2_locked = False

# ---------------------------------------------------
# START/RESTART GAME
# ---------------------------------------------------
def start_game():
    show_frame(game_frame)
    _launch_game()

def restart_game():
    _launch_game()

def _launch_game():
    global player_1_score, player_2_score, computer_score, game_state, p1_choice_pending

    player_1_score    = 0
    player_2_score    = 0
    computer_score    = 0
    game_state        = "waiting"
    p1_choice_pending = None

    if get_mode() == "Single-Player":
        score_label.config(text="Score: 0")
    else:
        score_label.config(text="P1: 0   P2: 0")

    restart_button.place_forget()
    draw_waiting()

def go_to_menu():
    show_frame(menu_frame)

# ---------------------------------------------------
# UI BUILDING
# ---------------------------------------------------
def build_menu_frame(parent):

    global mode_var

    frame = Frame(
        parent, 
        bg= "#0a0a0a"
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
    menu_button.pack(
        side=LEFT,
        padx=6,
        pady=4
    )
    
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
        padx=20, 
        pady=8,
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

    # Prevents both radiobuttons from being selected simultaneously at start
    mode_var = StringVar(value="Single-Player")

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

    # Key bindings 
    window.bind("<Escape>", lambda e: go_to_menu())
    window.bind("a", handle_key)
    window.bind("s", handle_key)
    window.bind("d", handle_key)

    window.bind("j", handle_key)
    window.bind("k", handle_key)
    window.bind("l", handle_key)
    window.bind("<Return>", handle_key)

    # Center window
    window.update()
    w, h = window.winfo_width(), window.winfo_height()
    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
    # width x height + x_position + y_position
    
    window.mainloop()

if __name__=="__main__":
    main()