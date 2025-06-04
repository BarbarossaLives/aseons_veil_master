import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os,json

BASE_DIR = os.path.dirname(__file__)


def load_item_names_from_folder(folder_path):
    names = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            try:
                with open(os.path.join(folder_path, filename), "r") as f:
                    data = json.load(f)
                    names.append(data.get("name", "Unnamed"))
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    return sorted(names)


# Create the main window
app = ttk.Window(
    title="Embark Character Creator",
    themename="darkly",
    size=(600, 500),
    resizable=(False, False)
)

# Title
ttk.Label(app, text="Embark Character Creator", font=("Helvetica", 24, "bold")).pack(pady=10)

# Create Notebook
notebook = ttk.Notebook(app)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

# --- TAB 1: General Info ---
tab_general = ttk.Frame(notebook)
notebook.add(tab_general, text="General Info")

# Name
ttk.Label(tab_general, text="Character Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
name_entry = ttk.Entry(tab_general)
name_entry.grid(row=0, column=1, sticky="ew", padx=10)

# Ancestry
ancestry_path = os.path.join(BASE_DIR, "data", "ancestries")
ancestry_list = load_item_names_from_folder(ancestry_path)
ttk.Label(tab_general, text="Ancestry:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
ancestry_combobox = ttk.Combobox(tab_general, values=ancestry_list)
ancestry_combobox.grid(row=1, column=1, sticky="ew", padx=10)

# Size
ttk.Label(tab_general, text="Size:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
size_combobox = ttk.Combobox(tab_general, values=["Small", "Medium", "Large"])
size_combobox.grid(row=2, column=1, sticky="ew", padx=10)

# Background
background_path= os.path.join(BASE_DIR, "data", "background" )
background_list = load_item_names_from_folder(background_path)
ttk.Label(tab_general, text="Background:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
background_combobox = ttk.Combobox(tab_general, values= background_list)
background_combobox.grid(row=3, column=1, sticky="ew", padx=10)

# Make sure the columns resize nicely
tab_general.columnconfigure(1, weight=1)

# --- TAB 2: Attributes ---
tab_attributes = ttk.Frame(notebook)
notebook.add(tab_attributes, text="Attributes")

# Starting points
total_points = 10
remaining_var = ttk.IntVar(value=total_points)

# Attribute values
attributes = {
    "Agility": ttk.IntVar(value=0),
    "Instinct": ttk.IntVar(value=0),
    "Might": ttk.IntVar(value=0),
    "Wit": ttk.IntVar(value=0),
}

# Function to update remaining points
def update_remaining():
    used = sum(var.get() for var in attributes.values())
    remaining_var.set(total_points - used)

def add_point(attr):
    if remaining_var.get() > 0:
        attributes[attr].set(attributes[attr].get() + 1)
        update_remaining()

def remove_point(attr):
    if attributes[attr].get() > 0:
        attributes[attr].set(attributes[attr].get() - 1)
        update_remaining()

# Layout
row = 0
for attr, var in attributes.items():
    ttk.Label(tab_attributes, text=f"{attr}:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
    ttk.Button(tab_attributes, text="-", width=3, command=lambda a=attr: remove_point(a)).grid(row=row, column=1,padx=5)
    ttk.Label(tab_attributes, textvariable=var).grid(row=row, column=2,padx=15)
    ttk.Button(tab_attributes, text="+", width=3, command=lambda a=attr: add_point(a)).grid(row=row, column=3,padx=5)
    row += 1

# Remaining points display
ttk.Label(tab_attributes, text="Remaining Points:").grid(row=row, column=0, columnspan=2, pady=10, sticky="e")
ttk.Label(tab_attributes, textvariable=remaining_var, font=("Helvetica", 12, "bold")).grid(row=row, column=2, sticky="w")

# --- Calculated stats ---
ttk.Separator(tab_attributes).grid(row=row+1, column=0, columnspan=4, pady=10, sticky="ew")
row += 2

# Create display variables
calculated_stats = {
    "Health": ttk.IntVar(value=0),
    "Initiative": ttk.IntVar(value=0),
    "Encumbrance Max": ttk.IntVar(value=0)
}

def update_calculated_stats():
    agility = attributes["Agility"].get()
    instinct = attributes["Instinct"].get()
    might = attributes["Might"].get()
    wit = attributes["Wit"].get()

    calculated_stats["Health"].set(10 + might * 2)
    calculated_stats["Initiative"].set(agility + instinct)
    calculated_stats["Encumbrance Max"].set(might * 4)

# Hook into the point updater
def add_point(attr):
    if remaining_var.get() > 0:
        attributes[attr].set(attributes[attr].get() + 1)
        update_remaining()
        update_calculated_stats()

def remove_point(attr):
    if attributes[attr].get() > 0:
        attributes[attr].set(attributes[attr].get() - 1)
        update_remaining()
        update_calculated_stats()

# Display calculated stats
for label, var in calculated_stats.items():
    ttk.Label(tab_attributes, text=f"{label}:").grid(row=row, column=0, columnspan=2, sticky="e", padx=10)
    ttk.Label(tab_attributes, textvariable=var, font=("Helvetica", 10)).grid(row=row, column=2, sticky="w")
    row += 1

# Launch the GUI
app.mainloop()
