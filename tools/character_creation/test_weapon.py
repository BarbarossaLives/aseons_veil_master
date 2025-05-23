from weapon_class import Weapon
import json

shortsword = Weapon(
    name="Shortsword",
    tags=["Melee", "Light"],
    damage="1d6",
    bulk=1,
    qp=1
)


# Print in out (tgus shows __repr__ from @dataclass)
print("Object:", shortsword)

# convert to a dectionary
weapon_dict = shortsword.to_dict()
print(".nas dictionary:", weapon_dict)

# Save to a json file
with open("shortsword.json", "w") as f:
    json.dump(weapon_dict, f, indent=2)
    print("\nSaved to shortsword,json")