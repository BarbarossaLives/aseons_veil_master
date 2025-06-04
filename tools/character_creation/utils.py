import os, json

def load_item_names_and_data(folder_path):
    items = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            full_path = os.path.join(folder_path, filename)
            with open(full_path, "r") as f:
                try:
                    data = json.load(f)
                    name = data.get("name", filename.replace(".json", ""))
                    items[name] = data
                except json.JSONDecodeError:
                    print(f"⚠️ Error reading {filename}")
    return items
