import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os, json
from ancestry_class import Ancestry

# --- Helper Functions ---

def parse_list_input(text: str) -> list:
    return [item.strip() for item in text.split(",") if item.strip()]

def parse_bonus_input(text: str) -> dict:
    bonuses = {}
    pairs = text.split(',')
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(':')
            try:
                bonuses[key.strip()] = int(value.strip())
            except ValueError:
                print(f"⚠️ Could not parse value for: {pair}")
    return bonuses

# --- File Paths ---

BASE_DIR = os.path.dirname(__file__)
ANCESTRY_FOLDER = os.path.join(BASE_DIR, "data", "ancestries")
os.makedirs(ANCESTRY_FOLDER, exist_ok=True)

# --- Save Logic ---

def save_ancestry():
    name = name_entry.get()
    size = size_entry.get()
    traits = parse_list_input(traits_entry.get())
    bonuses = parse_bonus_input(bonuses_entry.get())
    

    if not name:
        messagebox.showerror("Missing Name", "Please enter a name for the ancestry.")
        return


    ancestry = Ancestry(
        name=name,
        size=size,
        traits=traits,
        bonuses=bonuses,
    
    )

    filename = f"{name.lower().replace(' ', '_')}.json"
    path = os.path.join(ANCESTRY_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(ancestry.to_dict(), f, indent=2)

    messagebox.showinfo("Saved", f"{ancestry.name} saved to {filename}")

    # Clear fields
    for entry in (name_entry, size_entry, traits_entry, bonuses_entry):
        entry.delete(0, 'end')

    name_entry.focus()

# --- GUI Window ---

app = ttk.Window(title="Ancestry Creator", themename="darkly")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
print(screen_height)
print(screen_width)
width = 600
height = 700
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

app.geometry(f"{width}x{height}+{x}+{y}")


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

ttk.Label(app, text="Ancestry Creator", font=("Helvetica", 24, "bold")).pack(pady=10)

# Name
ttk.Label(app, text="Name:",style="info.Tlabel").pack()
name_entry = ttk.Entry(app)
name_entry.pack(pady=5)

# Size
ttk.Label(app, text="Size:",style="info.Tlabel").pack()
size_entry = ttk.Entry(app)
size_entry.pack(pady=5)

# Traits
ttk.Label(app, text="Traits (comma-separated):",style="info.Tlabel").pack()
traits_entry = ttk.Entry(app)
traits_entry.pack(pady=5)

# Bonuses
ttk.Label(app, text="Bonuses (e.g., Might:1, Agility:2):",style="info.Tlabel").pack()
bonuses_entry = ttk.Entry(app)
bonuses_entry.pack(pady=5)



# Save Button
ttk.Button(app, text="Save Ancestry", command=save_ancestry, style="success").pack(pady=15)

app.mainloop()
