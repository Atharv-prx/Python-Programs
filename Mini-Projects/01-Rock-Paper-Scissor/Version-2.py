from tkinter import *
import random

# ---------
# CONSTANTS
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

# -------
# GLOBALS
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

# for easter egg 🙂
idle_after_id = None
idle_timers = []

def idle_message_1():
    canvas.delete("idle")

    canvas.create_text(
        GAME_WIDTH // 2,
        GAME_HEIGHT // 2 + 100,
        text="You there? (ಠ_ಠ)",
        font=("Consolas", 16, "bold"),
        fill="#ff9900",
        tags="idle"
    )

def idle_message_2():
    canvas.delete("idle")

    canvas.create_text(
        GAME_WIDTH // 2,
        GAME_HEIGHT // 2 + 100,
        text="Still waiting... (¬_¬)",
        font=("Consolas", 16, "bold"),
        fill="#ff9900",
        tags="idle"
    )

def idle_message_3():
    canvas.delete("idle")

    canvas.create_text(
        GAME_WIDTH // 2,
        GAME_HEIGHT // 2 + 100,
        text="Wake up! (>_<)",
        font=("Consolas", 16, "bold"),
        fill="#ff9900",
        tags="idle"
    )

def idle_message_4():
    canvas.delete("idle")

    canvas.create_text(
        GAME_WIDTH // 2,
        GAME_HEIGHT // 2 + 100,
        text="Achievement unlocked: Professional Procrastinator :)",
        font=("Consolas", 16, "bold"),
        fill="#ff9900",
        tags="idle"
    )

def idle_message_5():
    canvas.delete("idle")

    canvas.create_text(
    GAME_WIDTH // 2,
    GAME_HEIGHT // 2 + 100,
    text="Fine, i'll wait ( >_< )",
    font=("Consolas", 16, "bold"),
    fill="#ff9900",
    tags="idle"
    )

def reset_idle_timer():
    global idle_timers

    # Cancelling old timers
    for timer_id in idle_timers:
        window.after_cancel(timer_id)

    idle_timers.clear()

    # Remove old idle text
    canvas.delete("idle")
    canvas.delete("idle_warning")

    # Schedule new timers
    idle_timers.append(window.after(10000, idle_message_1))
    idle_timers.append(window.after(20000, idle_message_2))
    idle_timers.append(window.after(30000, idle_message_3))
    idle_timers.append(window.after(45000, idle_message_4))
    idle_timers.append(window.after(60000, idle_message_5))

# -------
# Helpers 
def show_frame(frame):
    frame.tkraise()

def get_mode():
    return mode_var.get()

# --------------
# Canvas Drawing
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
            text="Waiting for choice (^w^)",
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
            text="Player 1: waiting (o_o)",
            font=("Consolas", 16),
            fill="#888888",
            tags="p1_status"
        )
        canvas.create_text(
            GAME_WIDTH // 2, 260,
            text="Player 2: waiting (^-^)",
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
        text="Press Enter for next round  (or A/S/D/J/K/L to pick immediately)",
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
        return "#00FF00", "YOU WIN :D"
    elif outcome == "lose":
        return "#FF4444", "YOU LOSE :("
    else:
        return "#ffff00", "DRAW (•_•)"

# ----------
# Game Logic

def resolve_single(player_choice):
    global player_1_score, computer_score, game_state

    comp_choice = random.choice(CHOICES)

    if player_choice == comp_choice:
        outcome = "draw"

    elif WINS_AGAINST[player_choice] == comp_choice:
        outcome = "win"
        player_1_score += 1

    else:
        outcome = "lose"
        computer_score += 1
    
    score_label.config(text=f"Score: {player_1_score}")
    game_state = "result"
    draw_result_single(player_choice, comp_choice, outcome)

def resolve_multi(p1, p2):
    global player_1_score, player_2_score, game_state

    if p1 == p2:
        outcome = "draw"
    elif WINS_AGAINST[p1] == p2:
        outcome = "p1"
        player_1_score += 1
    else:
        outcome = "p2"
        player_2_score += 1

    score_label.config(text=f"P1: {player_1_score}   P2: {player_2_score}")
    game_state = "result"
    draw_result_multi(p1, p2, outcome)

# ------------
# Key Handling 
def handle_key(event):
    reset_idle_timer()
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
                    # store p2 choice so when p1 presses i can resolve
                    handle_key._p2_pending = p2_choice

            # Check if we had a stored p2 and now p1 just presed
            if key in p1_keys and hasattr(handle_key, "_p2_pending"):
                resolve_multi(KEY_MAP[key], handle_key._p2_pending)
                del handle_key._p2_pending
                p1_choice_pending = None

# Sentinel used above (cleaner than another global)
_p2_locked = False

# ------------------
# START/RESTART GAME

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
    
    reset_idle_timer()

def go_to_menu():
    show_frame(menu_frame)

# -----------
# UI BUILDING

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
        text= "Be sure to read keybinds below ( >_< )",
        font= ("Consolas", 14),
        fg= "#3a7a3a",
        bg= "#0a0a0a"
    ).pack(pady=(0,40))
    
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

    Label(
        frame, 
        text="Feel free to give me ideas about improving this program :)",
        font=("Consolas", 10),
        fg="#333333", 
        bg="#0a0a0a",
    ).pack(side=BOTTOM, pady=14)

    return frame

def build_game_frame(parent):
    
    global canvas, score_label, restart_button 

    frame = Frame(parent,
                  bg= "#000000")
    
    top_bar = Frame(frame, 
                    bg="#111111")
    top_bar.pack(fill=X)
    
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
    
    canvas = Canvas(
        frame,
        bg=BACKGROUND_COLOR,
        height=GAME_HEIGHT,
        width=GAME_WIDTH,
        highlightthickness=0
    )
    canvas.pack()
 
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

# ----
# MAIN
def main():
    
    global window, menu_frame, game_frame, mode_var

    window = Tk()
    window.title("Rock Paper Scissors")
    window.resizable(False, False)
    window.configure(bg="#000000")

    # One of the bug fixes that i encountered, basically prevents both radiobutons to be enabled at same time
    mode_var = StringVar(value="Single-Player")

    container = Frame(window, bg="#000000")
    container.pack(fill=BOTH, expand=True) 

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    menu_frame = build_menu_frame(container)
    game_frame = build_game_frame(container)

    for frame in (menu_frame, game_frame):
        frame.grid(row=0, column=0, sticky= 'nsew')
    
    show_frame(menu_frame)

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