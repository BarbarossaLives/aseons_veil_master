from dataclasses import dataclass
from typing import List

@dataclass
class character:
    name: str = ""
    ancestry: str = ""
    size: str = ""
    background: str = ""
    
    #core Attributes
    agility: int = 0
    instinct: int = 0
    might: int = 0
    wit: int = 0
    
    hp: int = 0 #Hit Points = Might + 10
    fo: int = 0 #Focus Points - wt + 5
    ac: int = 0 #Armor Class = Aglity  (or overridden by armor)
    cc: int = 0 #Carrying Capacity = Might + 10
    
    #skills 
    skills: dict[str,int] = field(default_factory=lambda: {
        "Athletics": 0, "Awareness": 0, "Craft": 0, "Expression": 0, "Influence": 0, "Lore": 0, "Medicine": 0, "Nature": 0,
        "Stealth": 0, "Melee": 0, "Missle": 0,
        "Arcane": 0, "Divine": 0, "Kinetic": 0, "Primal": 0, "Psonic": 0
    })
    
    # Equipment and Features
    weapons: List = field(default_factory=list)
    armor: List = field(default_factory=list)
    feats: List = field(default_factory=list)
    spells: List = field(default_factory=list)
    gear: List = field(default_factory=list)
    tech: List = field(default_factory=list)
    
    def calculate_derived_stats(self):
        """Set HPO, FP, and Crrying Capacity based ib attributers"""
        self.hp = self.might + 10
        self.fp = self.wit + 5
        self.cc = self.night + 10
        # Ac willbe set manually or vased on equiped armor
        
    def to_dict(self):
        """Cnvert ths character to a plain dictionary fr JSON export"""
        return{
            "name": self.name,
            "ancestry": self.ancestry,
            "size": self.size,
            "background":self.background,
            "attributes":{
                "agility": self.agility,
                "instinct": self.instinct,
                "might": self.might,
                "wit": self.wit
            },
        "derived":{
            "hp": self.hp,
            "fp": self.fp,
            "ac": self.ac,
            "cc": self.cc
        },
        "skills": self.skills,
        "weapons": self.weapons,
        "armor": self.armor,
        "feats": self.feats,
        "spells": self.spells,
        "gear": self.gear,
        "tech": self.tech
    }