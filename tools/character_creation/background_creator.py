import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os, json
from background_class import Background

# helper function
def parse_list_input(text: str) -> list:
    return [item.strip() for item in text.split(",") if item.strip()]


# setup paths
BASE_DIR = os.path.dirname(__file__)
BACKGROUND_FOLDER = os.path.join(BASE_DIR,"data", "background")
os.makedirs(BACKGROUND_FOLDER, exist_ok= True)


# Save Function
def save_background():
    name = name_entry.get()
    description = description_entry.get()
    starting_skills = parse_list_input (starting_skills_entry.get())
    starting_gear = parse_list_input(starting_gear_entry.get())
    wealth_modifier = int(wealth_modifier.get())

    if not name:
        messagebox.showerror("Missing Name", "Please enter a name for the armor.")
        return

    background = Background(
        name=name,
        description=description,
        starting_skills = starting_skills,
        starting_gear = starting_gear,
        wealth_modifier = wealth_modifier

    )

    filename = f"{name.lower().replace(' ', '_')}.json"
    path = os.path.join(BACKGROUND_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(background.to_dict(), f, indent=2)


    messagebox.showinfo("Saved", f"{background.name} saved to {filename}")
                        
    #clear feilds
    for entry in (name,description,starting_skills,starting_gear,wealth_modifier):
        entry.delete(0,'end')
    name_entry.focus()


# Create window
app = ttk.Window(title="Background Creator", themename="darkly", size=(600 , 700))

style = ttk.Style()
style.configure(
"info.TLabel",
font=("Georgia", 18),
justify = "center",
anchor= "center"
)

style = ttk.Style()
style.configure(
"success.TButton",
font=("Georgia", 24),
justify = "center",
anchor= "center"
)

ttk.Label(app, text="Background Creator", font=("Helvitica", 24, "bold")).pack(pady=10)

#Name
ttk.Label(app, text="Name:", style = "info.TLabel").pack()
name_entry = ttk.Entry(app)
name_entry.pack(pady=5)

# Description
ttk.Label(app,text="Description", style= "info.TLbel").pack()
description_entry = ttk.Entry(app)
description_entry.pack(pady=5)

# Starting skills
ttk.Label(app, text="Starting_skills (coma-separated):", style = "info.TLabel").pack()
starting_skills_entry = ttk.Entry(app)
starting_skills_entry.pack(pady=5)

#Starting Gear
ttk.Label(app, text="Starting gear (coma-separated)", style = "info.TLabel").pack()
starting_gear_entry = ttk.Entry(app)
starting_gear_entry.pack(pady=5)

# wealth modifier
ttk.Label(app, text="Wealth Modifier:", style = "info.TLabel").pack()
wealth_modifier_entry = ttk.Entry(app)
wealth_modifier_entry.pack(pady=5)

#Save Button
ttk.Button(app, text="Save Background", command=save_background, style="success.TButton").pack(pady=20)


app.mainloop()




                                       
                                       