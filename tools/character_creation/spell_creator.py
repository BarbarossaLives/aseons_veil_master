import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os, json
from spell_class import Spell



# Setup paths
BASE_DIR = os.path.dirname(__file__)
SPELL_FOLDER = os.path.join(BASE_DIR, "data", "spell")
os.makedirs(SPELL_FOLDER, exist_ok=True)

# Save function
def save_spell():
    name = name_entry.get()
    school = school_entry.get()
    defense = defense_entry.get()
    difficulty = difficulty_entry.get()
    description = description_entry.get()


    spell = Spell(
        name=name,
        school=school,
        defense=defense,
        difficulty=difficulty,
        description=description,
    )

    filename = f"{name.lower().replace(' ', '_')}.json"
    path = os.path.join(SPELL_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(spell.to_dict(), f, indent=2) 

    messagebox.showinfo("Saved", f"{spell.name} saved to {filename}")

    # Clear fields for the next entry
    for entry in (name_entry, school_entry, defense_entry, difficulty_entry, description_entry):
        entry.delete(0, 'end')
    name_entry.focus()


# Create window
app = ttk.Window(title="Spell Creator", themename="darkly", size=(600, 950))

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

ttk.Label(app, text="Spell Creator", font=("Helvetica", 24, "bold")).pack(pady=10)

# Name
ttk.Label(app, text="Name:", style = "info.TLabel").pack()
name_entry = ttk.Entry(app)
name_entry.pack(pady=5)

# Tage
ttk.Label(app, text="School:", style = "info.TLabel").pack()
school_entry = ttk.Entry(app)
school_entry.pack(pady=5)

# Defense
ttk.Label(app, text="Defense", style="info.TLabel").pack()
defense_entry = ttk.Entry(app)
defense_entry.pack(pady=5)

# Difficulty
ttk.Label(app, text="Difficulty", style="info.TLabel").pack()
difficulty_entry = ttk.Entry(app)
difficulty_entry.pack(pady=5)


# Description
ttk.Label(app, text="Description:", style="info.TLabel").pack()
description_entry = ttk.Entry(app)
description_entry.pack(pady=5)


#Save Button
ttk.Button(app, text="Save Spell", command=save_spell, style="success").pack(pady=15)

app.mainloop()