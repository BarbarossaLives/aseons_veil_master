from dataclasses import dataclass
from typing import List

@dataclass
class Weapon:
    name: str = ""
    tags: List[str] = None # e.g. ["melee","light","Thrown"
    damage: str = "" # e.g. "2d6", "1d10"
    bulk: int = 0 #used to track carrying wieght
    qp: int = 0 #Quality Points (item durability pr value)
    cost: int = 0
    description: str = ""
    
    def to_dict(self):
        """Convert this wespon to a plain dictionary (for saving/export)"""
        return{
            "name": self.name,
            "tags": self.tags,
            "damage": self.damage,
            "bulk": self.bulk,
            "qp": self.qp,
            "cosst":self.cost,
            "description":self.cost
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        """Create a Weapon from a dictionary (like one loaded from JSON)."""
        return cls(
            name=data.get("name", ""),
            tags=data.get("tags", []),
            damage=data.get("damage", ""),
            bulk=data.get("bulk", 0),
            qp=data.get("qp", 0),
            cost=data.get("cost",0),
            description=data.get("description", "")
        )