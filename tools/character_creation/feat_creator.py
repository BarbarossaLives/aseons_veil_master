import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os, json
from feat_class import Feat

#Helper Function
def parse_list_input(text: str) -> list:
    return [item.strip() for item in text.split(",") if item.strip()]

# set paths
BASE_DIR = os.path.dirname(__file__)
FEAT_FOLDER = os.path.join(BASE_DIR,"data","feat")
os.makedirs(FEAT_FOLDER, exist_ok=True)

#save function

def save_feat():
    name = name_entry.get()
    category = category_entry.get()
    fp_cost = fp_cost_entry.get()
    usage = usage_entry.get()
    effect = effect_entry.get()
    pip = pip_entry.get()

    if not name:
        messagebox.showerror("Missing Name", "Please enter a name for the armor.")
        return
    
    feat = Feat(
        name=name,
        category=category,
        fp_cost=fp_cost,
        usage=usage,
        effect=effect,
        pip=pip
    )

    filename= f"{name.lower().replace(' ','_')}.json"
    path= os.path.join(FEAT_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(feat.to_dict(), f, indent=2)

    messagebox.showinfo("Saved", f"{feat.name} saved to {filename}")


    #clear fields for the next entry
    for entry in (name_entry,category_entry,fp_cost_entry,usage_entry,effect_entry,pip_entry):
        entry.delete(0,"end")

    name_entry.focus


# create window
app =ttk.Window(title="Feat Creator", themename="darkly", size=(600,850))

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

ttk.Label(app, text="Name", style = "info.TLabel").pack()
name_entry = ttk.Entry(app)
name_entry.pack(pady=5)


ttk.Label(app, text="Category", style = "info.TLabel").pack()
category_entry = ttk.Entry(app)
category_entry.pack(pady=5)

ttk.Label(app, text="FP Cost", style = "info.TLabel").pack()
fp_cost_entry = ttk.Entry(app)
fp_cost_entry.pack(pady=5)

ttk.Label(app, text="Usage", style = "info.TLabel").pack()
usage_entry = ttk.Entry(app)
usage_entry.pack(pady=5)

ttk.Label(app, text="Effect", style = "info.TLabel").pack()
effect_entry = ttk.Entry(app)
effect_entry.pack(pady=5)


ttk.Label(app, text="Pip", style = "info.TLabel").pack()
pip_entry = ttk.Entry(app)
pip_entry.pack(pady=5)

# Save Button
ttk.Button(app, text="Save Feat", command=save_feat, style="success").pack(pady=15)

app.mainloop()