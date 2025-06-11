from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Skill:
    name: str = ""
    type: List[str] = field(default_factory=lambda: ["Adventure", "Magic", "Combat"])
    pips: List[str] = field(default_factory=lambda: ["Proficient", "Adept", "Expert", "Legend"])
    roll: Optional[List[str]] = field(default_factory=list)

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "pips": self.pips,
            "roll": self.roll
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            type=data.get("type", []),
            pips=data.get("pips", []),
            roll=data.get("roll", [])
        )



