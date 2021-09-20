from __future__ import annotations
import copy
from dataclasses import dataclass
from enum import Enum
import itertools
import operator
from typing import Dict, List, Set, Tuple


class Position(str, Enum):
    """Position that an athlete plays"""

    Quarterback: str = "Quarterback"
    Running_Back: str = "Running Back"
    Wide_Receiver: str = "Wide Receiver"


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


class Player(str, Enum):
    """One of the games players"""

    A: str = "Player A"
    B: str = "Player B"
    C: str = "Player C"


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


@dataclass
class GameState:
    """Specify the status of the game"""

    player_athletes: Dict[Player, Set[Athlete]]
    descendent_states: List[GameState]

    def take_turn(
        self, turn_order: List[Player], turn_index: int, athletes: List[Athlete]
    ) -> GameState:
        """Build out all possible descendent states"""
        player = turn_order[turn_index]
        for athlete in athletes:
            if athlete in itertools.chain.from_iterable(self.player_athletes.values()):
                continue
            if athlete.position in map(
                operator.attrgetter("position"), self.player_athletes[player]
            ):
                continue
            new_state = GameState(copy.deepcopy(self.player_athletes), [])
            new_state.player_athletes[player].add(athlete)
            self.descendent_states.append(new_state)
            if (new_turn_index := (turn_index + 1)) < len(turn_order):
                new_state.take_turn(turn_order, new_turn_index, athletes)

    def determine_winner(self) -> Tuple[Player, int]:
        """Determine who would win in the current game state"""
        if not self.descendent_states:
            totals = {}
            for player in Player:
                totals[player] = sum(
                    map(operator.attrgetter("value"), self.player_athletes[player])
                )
            return max(totals.items(), key=operator.itemgetter(1))
        else:
            results = []
            for state in self.descendent_states:
                results.append(state.determine_winner())
            return max(results, key=operator.itemgetter(1))


if __name__ == "__main__":
    player_athletes_empty = {
        Player.A: set(),
        Player.B: set(),
        Player.C: set(),
    }

    state = GameState(player_athletes_empty, [])
    state.take_turn(TURN_ORDER, 0, ATHLETES)
    winner = state.determine_winner()
    print(winner)
