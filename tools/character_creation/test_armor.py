from armor_class import Armor
import json

#Create an armor object
chainmail = Armor(
    name = "Chainmail",
    tags = ["Heavy"],
    ac_bonus = 4,
    bulk = 3,
    qp = 2
)

# Prnt object
print("Object:", chainmail)

# print the object
armor_dict = chainmail.to_dict()
print("nAs dictionary:", armor_dict)

#Sve to Json
with open("chainmail.json", "w") as f:
    json.dump(armor_dict, f, indent=2)
    print("/nSaved to chainmal.json")