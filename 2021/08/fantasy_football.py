from __future__ import annotations
import copy
from dataclasses import dataclass
from enum import Enum
import operator
from typing import Dict, List, Set, Tuple


class Position(Enum):
    """Position that an athlete plays"""

    Quarterback = 1
    Running_Back = 2
    Wide_Receiver = 3


@dataclass(eq=True, frozen=True)
class Athlete:
    """An athlete that can be chosen"""

    name: str
    value: int
    position: Position

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

class Player(Enum):
    """One of the games players"""

    A = 1
    B = 2
    C = 3

TURN_ORDER = [
    Player.A,
    Player.B,
    Player.C,
    Player.C,
    Player.B,
    Player.A,
    Player.A,
    Player.B,
    Player.C,
]

# @dataclass
# class PlayerAthletes:
    # """Athletes a player has chosen"""
# 
    # quarterback: Optional[Athlete]
    # running_back: Optional[Athlete]
    # wide_receiver: Optional[Athlete]



@dataclass
class GameState:
    """Specify the status of the game"""

    player_athletes: Dict[Player, Set[Athlete]]
    descendent_states: List[GameState]

    def take_turn(self, turn_index: int) -> GameState:
        """Build out all possible descendent states"""
        player = TURN_ORDER[turn_index]
        for athlete in ATHLETES:
            if athlete in self.player_athletes[player]:
                break
            new_state = copy.deepcopy(self) 
            new_state.player_athletes[player].quarterback = athlete
            self.descendent_states.add(new_state)
            if new_turn_index := turn_index + 1 < len(TURN_ORDER):
                new_state.take_turn(new_turn_index)

    def determine_winner(self) -> Tuple[Player, int]:
        """Determine who would win in the current game state"""
        if not self.descendent_states:
            totals = {}
            for player in Player:
                totals[player] = sum(map(operator.attrgetter('value'), self.player_athletes[player]))
            return max(totals.items(), key=operator.itemgetter(1))
        else:
            results = [] 
            for state in self.descendent_states:
                results.append(state.determine_winner())
            return max(results, key=operator.itemgetter(1)) 
