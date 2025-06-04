import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils import load_item_names_and_data

def build_general_tab(notebook, state):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="General Info")

    # Paths to data folders
    ancestry_path = os.path.join(os.path.dirname(__file__), "..", "data", "ancestries")
    background_path = os.path.join(os.path.dirname(__file__), "..", "data", "background")

    # Load JSON templates
    ancestry_data = load_item_names_and_data(ancestry_path)
    background_data = load_item_names_and_data(background_path)

    # --- Character Name ---
    ttk.Label(tab, text="Character Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    name_entry = ttk.Entry(tab, textvariable=state["name"])
    name_entry.grid(row=0, column=1, sticky="ew", padx=10)

    # --- Ancestry ---
    ttk.Label(tab, text="Ancestry:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    ancestry_cb = ttk.Combobox(tab, values=list(ancestry_data.keys()), textvariable=state["ancestry"])
    ancestry_cb.grid(row=1, column=1, sticky="ew", padx=10)

    # --- Background ---
    ttk.Label(tab, text="Background:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    background_cb = ttk.Combobox(tab, values=list(background_data.keys()), textvariable=state["background"])
    background_cb.grid(row=2, column=1, sticky="ew", padx=10)

    
    # --- Size (fixed dropdown) ---
    ttk.Label(tab, text="Size:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    size_cb = ttk.Combobox(tab, values=["Small", "Medium", "Large"], textvariable=state["size"])
    size_cb.grid(row=3, column=1, sticky="ew", padx=10)


    # --- Function to apply bonuses ---
    def apply_bonuses_from_template(template_data):
        bonuses = template_data.get("bonuses", {})
        for attr, mod in bonuses.items():
            if attr in state["attributes"]:
                current = state["attributes"][attr].get()
                state["attributes"][attr].set(current + mod)

    def on_ancestry_selected(event=None):
        selected = ancestry_cb.get()
        if selected in ancestry_data:
            ancestry = ancestry_data[selected]
            apply_bonuses_from_template(ancestry)

        # Auto-fill size if provided in ancestry JSON
        ancestry_size = ancestry.get("size", "")
        if ancestry_size:
            state["size"].set(ancestry_size)


    def on_background_selected(event=None):
        selected = background_cb.get()
        if selected in background_data:
            apply_bonuses_from_template(background_data[selected])

    ancestry_cb.bind("<<ComboboxSelected>>", on_ancestry_selected)
    background_cb.bind("<<ComboboxSelected>>", on_background_selected)

    tab.columnconfigure(1, weight=1)
    return tab
