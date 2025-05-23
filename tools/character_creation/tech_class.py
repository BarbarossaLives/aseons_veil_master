from dataclasses import dataclass
from typing import List

class Tech:
    name: str = ""  # name of the items
    type: str = ""   # e.g., "Weapon", "Tool", "Implant", "Interface"
    tags: List[str] = None   # e.g., "Weapon", "Tool", "Implant", "Interface"
    activation: str = ""  # how des it activate or work
    power_source: str = ""  ## e.g., "Internal battery", "External crystal"
    bulk: str = "" # e.g., "Internal battery", "External crystal"
    qp: int = 0  #  Quality Points (tech integrity or charge level)
    description: str = ""  # Optional long-form description or lore
    
    def to_dict(self): # exoirt to dictionary
        return{
            "name": self.name,
            "type": self.type,
            "tags": self.tags,
            "activation": self.activation,
            "power_source": self.power_source,
            "bulk": self.bulk,
            "qp": self.qp,
            "description":self.description         
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            type=data.get("type", ""),
            tags=data.get("tags", []),
            activation=data.get("activation", ""),
            power_source=data.get("power_source", ""),
            bulk=data.get("bulk", 0),
            qp=data.get("qp", 0),
            description=data.get("description", "")
        )

    
    
    

