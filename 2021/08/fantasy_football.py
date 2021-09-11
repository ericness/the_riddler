from dataclasses import dataclass
from enum import Enum
from __future__ import annotations
from typing import Optional, Set

class Position(Enum):
    """Position that an athlete plays"""
    Quarterback = 1
    Running_Back = 2
    Wide_Receiver = 3

@dataclass
class Athlete:
    """An athlete that can be chosen"""
    name: str
    value: float
    position: Position

@dataclass
class PlayerAthletes:
    """Athletes a player has chosen"""
    quarterback: Optional[Athlete]
    running_back: Optional[Athlete]
    wide_receiver: Optional[Athlete]

@dataclass
class GameState:
    """Specify the status of the game"""
    player_a_athletes: PlayerAthletes
    player_b_athletes: PlayerAthletes
    player_c_athletes: PlayerAthletes
    descendent_states: Set[GameState]
    winner: str

ATHLETES = [
    Athlete("Matrick Pahomes", 400, Position.Quarterback),
    Athlete("Osh Jallen", 350, Position.Quarterback),
    Athlete("Myler Kurray", 300, Position.Quarterback),
    Athlete("Caffrey McChristian", 300, Position.Running_Back),
    Athlete("Calvin Dook", 225, Position.Running_Back),
    Athlete("Herrick Denry", 200, Position.Running_Back),
    Athlete("Avante Dadams", 250, Position.Wide_Receiver),
    Athlete("Hyreek Till", 225, Position.Wide_Receiver),
    Athlete("Defon Stiggs", 175, Position.Wide_Receiver),
]

