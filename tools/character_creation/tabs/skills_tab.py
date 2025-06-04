import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils import load_item_names_and_data


def build_skills_tab(notebook, state):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Skills")

    # Load skill list from data
    skills_path = os.path.join(os.path.dirname(__file__), "..", "data", "skills")
    skill_data = load_item_names_and_data(skills_path)

    # Create storage for skill IntVars
    state["skills"] = {}
    skill_frame = ttk.Frame(tab)
    skill_frame.pack(fill="both", expand=True, padx=10, pady=10)

    skill_points_total = 4
    state["skill_points_remaining"] = ttk.IntVar(value=skill_points_total)

    def update_remaining_points():
        spent = sum(var.get() for var in state["skills"].values())
        state["skill_points_remaining"].set(skill_points_total - spent)

    def add_point(skill):
        if state["skill_points_remaining"].get() > 0:
            var = state["skills"][skill]
            var.set(var.get() + 1)
            update_remaining_points()

    def remove_point(skill):
        var = state["skills"][skill]
        if var.get() > 0:
            var.set(var.get() - 1)
            update_remaining_points()

    # Populate skills
    for row, (skill, details) in enumerate(skill_data.items()):
        state["skills"][skill] = ttk.IntVar(value=0)

        ttk.Label(skill_frame, text=skill).grid(row=row, column=0, sticky="w", padx=5)
        ttk.Button(skill_frame, text="-", width=3, command=lambda s=skill: remove_point(s)).grid(row=row, column=1)
        ttk.Label(skill_frame, textvariable=state["skills"][skill]).grid(row=row, column=2)
        ttk.Button(skill_frame, text="+", width=3, command=lambda s=skill: add_point(s)).grid(row=row, column=3)

    # Display remaining points
    footer = ttk.Frame(tab)
    footer.pack(pady=10)
    ttk.Label(footer, text="Remaining Skill Points: ").pack(side="left")
    ttk.Label(footer, textvariable=state["skill_points_remaining"], font=("Helvetica", 10, "bold")).pack(side="left")

    update_remaining_points()
    return tab
