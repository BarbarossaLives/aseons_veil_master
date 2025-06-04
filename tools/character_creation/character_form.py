import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tabs.general_tab import build_general_tab
from tabs.attributes_tab import build_attributes_tab
from tabs.skills_tab import build_skills_tab
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

# Character state shared across tabs
state = {
    # --- Character Identity ---
    "name": ttk.StringVar(),
    "ancestry": ttk.StringVar(),
    "background": ttk.StringVar(),
    "size": ttk.StringVar(),
    "traits": [],
    "starting_skills": [],
    "starting_gear": [],
    "journal_notes": ttk.StringVar(),

    # --- Core Attributes ---
    "attributes": {
        "Agility": ttk.IntVar(value=0),
        "Instinct": ttk.IntVar(value=0),
        "Might": ttk.IntVar(value=0),
        "Wit": ttk.IntVar(value=0)
    },

    # --- Calculated Stats ---
    "calculated": {
        "Health": ttk.IntVar(value=0),
        "Initiative": ttk.IntVar(value=0),
        "Encumbrance Max": ttk.IntVar(value=0)
    }
}




# Title
ttk.Label(app, text="Embark Character Creator", font=("Helvetica", 24, "bold")).pack(pady=10)

# Create Notebook
notebook = ttk.Notebook(app)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

build_general_tab(notebook, state)
build_attributes_tab(notebook, state)
build_skills_tab(notebook, state)



# Launch the GUI
app.mainloop()
