import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os, json
from spell_class import Spell


#HelperFunction
def parse_list_input(text: str) -> list:
    return [item.strip() for item in text.split(",") if item.strip()]


# Setup paths
BASE_DIR = os.path.dirname(__file__)
SPELL_FOLDER = os.path.join(BASE_DIR, "data", "spell")
os.makedirs(SPELL_FOLDER, exist_ok=True)

# Save function
def save_armor():
    name = name_entry.get()
    tags = parse_list_input(tags_entry.get())
    description = description_entry.get()
    fp_cost = int(fp_cost.get())
    area = area_entry.get()
    duration = duration_entry.get()
    range = range_entry.get()
    concentration= concentration_entry.get()



    if not name:
        messagebox.showerror("Missing Name", "Please enter a name for the armor.")
        return

    armor = Armor(
        name=name,
        tags=tags,
        description=description,
        fp_cost=fp_cost,
        area=area,
        duration=duration,
        range=range,
        concentration=concentration

    )

    filename = f"{name.lower().replace(' ', '_')}.json"
    path = os.path.join(SPELL_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(spell.to_dict(), f, indent=2) 

    messagebox.showinfo("Saved", f"{armor.name} saved to {filename}")

    # Clear fields for the next entry
    for entry in (name_entry, tags_entry, fp_cost_entry, area_entry, duration_entry, concentration_entry, description_entry):
        entry.delete(0, 'end')
    name_entry.focus()


# Create window
app = ttk.Window(title="Spell Creator", themename="darkly", size=(600, 850))

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
ttk.Label(app, text="Tags: (coma-seperated)", style = "info.TLabel").pack()
tags_entry = ttk.Entry(app)
tags_entry.pack(pady=5)

# FPcost
ttk.Label(app, text="Focus Point Coast:", style = "info.TLabel").pack()
fp_cost_entry = ttk.Entry(app)
fp_cost_entry.pack(pady=5)