from dataclasses import dataclass
from typing import List

@dataclass
class Feat:
    name: str = ""# name of the feat
    category: str = "" # e.g., "Athletics", "Lore", "Combat"
    fp_cost: int = 0 # FP required to activate (0 if permanent)
    usage: str = ""  # "Permanent", "1 FP", "3 FP", "Special", etc.
    effect: str = ""  # Short description of what it does
    pip: int = ""
    
    def to_dict(self): # export to dictionary
        return{
            "name": self.name,
            "catagory": self.category,
            "fp_cost": self.fp_cost,
            "usage": self.usage,
            "effect": self.effect,
            "pip" : self.pip
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            catagory=data.get("category", ""),
            fp_cost=data.get("fp_cost", 0),
            usage=data.get("usage", ""),
            effect=data.get("effect", ""),
            pip=data.get("description", "")
        )

    
    
    
    
