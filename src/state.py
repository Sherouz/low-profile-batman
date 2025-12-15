# src/state.py - Game State and Rules

def init_state():
    """
    Creates and returns the initial game state.
    This is the single source of truth for the game.
    """
    state = {
        "progress": 0,      # 0 to 100
        "risk": 0,          # 0 to 100
        "turn": 1,          # starts at 1
        "max_turns": 15,    # fixed limit
        "hide_streak": 0    # consecutive hide counter
    }

    return state


def clamp_state(state):
    """
    Enforces the physical rules of the game.
    Called after ANY state change.
    """

    if state["progress"] > 100:
        state["progress"] = 100
    if state["progress"] < 0:
        state["progress"] = 0

    if state["risk"] < 0:
        state["risk"] = 0

    return state


def is_game_over(state):
    """
    Checks hard stop conditions.
    Does NOT print anything.
    """

    if state["risk"] >= 100:
        return True
    
    if state["turn"] > state["max_turns"]:
        return True
    
    if state["progress"] >= 100:
        return True
    
    return False