import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from feat_class import Feat

#Helper Function
def parse_list_input(text: str) -> list:
    return [item.strip() for item in text.split(",") if item.strip()]

# set paths
BASE_DIR = os.path.dirname(__file__)
FEAT_FOLDER = os.path.join(BASE_DIR,"data","feat")
os.markedirs(FEAT_FOLDER, exist_ok=True)

#save function

def save_feat():
    name = name_entry.get()
    tags = parse_list_input(tags_entry.get())
    description = description_entry.get()
    catagory = catagory_entry.get()
    fp_cost = fp_cost_entry.get()
    usage = usage_entry.get()
    effect = effect_entry.get()
    requirements = requirements_entry.get()

    if not name:
        messagebox.showerror("Missing Name", "Please enter a name for the armor.")
        return
    
    feat = Feat(
        name=name,
        tags=tags,
        description=description,
        catagory=catagory,
        fp_cost=fp_cost,
        usage=usage,
        effect=effect,
        requirements=requirements
    )

    filename= f"{name.lower().replace(' ','_')}.json"
    path= os.path.join(FEAT_FOLDER, filename)

    with open(path, "w") as f:
        json.dump(feat.to_dict(), f, indent=2)

    messagebox.showinfo("Saved", f"{feat.name} saved to {filename}")


    #clear fields for the next entry
    for entry in (name_entry,tags_entry,catagory_entry,description_entry,fp_cost_entry,usage_entry,effect_entry,requirements_entry):
        entry.delete(0,"end")

    name_entry.focus()


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

ttk.Label(app, text="Tags", style = "info.TLabel").pack()
tags_entry = ttk.Entry(app)
tags_entry.pack(pady=5)

ttk.Label(app, text="Catagory", style = "info.TLabel").pack()
catagory_entry = ttk.Entry(app)
catagory_entry.pack(pady=5)

ttk.Label(app, text="FP Cost", style = "info.TLabel").pack()
fp_cost_entry = ttk.Entry(app)
fp_cost_entry.pack(pady=5)

ttk.Label(app, text="Usage", style = "info.TLabel").pack()
usage_entry = ttk.Entry(app)
usage_entry.pack(pady=5)

ttk.Label(app, text="Effect", style = "info.TLabel").pack()
effect_entry = ttk.Entry(app)
effect_entry.pack(pady=5)

ttk.Label(app, text="Requirements", style = "info.TLabel").pack()
requirements_entry = ttk.Entry(app)
requirements_entry.pack(pady=5)

ttk.Label(app, text="Description", style = "info.TLabel").pack()
description_entry = ttk.Entry(app)
description_entry.pack(pady=5)
