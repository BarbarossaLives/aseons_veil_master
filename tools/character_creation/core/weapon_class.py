from dataclasses import dataclass
from typing import List

@dataclass
class Weapon:
    name: str = ""
    tags: List[str] = None # e.g. ["melee","light","Thrown"
    damage: str = "" # e.g. "2d6", "1d10"
    bulk: int = 0 #used to track carrying wieght
    qp: int = 0 #Quality Points (item durability pr value)
    
    def to_dict(self):
        """Convert this wespon to a plain dictionary (for saving/export)"""
        return{
            "name": self.name,
            "tags": self.tags,
            "damage": self.damage,
            "bulk": self.bulk,
            "qp": self.qp
        }