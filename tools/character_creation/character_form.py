import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Create the main app window
app = ttk.Window(
    title="Embark Character Builder",
    themename="darkly",  # You can try "solar", "cyborg", "flatly", etc.
    size=(600, 500),
    resizable=(False, False)
)

# Header Label
ttk.Label(app, text="Create New Character", font=("Arial", 20)).pack(pady=20)

# Name input
name_label = ttk.Label(app, text="Name:")
name_label.pack()
name_entry = ttk.Entry(app)
name_entry.pack(pady=5)

# Ancestry input
ancestry_label = ttk.Label(app, text="Ancestry:")
ancestry_label.pack()
ancestry_entry = ttk.Entry(app)
ancestry_entry.pack(pady=5)

# Size input
size_label = ttk.Label(app, text="Size:")
size_label.pack()
size_entry = ttk.Entry(app)
size_entry.pack(pady=5)

# Background input
background_label = ttk.Label(app, text="Background:")
background_label.pack()
background_entry = ttk.Entry(app)
background_entry.pack(pady=5)

# Launch the GUI
app.mainloop()
