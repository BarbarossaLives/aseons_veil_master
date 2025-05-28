from dataclasses import dataclass
from typing import List

# clothing, gear, leisure, light, tools, gadgets,remedy, poison, 

@dataclass
class Gear:
    name: str = ""
    category: str = ""
    bulk: int = 0
    cost: int = 0


    def to_dict(self):
        return{
            "name": self.name,
            "category": self.category,
            "bulk": self.bulk,
            "cost": self.cost
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name = data.get("name",""),
            category = data.get("category", ""),
            bulk = data.get("bulk",0),
            cost = data.get("cost",0)
        )
