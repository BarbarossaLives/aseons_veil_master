import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def build_attributes_tab(notebook, state):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Attributes")

    # --- Layout Vars ---
    total_points = 10
    remaining_var = ttk.IntVar(value=total_points)

    # Save it to state for possible access elsewhere
    state["attribute_points_remaining"] = remaining_var

    # Shortcuts
    attributes = state["attributes"]
    calculated = state["calculated"]

    # --- Point Management ---
    def update_remaining():
        used = sum(var.get() for var in attributes.values())
        remaining_var.set(total_points - used)

    def update_calculated_stats():
        agi = attributes["Agility"].get()
        ins = attributes["Instinct"].get()
        mig = attributes["Might"].get()

        calculated["Health"].set(10 + mig * 2)
        calculated["Initiative"].set(agi + ins)
        calculated["Encumbrance Max"].set(mig * 4)

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

    # --- Attributes Grid ---
    row = 0
    for attr, var in attributes.items():
        ttk.Label(tab, text=f"{attr}:").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ttk.Button(tab, text="-", width=3, command=lambda a=attr: remove_point(a)).grid(row=row, column=1)
        ttk.Label(tab, textvariable=var).grid(row=row, column=2)
        ttk.Button(tab, text="+", width=3, command=lambda a=attr: add_point(a)).grid(row=row, column=3)
        row += 1

    # --- Remaining Points Display ---
    ttk.Label(tab, text="Remaining Points:").grid(row=row, column=0, columnspan=2, pady=10, sticky="e")
    ttk.Label(tab, textvariable=remaining_var, font=("Helvetica", 12, "bold")).grid(row=row, column=2, sticky="w")
    row += 1

    # --- Calculated Stats ---
    ttk.Separator(tab).grid(row=row, column=0, columnspan=4, pady=10, sticky="ew")
    row += 1

    for label, var in calculated.items():
        ttk.Label(tab, text=f"{label}:").grid(row=row, column=0, columnspan=2, sticky="e", padx=10)
        ttk.Label(tab, textvariable=var, font=("Helvetica", 10)).grid(row=row, column=2, sticky="w")
        row += 1

    # Final row config for spacing
    tab.columnconfigure(2, weight=1)

    # Initialize on load
    update_remaining()
    update_calculated_stats()

    return tab
