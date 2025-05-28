import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os

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
ttk.Label(tab_general, text="Ancestry:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
ancestry_combobox = ttk.Combobox(tab_general, values=["Human", "Elf", "Orc", "Dwarf"])
ancestry_combobox.grid(row=1, column=1, sticky="ew", padx=10)

# Size
ttk.Label(tab_general, text="Size:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
size_combobox = ttk.Combobox(tab_general, values=["Small", "Medium", "Large"])
size_combobox.grid(row=2, column=1, sticky="ew", padx=10)

# Background
ttk.Label(tab_general, text="Background:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
background_combobox = ttk.Combobox(tab_general, values=["Innkeeper", "Soldier", "Scholar"])
background_combobox.grid(row=3, column=1, sticky="ew", padx=10)

# Make sure the columns resize nicely
tab_general.columnconfigure(1, weight=1)

# Launch the GUI
app.mainloop()
