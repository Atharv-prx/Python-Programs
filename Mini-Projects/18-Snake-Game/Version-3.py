# Upgrades from version-2:
# 1 --Adding Menu System
# 2 --Preventing food from spawning inside snake
# 3 --Multiple Food spawns
# 4 --Difficulty System
# 5 --Speed increases with score

from tkinter import *
import random

# ---------------------------------------------------
# CONSTANTS
# ---------------------------------------------------
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
DIFFICULTY_SPEEDS = {
    'Easy': 150,
    'Medium': 100,
    'Hard': 60
}

# ---------------------------------------------------
# GLOBALS
# ---------------------------------------------------
window        = None
canvas        = None
score_label   = None
restart_button = None
snake         = None
food_items    = []
score         = 0
direction     = "down"
next_direction = "down"
after_id      = None          # holds window.after() handle so i can cancel it

# Menu selection variables (set after window created)
difficulty_var  = None
food_count_var  = None

# ---------------------------------------------------
# CLASSES
# ---------------------------------------------------
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for x in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, 
                y + SPACE_SIZE, 
                fill=SNAKE_COLOR, 
                tags="snake"
            )
            self.squares.append(square)

class Food:
    def __init__(self, occupied):
        # Generate random coordinates for the food, ensuring it doesn't spawn on the snake or other food items
        while True:
            x = random.randint(0, GAME_WIDTH // SPACE_SIZE - 1) * SPACE_SIZE
            y = random.randint(0, GAME_HEIGHT // SPACE_SIZE - 1) * SPACE_SIZE
            if [x, y] not in occupied:
                break

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, 
            y + SPACE_SIZE, 
            fill=FOOD_COLOR, 
            tag="food"
        )

# ---------------------------------------------------
# Frame switching 
# ---------------------------------------------------
def show_frame(frame):
    frame.tkraise()

# ---------------------------------------------------
# GAME LOGIC
# ---------------------------------------------------
def next_turn(snake):

    global direction, next_direction, after_id, score, food_items

    direction = next_direction
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, 
        y + SPACE_SIZE, 
        fill=SNAKE_COLOR
        )

    snake.squares.insert(0, square)
    
    # Food Check
    ate = False
    for food in food_items[:]:
        # Check if snake head is on the same coordinates as any food item
        if x == food.coordinates[0] and y == food.coordinates[1]:

            score += 1
            score_label.config(text="Score:{}".format(score))

            canvas.delete("food")     # redraw remaining food
            food_items.remove(food)

            # Spawn replacement food
            occupied = snake.coordinates + [f.coordinates for f in food_items]
            food_items.append(Food(occupied))

            # Redraw all remaining food (they were deleted above)
            for f in food_items:
                fx, fy = f.coordinates
                canvas.create_oval(
                    fx, fy, fx + SPACE_SIZE, fy + SPACE_SIZE,
                    fill=FOOD_COLOR, tag="food"
                )
            ate = True
            break
    
    # If the snake didn't eat, remove the last square to maintain length. If it did eat, keep the tail to grow.
    if not ate:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Check if the snake has collided with the walls or itself
    if check_collisions(snake):
        game_over()

    else:
        speed = DIFFICULTY_SPEEDS[difficulty_var.get()]
        after_id = window.after(speed, next_turn, snake)

def change_direction(new_direction):
    global next_direction

    if new_direction == 'left':
        if direction != 'right':
            next_direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            next_direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            next_direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            next_direction = new_direction

def check_collisions(snake):
    # Check if the snake has collided with the walls
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():

    canvas.delete(ALL)

    canvas.create_text(
        GAME_WIDTH / 2, 
        GAME_HEIGHT / 2 - 60,
        font=("Consolas", 60), 
        text="GAME OVER", 
        fill="red"
    )

    canvas.create_text(
        GAME_WIDTH / 2, 
        GAME_HEIGHT / 2 + 10,
        font=("Consolas", 24), 
        text=f"Final Score: {score}", 
        fill="white"
    )

    restart_button.place(relx=0.5, 
                         rely=0.72, 
                         anchor=CENTER)

# ---------------------------------------------------
# START/RESTART GAME
# ---------------------------------------------------

def start_game():
    
    # Gets called from menu, switches to game frame then launches the game
    show_frame(game_frame)
    _launch_game()

def restart_game():
    # Called from in-game restart button
    _launch_game()

def _launch_game():
    global score, direction, next_direction, snake, food_items, after_id

    # Cancelling any running game loop
    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None
    
    score = 0
    direction = "down"
    next_direction = "down"
    food_items = []

    score_label.config(text="Score: 0")
    canvas.delete(ALL)
    restart_button.place_forget()

    snake = Snake()

    count = food_count_var.get()
    for _ in range(count):
        occupied = snake.coordinates + [f.coordinates for f in food_items]
        food_items.append(Food(occupied))

    window.after(100, next_turn, snake)

