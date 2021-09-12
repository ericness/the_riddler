from fantasy_football import ATHLETES, Player, GameState


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


def test_determine_winner_empty():
    """Should calculate totals for players and return max"""
    state = GameState(PLAYER_ATHLETES_A_MAX, set())
    result = state.determine_winner()
    assert result == (Player.A, 950)


def test_determine_winner_non_empty():
    """Should calculate totals for players and return max"""
    state_a = GameState(PLAYER_ATHLETES_A_MAX, set())
    state_b = GameState(PLAYER_ATHLETES_B_MAX, set())
    parent_state = GameState({}, [state_a, state_b])
    result = parent_state.determine_winner()
    assert result == (Player.A, 950)
