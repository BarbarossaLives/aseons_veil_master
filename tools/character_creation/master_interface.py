import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import os

# Path setup
BASE_DIR = os.path.dirname(__file__)

# Create the window
app = ttk.Window(
    title="Aeon's Veil Toolkit",
    themename="darkly",
    size=(600, 800),
    resizable=(False, False)
)

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

ttk.Label(app, text="Aeon's Veil Toolkit", font=("Helvetica", 24, "bold")).pack(pady=20)

# --- Launchers for tools ---

def run_tool(script_name):
    full_path = os.path.abspath(os.path.join(BASE_DIR, script_name))
    subprocess.Popen(["python3", full_path])  

# Ancestry Creator
ttk.Button(app, text="Create Ancestry",command=lambda: run_tool("ancestry_creator.py"), style="success.TButton").pack(pady=10)

# Background Creator
ttk.Button(app,text="Background Creator", command=lambda:run_tool("background_creator.py"), style="success.TButton").pack(pady=10)


# Weapon Creator
ttk.Button(app, text="Create Weapon", command=lambda: run_tool("weapon_creator.py"), style="success.TButton").pack(pady=10)

# Armor Creator
ttk.Button(app, text="Create Armor",command=lambda: run_tool("armor_creator.py"), style="success.TButton").pack(pady=10)

# Feat Creator
ttk.Button(app, text="Create Feat",command=lambda: run_tool("feat_creator.py"), style="success.TButton").pack(pady=10)


# Character Builder (in development)
ttk.Button(app, text="Character Builder", command=lambda: run_tool("core/character_class.py"), style="success.TButton").pack(pady=10)


# Dice Roller
ttk.Button(app, text="Roll Dice", command=lambda: run_tool("../dice_roller/roller_phase_1.py"), style="success.TButton").pack(pady=10)

# Launch GUI
app.mainloop()
