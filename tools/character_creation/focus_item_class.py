from dataclasses import dataclass
from typing import List

@dataclass
class Focus_Item:
    name: str = "" 
    magic_school: str = ""
    cost: int = 0
    bonus: int = 0


    def to_dict(self):
        return{
            "name": self.name,
            "magic_school":self.magic_school,
            "cost": self.cost,
            "bonus": self.bonus
        }


    @classmethod
    def frm_dict(cls, data: dict):
        return cls(
            name=data.get("name",""),
            magic_school= data.get("magic_school", ""),
            cost = data.get("cost", 0),
            bonus = data.get("data", 0)
        )

