from dataclasses import dataclass
from typing import List

@dataclass
class Potion:
    name: str = ""
    category: str = ""  # potion, pioson, remedy
    cost: int = 0
    effect: str = ""


    def t0_dict(self):
        return{
            "name": self.name,
            "category": self.category,
            "cost": self.cost,
            "effect": self.effect
        }
    

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name = data.get("name", ""),
            category = data.get("category", ""),
            cost = data.get("cost", 0),
            effect = data.get("effect", "")
        )