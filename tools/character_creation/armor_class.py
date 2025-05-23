from dataclasses import dataclass
from typing import List

@dataclass
class Armor:
    name: str = "",
    tags: List[str] = None,
    ac_bonus: int = 0,
    bulk: int = 0,
    qp: int = 0
    
    def to_dict(self):
        """Convert this armor piece to a plain dictionary"""
        return{
            "name": self.name,
            "tags": self.tags if self.tags else [],
            "ac_bonus": self.ac_bonus,
            "bulk": self.bulk,
            "qp": self.qp
            
        } 
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            tags=data.get("tags", []),
            ac_bonus=data.get("ac_bonus", 0),
            bulk=data.get("bulk", 0),
            qp=data.get("qp", 0)
        )  
    

