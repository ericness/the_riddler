import pprint

from fantasy_football import ATHLETES, Player, GameState

TURN_ORDER = [
    Player.A,
    Player.B,
    Player.C,
]

TEST_ATHLETES = ATHLETES[:3]

FINAL_STATE_1 = GameState({Player.A: {ATHLETES[0]}, Player.B: {ATHLETES[1]}, Player.C: {ATHLETES[2]}}, [])
FINAL_STATE_2 = GameState({Player.A: {ATHLETES[0]}, Player.B: {ATHLETES[2]}, Player.C: {ATHLETES[1]}}, [])
FINAL_STATE_3 = GameState({Player.A: {ATHLETES[1]}, Player.B: {ATHLETES[0]}, Player.C: {ATHLETES[2]}}, [])
FINAL_STATE_4 = GameState({Player.A: {ATHLETES[1]}, Player.B: {ATHLETES[2]}, Player.C: {ATHLETES[0]}}, [])
FINAL_STATE_5 = GameState({Player.A: {ATHLETES[2]}, Player.B: {ATHLETES[0]}, Player.C: {ATHLETES[1]}}, [])
FINAL_STATE_6 = GameState({Player.A: {ATHLETES[2]}, Player.B: {ATHLETES[1]}, Player.C: {ATHLETES[0]}}, [])

MIDDLE_STATE_1 = GameState({Player.A: {ATHLETES[0]}, Player.B: {ATHLETES[1]}, Player.C: set()}, [FINAL_STATE_1])
MIDDLE_STATE_2 = GameState({Player.A: {ATHLETES[0]}, Player.B: {ATHLETES[2]}, Player.C: set()}, [FINAL_STATE_2])
MIDDLE_STATE_3 = GameState({Player.A: {ATHLETES[1]}, Player.B: {ATHLETES[0]}, Player.C: set()}, [FINAL_STATE_3])
MIDDLE_STATE_4 = GameState({Player.A: {ATHLETES[1]}, Player.B: {ATHLETES[2]}, Player.C: set()}, [FINAL_STATE_4])
MIDDLE_STATE_5 = GameState({Player.A: {ATHLETES[2]}, Player.B: {ATHLETES[0]}, Player.C: set()}, [FINAL_STATE_5])
MIDDLE_STATE_6 = GameState({Player.A: {ATHLETES[2]}, Player.B: {ATHLETES[1]}, Player.C: set()}, [FINAL_STATE_6])

INITIAL_STATE_1 = GameState({Player.A: {ATHLETES[0]}, Player.B: set(), Player.C: set()}, [MIDDLE_STATE_1, MIDDLE_STATE_2])
INITIAL_STATE_2 = GameState({Player.A: {ATHLETES[1]}, Player.B: set(), Player.C: set()}, [MIDDLE_STATE_3, MIDDLE_STATE_4])
INITIAL_STATE_3 = GameState({Player.A: {ATHLETES[2]}, Player.B: set(), Player.C: set()}, [MIDDLE_STATE_5, MIDDLE_STATE_6])

PLAYER_ATHLETES_EMPTY = {
    Player.A: set(),
    Player.B: set(),
    Player.C: set(),
}

EXPECTED_STATE = GameState(
    PLAYER_ATHLETES_EMPTY,
    [INITIAL_STATE_1, INITIAL_STATE_2, INITIAL_STATE_3]
)

PLAYER_ATHLETES_A_MAX = {
    Player.A: {
        ATHLETES[0],
        ATHLETES[3],
        ATHLETES[6],
    },
    Player.B: {
        ATHLETES[1],
        ATHLETES[4],
        ATHLETES[7],
    },
    Player.C: {
        ATHLETES[2],
        ATHLETES[5],
        ATHLETES[8],
    },
}

PLAYER_ATHLETES_B_MAX = {
    Player.A: {
        ATHLETES[2],
        ATHLETES[4],
        ATHLETES[7],
    },
    Player.B: {
        ATHLETES[1],
        ATHLETES[3],
        ATHLETES[6],
    },
    Player.C: {
        ATHLETES[0],
        ATHLETES[5],
        ATHLETES[8],
    },
}


def test_take_turn():
    """Should create game state tree"""
    state = GameState(PLAYER_ATHLETES_EMPTY, [])
    state.take_turn(TURN_ORDER, 0, TEST_ATHLETES)
    assert state == EXPECTED_STATE


def test_determine_winner_empty():
    """Should calculate totals for players and return max"""
    state = GameState(PLAYER_ATHLETES_A_MAX, [])
    result = state.determine_winner()
    assert result == (Player.A, 950)


def test_determine_winner_non_empty():
    """Should calculate totals for players and return max"""
    state_a = GameState(PLAYER_ATHLETES_A_MAX, [])
    state_b = GameState(PLAYER_ATHLETES_B_MAX, [])
    parent_state = GameState({}, [state_a, state_b])
    result = parent_state.determine_winner()
    assert result == (Player.A, 950)
