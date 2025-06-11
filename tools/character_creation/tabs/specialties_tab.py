import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils import load_item_names_and_data

WEAPON_CATEGORIES = [
    "One-Handed Blade", "One-Handed Blunt",
    "Two-Handed Blade", "Two-Handed Blunt",
    "Ranged", "Thrown", "Polearms"
]

MAGIC_SCHOOLS = ["Arcane", "Primal", "Divine", "Psionic", "Kinetic"]

# Mock spell data if JSON not yet available
SPELL_DATA = {
    "Arcane": ["Arcane Spell 1", "Arcane Spell 2", "Arcane Spell 3"],
    "Primal": ["Primal Spell 1", "Primal Spell 2", "Primal Spell 3"],
    "Divine": ["Divine Spell 1", "Divine Spell 2", "Divine Spell 3"],
    "Psionic": ["Psionic Spell 1", "Psionic Spell 2", "Psionic Spell 3"],
    "Kinetic": ["Kinetic Spell 1", "Kinetic Spell 2", "Kinetic Spell 3"]
}

def build_specialties_tab(notebook, state):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Specialties")

    state["specialties"] = {"weapons": [], "spells": {school: [] for school in MAGIC_SCHOOLS}}

    section = ttk.Frame(tab)
    section.pack(fill="both", expand=True, padx=10, pady=10)

    # --- Weapon Specialties from Combat Pips ---
    combat_pips = sum(1 for s in state["skills"] if s.lower() == "combat" for _ in range(state["skills"][s].get()))
    used_weapon_choices = set()

    ttk.Label(section, text="Weapon Specialties", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(0, 5))
    for i in range(combat_pips):
        var = ttk.StringVar()
        combo = ttk.Combobox(section, textvariable=var, values=WEAPON_CATEGORIES, state="readonly")
        combo.pack(fill="x", pady=2)
        state["specialties"]["weapons"].append(var)

    # --- Spell Specialties from Magic School Pips ---
    for school in MAGIC_SCHOOLS:
        pips = sum(1 for s in state["skills"] if school.lower() in s.lower() for _ in range(state["skills"][s].get()))
        if pips == 0:
            continue

        ttk.Label(section, text=f"{school} Spells", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(10, 5))
        for i in range(pips):
            var = ttk.StringVar()
            spell_list = SPELL_DATA.get(school, [])
            combo = ttk.Combobox(section, textvariable=var, values=spell_list, state="readonly")
            combo.pack(fill="x", pady=2)
            state["specialties"]["spells"][school].append(var)

    return tab