def go_to_menu():
    global after_id

    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None

    canvas.delete(ALL)
    restart_button.place_forget()
    show_frame(menu_frame)

# ---------------------------------------------------
# UI BUILDING
# ---------------------------------------------------
def build_menu_frame(parent):
    # Lowkey retro styled
    frame = Frame(parent, bg= "#0a0a0a")

    # TITLE
    Label(
        frame,
        text="🐍 SNAKE",
        font=("Consolas", 54, "bold"),
        fg="#00FF00", 
        bg="#0a0a0a"
    ).pack(pady=(60, 4))

    Label(
        frame,
        text="classic arcade",
        font=("Consolas", 14),
        fg="#3a7a3a", 
        bg="#0a0a0a"
    ).pack(pady=(0, 40))

    # DIFFICULTY
    Label(
        frame, text="DIFFICULTY",
        font=("Consolas", 13, "bold"),
        fg="#888888", 
        bg="#0a0a0a"
    ).pack()

    diff_frame = Frame(frame, bg="#0a0a0a")
    diff_frame.pack(pady=(6, 24))

    for level in ["Easy", "Medium", "Hard"]:
        color = {"Easy": "#00cc44", "Medium": "#ffaa00", "Hard": "#ff3333"}[level]
        Radiobutton(
            diff_frame,
            text=level,
            variable=difficulty_var,
            value=level,
            font=("Consolas", 13),
            fg=color, bg="#0a0a0a",
            activebackground="#0a0a0a",
            activeforeground=color,
            selectcolor="#1a1a1a",
            indicatoron=True,
            padx=10
        ).pack(side=LEFT, 
               padx=8)

    # FOOD COUNT
    Label(
        frame, text="FOOD ON SCREEN",
        font=("Consolas", 13, "bold"),
        fg="#888888", 
        bg="#0a0a0a"
    ).pack()

    food_frame = Frame(frame, 
                       bg="#0a0a0a")
    food_frame.pack(pady=(6, 40))

    for n in [1, 2, 3]:
        Radiobutton(
            food_frame,
            text=str(n),
            variable=food_count_var,
            value=n,
            font=("Consolas", 16, "bold"),
            fg="#00FF00", 
            bg="#0a0a0a",
            activebackground="#0a0a0a",
            activeforeground="#00FF00",
            selectcolor="#1a1a1a",
            indicatoron=True,
            padx=12
        ).pack(side=LEFT, 
               padx=14)

    # START BUTTON
    start_btn = Button(
        frame,
        text="▶  START GAME",
        font=("Consolas", 18, "bold"),
        fg="#000000", 
        bg="#00FF00",
        activebackground="#00cc00",
        activeforeground="#000000",
        relief=FLAT,
        padx=24, pady=10,
        cursor="hand2",
        command=start_game
    )
    start_btn.pack()

    # Subtle footer
    Label(
        frame,
        text="← → ↑ ↓  to move",
        font=("Consolas", 10),
        fg="#333333", 
        bg="#0a0a0a"
    ).pack(side=BOTTOM, pady=14)

    return frame

def build_game_frame(parent):
    # score label + canvas + hidden restart button + menu button
    global canvas, score_label, restart_button

    frame = Frame(parent, 
                  bg="#000000")

    # Top bar
    top_bar = Frame(frame, 
                    bg="#111111")
    top_bar.pack(fill=X)

    menu_btn = Button(
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
    menu_btn.pack(side=LEFT, 
                  padx=6, 
                  pady=4)

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

    # Restart button (hidden until game-over)
    restart_button = Button(
        canvas,
        text="RESTART",
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
    
    global window, menu_frame, game_frame, difficulty_var, food_count_var
    
    window = Tk()
    window.title("Snake Game")
    window.resizable(False, False)
    window.configure(bg="#000000")

    # Tk variables (must exist after window)
    difficulty_var = StringVar(value="Medium")
    food_count_var = IntVar(value=1)

    # Container holds all frames stacked
    container = Frame(window, bg="#000000")
    container.pack(fill=BOTH, expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # Build frames
    menu_frame = build_menu_frame(container)
    game_frame = build_game_frame(container)

    for f in (menu_frame, game_frame):
        f.grid(row=0, column=0, sticky="nsew")

    show_frame(menu_frame)

    # Keyboard bindings
    window.bind("<Left>",  lambda e: change_direction("left"))
    window.bind("<Right>", lambda e: change_direction("right"))
    window.bind("<Up>",    lambda e: change_direction("up"))
    window.bind("<Down>",  lambda e: change_direction("down"))

    # Center window
    window.update()
    w, h = window.winfo_width(), window.winfo_height()
    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    window.mainloop()

if __name__ == "__main__":
    main()