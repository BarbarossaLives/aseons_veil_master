import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os, json
from weapon_class import Weapon

# Setup paths
BASE_DIR = os.path.dirname(__file__)
WEAPON_FOLDER = os.path.join(BASE_DIR, "data", "weapons")
os.makedirs(WEAPON_FOLDER, exist_ok=True)



def save_weapon():
    name = name_entry.get()
    tags = [t.strip() for t in tags_entry.get().split(",") if t.strip()]
    description = description_entry.get()
    damage = damage_entry.get()
    try:
        bulk = int(bulk_entry.get())
        qp = int(qp_entry.get())
        cost = int(cost_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Bulk, QP and Cost must be integers.")
        return
 
    if not name:
        messagebox.showerror("Missing Name", "Please enter a name for the weapon.")
        return

    weapon = Weapon(name=name, tags=tags, description=description, damage=damage, bulk=bulk, qp=qp, cost=cost)
    filename = f"{name.lower().replace(' ', '_')}.json"
    path = os.path.join(WEAPON_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(weapon.to_dict(), f, indent=2)

    if os.path.exists(path):
        if not messagebox.askyesno("Overwrite?", f"A weapon named '{name}' already exists. Overwrite it?"):
            return


    messagebox.showinfo("Saved", f"{weapon.name} saved to {filename}")

    # Clear fields for the next entry
    name_entry.delete(0, 'end')
    tags_entry.delete(0, 'end')
    description_entry.delete(0, 'end')
    damage_entry.delete(0, 'end')
    bulk_entry.delete(0, 'end')
    qp_entry.delete(0, 'end')
    cost_entry.delete(0, 'end')
    name_entry.focus()


# Create window
app = ttk.Window(title="Create New Weapon", themename="darkly", size=(600, 850))

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

ttk.Label(app, text="Weapon Creator", font=("Helvetica", 24)).pack(pady=10)

# Name
ttk.Label(app, text="Name:",style="info.Tlabel").pack()
name_entry = ttk.Entry(app)
name_entry.pack(pady=5)

# Tags
ttk.Label(app, text="Tags (comma-separated):", style="info.Tlabel").pack()
tags_entry = ttk.Entry(app)
tags_entry.pack(pady=5)

# Desription
ttk.Label(app, text="Descripton:", style="info.Tlabel").pack()
description_entry = ttk.Entry(app)
description_entry.pack(pady=5)

# Damage
ttk.Label(app, text="Damage (e.g., 1d6):", style="info.Tlabel").pack()
damage_entry = ttk.Entry(app)
damage_entry.pack(pady=5)

# Bulk
ttk.Label(app, text="Bulk:", style="info.Tlabel").pack()
bulk_entry = ttk.Entry(app)
bulk_entry.pack(pady=5)

# QP
ttk.Label(app, text="QP (quality points):", style="info.Tlabel").pack()
qp_entry = ttk.Entry(app)
qp_entry.pack(pady=5)

# Cost
ttk.Label(app,text="Cost:", style="info.Tlabel").pack()
cost_entry = ttk.Entry(app)
cost_entry.pack(pady=5)


# Save button
ttk.Button(app, text="Save Weapon", command=save_weapon, style="success.tButton").pack(pady=15)

app.mainloop()
