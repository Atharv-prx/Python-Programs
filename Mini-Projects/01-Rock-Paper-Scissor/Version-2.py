from tkinter import *

def build_menu_frame(parent):
    frame = Frame(parent, 
                  bg= "#0a0a0a")
    
    Label(
        frame,
        text="Rock🪨 Paper📃 Scissors✂️",
        font=("Consolas", 30, "bold"),
        fg= "#00FF00",
        bg= "#0a0a0a"
    ).pack()

    return frame

def main():

    window = Tk()
    window.title("Rock Paper Scissors")
    window.resizable(False, False)
    window.configure(bg="#000000")
    
    menu_frame = build_menu_frame(window)
    menu_frame.pack(padx=20, pady=20)

    window.mainloop()

if __name__=="__main__":
    main()