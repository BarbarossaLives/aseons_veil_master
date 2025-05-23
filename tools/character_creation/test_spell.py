from spell_class import Spell
import json

# sample spell
fire_bolt = Spell(
    name = "Fire Bolt",
    tags = ["Arcane", "Fire"],
    fp_cost = 2,
    power = "2d6",
    area = "single target",
    duration = "instant",
    range = "nearby",
    concentration = False,
    description = "A searing bolt of fire strikes a target, Deals fire damge",
           
)
# print the bject
print("Object:", fire_bolt)

# Coonvert to dectionary
print("\nAs dictionary:", fire_bolt.to_dict)

# Save to JSON file
with open("fire_bolt.json", "w") as f:
    json.dump(fire_bolt.to_dict(), f, indent=2)
    print("\nSaved to fire_bolt.json")
