 # imports
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar
import random

# variable declaration

pad_x = 8
pad_y = 5

def main():     

    #Master GUI setup
    app = ttk.Window(themename="darkly")
    app.title("Dice Roller - Phase 1")
    app.geometry("500x700")
    app.place_window_center()
    dice_pool = []
    results_pool = []
    state = {'modifier': 0}
    
    
    def add_die(die_type):
        dice_pool.append(die_type)
        dice_list.config(
        text="Dice Pool: " + ", ".join(dice_pool)
        )

        
    def adjust_modifier(mod):
        state["modifier"] += mod
        modifier_total.config(text=
        f"Modifier: {state['modifier']}")
        
    def roll(dice_pool, results_pool, results_list, state):
        results_number = []
        results_pool.clear()
        for die in dice_pool:
            sides = int(die[1:])
            roll_result=random.randint(1,sides)
            print(roll_result) 
            results_pool.append(str(roll_result))
            results_number.append(roll_result)
        
        results_list.config(text="Results: " + ", ".join(results_pool))   
        
        grand_total = sum(results_number) + state["modifier"]
        grand_total_text = str(grand_total)
        result_total.config(text="Total:" + grand_total_text)
        
        dice_pool.clear()
        dice_list.config(text="Dice Pool: ")
        
        state['modifier'] = 0
        modifier_total.config(text="Modifier: 0")
        
    
    # style configuration    
    style = ttk.Style()
    style.configure(
    "info.TLabel",
    font=("Georgia", 20, "bold"),
    justify = "center",
    anchor= "center"
    )
    
    style = ttk.Style()
    style.configure(
    "success.TLabel",
    font=("Georgia", 16, "bold"),
    justify = "center",
    anchor= "center"
    )
    
    style = ttk.Style()
    style.configure(
    "info.Labelframe",
    font=("Georgia", 20, "bold"),
    justify = "center",

    )
    
    style = ttk.Style()
    style.configure(
    "success.Labelframe",
    font=("Georgia", 20, "bold"),
    justify = "center",

    )

    style.configure(
    "success.TButton",
    font=("Veranda", 16, "bold"),
    relief = "raised",
    width=5
    )
    style.configure(
    "info.TButton",
    font=("Veranda", 16, "bold"),
    relief = "raised",
    width=5
    )
    
    dice_frame = ttk.Labelframe(
        app,
        text='Click to add to dice pool',
        bootstyle="info.Labelframe",
        borderwidth=5,)
    dice_frame.config(width=650)
    dice_frame.grid(
        row=1, column=0, pady=10,columnspan="4")
    modifier_frame = ttk.LabelFrame(
        app,
        text="Click to add your modfier",
        bootstyle = "success.Labelframe",
        borderwidth=5   )
    modifier_frame.grid(
        row=4, column=0, padx=10, pady=10,)
    results_frame=ttk.LabelFrame(
        app,
        text="The Results",
        bootstyle="info.Labelframe",
        borderwidth=8
    )
    results_frame.grid(
        row=9,
        column=0,
        columnspan=4
    )
    
    

    # variable declaration

    pad_x = 8
    pad_y = 5

    
    # dice  section
    label = ttk.Label(
    app,
    text="Aeon's Veil Dice Roller",
    style = "info.TLabel",

    )
    label.grid(
        row="0",
        column="0",
        columnspan="4",
        pady=20
    )


    D4_button = ttk.Button(
            dice_frame, text="D4",
            command=lambda: add_die("D4"),  
            style = "info.TButton"
        )
    D4_button.grid(
            row="1",
            column="0",
            pady=pad_y,
            padx=pad_x
        )
        
    D6_button = ttk.Button(
        dice_frame, text="D6",
        command=lambda: add_die("D6"),  
        style = "info.TButton"
    )
    D6_button.grid(
        row="1",
        column="1",
        pady=pad_y,
        padx=pad_x
    )

    D8_button = ttk.Button(
        dice_frame, text="D8",
        command=lambda: add_die("D8"),  
        style = "info.TButton"
    )
    D8_button.grid(
        row="1",
        column="2",
        pady= pad_y,
        padx= pad_x
    )

    D10_button = ttk.Button(
        dice_frame, text="D10",
        command=lambda: add_die("D10"),  
        style = "info.TButton"
    )
    D10_button.grid(
        row="1",
        column="3",
        pady= pad_y,
        padx= pad_x
    )

    D12_button = ttk.Button(
        dice_frame, text="D12",
        command=lambda: add_die("D12"),  
        style = "info.TButton"
    )
    D12_button.grid(
        row="2",
        column="0",
        pady=pad_y,
        padx= pad_x
    )

    D100_button = ttk.Button(
        dice_frame, text="D100",
        command=lambda: add_die("D100"),  
        style = "info.TButton"
    )
    D100_button.grid(
        row="2",
        column="1",
        pady=pad_y,
        padx= pad_x
    )

    D20_button = ttk.Button(
        dice_frame, text="D20",
        command=lambda: add_die("D20"),  
        style = "info.TButton",
        width = 13
    )
    D20_button.grid(
        row="2",
        column="2",
        columnspan=2
    )
    
    dice_list = ttk.Label(
        dice_frame,
        font=("Verdana", 12),
        text="dice list",
        style="info",
        wraplength=400,
        justify="left",
    )
    dice_list.grid(
        row=4,
        column=0,
        columnspan=4
    )
    
    # Modifier Section
    plus_one_buttom = ttk.Button(
        modifier_frame,text="+1",
        command=lambda: adjust_modifier(1),
        style = "success.TButton",
        width= 13
    )
    plus_one_buttom.grid(
        row=4,
        column="0",
        columnspan="2",
        padx=pad_x  
    )
    
    minus_one_buttom = ttk.Button(
        modifier_frame,text="-1",
        command=lambda: adjust_modifier(-1),
        style = "success.TButton",
        width=13
    )
    minus_one_buttom.grid(
        row=4,
        column="2",
        columnspan="2",
        padx=pad_x  
    )
    modifier_total = ttk.Label(
        modifier_frame,
        text = "total modifier",
        style = "success.TLabel"  
    )
    modifier_total.grid(
        row=5,
        column=0,
        columnspan=4
    )
# roll button

    roll_button = ttk.Button(
        app,text="ROLL",
        command=lambda:roll(dice_pool, results_pool, results_list, state),
        style="info.TButton",
    )
    roll_button.grid(
        row=7,
        column=0,
       
    )


# results section
    results_list = ttk.Label(
        results_frame,
        text = "Results:",
        style= "info.TLabel",
    )
    results_list.grid(
        row=9,
        column=0,
        columnspan=4
        
    )
    
    result_total = ttk.Label(
        results_frame,
        text="final result",
        style= "info.TLabel",
    
    )
    result_total.grid(
        row=10,
        column=0,
        columnspan=4,
        padx=pad_x
    )
    

    
    app.mainloop()

if __name__ == "__main__":
    main()