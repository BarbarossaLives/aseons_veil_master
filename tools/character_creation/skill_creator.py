import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os,json
from skill_class import Skill

def parse_list_input(text: str) -> list:
    return[item.strip() for item in text.split(",") if item.strip()]

# Setup paths
BASE_DIR = os.path.dirname(__file__)
SKILL_FOLDER = os.path.join(BASE_DIR, "data", "skills")
os.makedirs(SKILL_FOLDER, exist_ok=True)


#save function
def save_skill():
    name = name_entry.get()
    type = parse_list_input(type_entry.get())
    pips = parse_list_input(type_entry.get())
    roll = parse_list_input(type_entry.get())


    skill = Skill(
        name=name, 
        type=type,
        pips=pips,
        roll=roll
    )

    filename = f"{name.lower().replace(' ', '_')}.json"
    path = os.path.join(SKILL_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(skill.to_dict(), f, indent=2)

    messagebox.showinfo("Saved", f"{skill.name} saved to (filename)")

    # Clear felds for the next entry
    for entry in (name_entry,type_entry,pips_entry,roll_entry):
        entry.delete(0, 'end')
    name_entry.focus()


# Create wndow
app = ttk.Window(title="Skill Creator", themename="darkly", size=(600,850))

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

ttk.Label(app, text="Name:", style="info.TLabel").pack()
name_entry = ttk.Entry(app)
name_entry.pack(pady=5)

ttk.Label(app, text="Skill Type", style = "info.TLabel").pack()
type_entry = ttk.Entry(app)
type_entry.pack(pady=5)

ttk.Label(app, text="Pips", style="info.TLabel").pack()
pips_entry = ttk.Entry(app)
pips_entry.pack(pady=5)

ttk.Label(app, text="Rolls", style="info.TLabel").pack()
roll_entry = ttk.Entry(app)
roll_entry.pack(pady=5)

ttk.Button(app, text="Save Skill", command=save_skill,
style="success.TButton").pack(pady=20)

app.mainloop()