from dataclasses import dataclass
from typing import List
from typing import Dict

@dataclass
class Ancestry:
    name: str  # name of the race
    size: str  #size of the character 
    traits: List[str] 
    bonuses: Dict[str,int]
    description: str


    def to_dict(self):
        return{
            "name": self.name,
            "size": self.size,
            "traits": self.traits,
            "bonuses": self.bonuses,
            "description": self.description,
        }
    

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            size=data.get("size", ""),
            traits=data.get("traits", "" ),
            bonuses=data.get("bonuses", []),
            description= data.get("description", "")
        )