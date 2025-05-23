from dataclasses import dataclass
from typing import List

@dataclass
class Spell:
    name: str = "", # Name of the spell
    tags: List[str] = None, # e.g., ["Arcane", "Primal", "Fire"]
    fp_cost:int  = 0, # Focus Points required to cast 
    power: int = "", # Spell power level, e.g. "1d6", "2d4+2"
    area:int = "", # Area of Effect (e.g. "nearby", "1d4 targets")
    duration:int = "", # How long it lasts (e.g. "1d4 rounds", "permanent")
    range: str = ""  # e.g. "touch", "nearby", "faraway"
    concentration: bool = False  # Does it require concentration?
    description: str = "" # Full description or rules text
    
    def to_dict(self):
        # convert to plain dictionary
        return{
            "name": self.name,
            "tags": self.tags if self.tags else [],
            "fp_cost": self.fp_cost,
            "power": self.power,
            "area": self.area,
            "duration":self.duration,
            "range": self.range,
            "concentration": self.concentration,
            "description": self.description
        
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            tags=data.get("tags", []),
            fp_cost=data.get("fp_cost", 0),
            power=data.get("power", ""),
            area=data.get("area", ""),
            duration=data.get("duration", ""),
            range=data.get("range", ""),
            concentration=data.get("concentration", False),
            description=data.get("description", "")
        )

    
    

