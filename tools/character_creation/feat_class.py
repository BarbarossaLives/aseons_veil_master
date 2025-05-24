from dataclasses import dataclass
from typing import List

@dataclass
class Feat:
    name: str = ""# name of the feat
    tags: List[str] = None  # identifing tags
    category: str = "" # e.g., "Athletics", "Lore", "Combat"
    fp_cost: int = 0 # FP required to activate (0 if permanent)
    usage: str = ""  # "Permanent", "1 FP", "3 FP", "Special", etc.
    effect: str = ""  # Short description of what it does
    requirements: str = "" # XP or skill pip requirements (optional)
    
    def to_dict(self): # export to dictionary
        return{
            "name": self.name,
            "tags": self.tags,
            "catagory": self.catagory,
            "fp_cost": self.rp_cost,
            "usage": self.usage,
            "effect": self.effects,
            "requirements": self.requirements
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            tags=data.get("tags", [])
            category=data.get("category", ""),
            fp_cost=data.get("fp_cost", 0),
            usage=data.get("usage", ""),
            effect=data.get("effect", ""),
            requirements=data.get("requirements", "")
        )

    
    
    
    
