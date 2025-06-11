from dataclasses import dataclass
from typing import List

@dataclass
class Spell:
    name: str = "" # Name of the spell
    school: str = ""
    defense: str = ""
    difficulty: int = 0
    description: str = "" # Full description or rules text
    
    def to_dict(self):
        # convert to plain dictionary
        return{
            "name": self.name,
            "school": self.school,
            "defense": self.defense,
            "difficulty": self.difficulty,
            "description": self.description
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            schools=data.get("school", ""),
            defense=data.get("defese", ""),
            difficulty=data.get("difficulty",0),
            description=data.get("description", "")
        )

    
    

