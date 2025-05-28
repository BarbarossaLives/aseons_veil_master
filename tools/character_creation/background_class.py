from dataclasses import dataclass
from typing import List

@dataclass
class Background:
    name: str
    description: str
    starting_skills: List[str]
    starting_gear: List[str]
    wealth_modifier: int

    def to_dict(self):
        # convert to dictionary
        return{
            "name": self.name,
            "description": self.description,
            "starting_skills": self.starting_skills if self.starting_skills else [],
            "starting_gear":self.starting_gear if self.starting_gear else [],
            "wealth_modifier": self.wealth_modifier

        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name",""),
            description=data.get("description",[]),
            starting_slkils=data.get("starting_skills", []),
            starting_gear=data.get("starting_gear", []),
            wealth_modifier=data.get("wealth_modifier", 0)
        )