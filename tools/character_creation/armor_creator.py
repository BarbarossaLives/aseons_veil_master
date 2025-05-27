import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os, json
from armor_class import Armor


#HelperFunction
def parse_list_input(text: str) -> list:
    return [item.strip() for item in text.split(",") if item.strip()]


# Setup paths
BASE_DIR = os.path.dirname(__file__)
ARMOR_FOLDER = os.path.join(BASE_DIR, "data", "armor")
os.makedirs(ARMOR_FOLDER, exist_ok=True)



# Save function
def save_armor():
    name = name_entry.get()
    tags = parse_list_input(tags_entry.get())
    description = description_entry.get()
    try:
        ac_bonus = int(ac_entry.get())
        bulk = int(bulk_entry.get())
        qp = int(qp_entry.get())
        cost = int(cost_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "AC Bonus, Bulk, QP, and Cost must be integers.")
        return

    if not name:
        messagebox.showerror("Missing Name", "Please enter a name for the armor.")
        return

    armor = Armor(
        name=name,
        tags=tags,
        description=description,
        ac_bonus=ac_bonus,
        bulk=bulk,
        qp=qp,
        cost=cost,
        
    )

    filename = f"{name.lower().replace(' ', '_')}.json"
    path = os.path.join(ARMOR_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(armor.to_dict(), f, indent=2)

    messagebox.showinfo("Saved", f"{armor.name} saved to {filename}")

    # Clear fields for the next entry
    for entry in (name_entry, tags_entry, ac_entry, bulk_entry, qp_entry, cost_entry, description_entry):
        entry.delete(0, 'end')
    name_entry.focus()

# Create window
app = ttk.Window(title="Armor Creator", themename="darkly", size=(600, 850))

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

ttk.Label(app, text="Armor Creator", font=("Helvetica", 24, "bold")).pack(pady=10)

# Name
ttk.Label(app, text="Name:", style = "info.TLabel").pack()
name_entry = ttk.Entry(app)
name_entry.pack(pady=5)

# Tags
ttk.Label(app, text="Tags (comma-separated):", style = "info.TLabel").pack()
tags_entry = ttk.Entry(app)
tags_entry.pack(pady=5)

# Description
ttk.Label(app, text="Description:", style = "info.TLabel").pack()
description_entry = ttk.Entry(app)
description_entry.pack(pady=5)

# AC Bonus
ttk.Label(app, text="AC Bonus:", style = "info.TLabel").pack()
ac_entry = ttk.Entry(app)
ac_entry.pack(pady=5)

# Bulk
ttk.Label(app, text="Bulk:", style = "info.TLabel").pack()
bulk_entry = ttk.Entry(app)
bulk_entry.pack(pady=5)

# QP
ttk.Label(app, text="Quality Points (QP):", style = "info.TLabel").pack()
qp_entry = ttk.Entry(app)
qp_entry.pack(pady=5)

# Cost
ttk.Label(app, text="Cost (¤):", style = "info.TLabel").pack()
cost_entry = ttk.Entry(app)
cost_entry.pack(pady=5)



# Save Button
ttk.Button(app, text="Save Armor", command=save_armor, style="success.TButton").pack(pady=20)

app.mainloop()
