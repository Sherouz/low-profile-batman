# src/actions.py

import random

def apply_action(state, action):
    """
    Receives current state and a player action.
    Returns updated state.
    """

    if action == "scan":
        state = action_scan(state)

    elif action == "move":
        state = action_move(state)

    elif action == "hide":
        state = action_hide(state)

    elif action == "abort":
        state = action_abort(state)

    return state


def action_scan(state):
    """
    High progress, high risk
    """

    # progress should increase (medium to high)
    progress_gain = random.randint(10, 18)

    # risk should increase (high)
    risk_gain = random.randint(12, 22)

    state["progress"] += progress_gain
    state["risk"] += risk_gain

    return state


def action_move(state):
    """
    Medium progress, medium risk
    """

    # progress should increase (low to medium)
    progress_gain = random.randint(5, 10)

    # risk should increase (low to medium)
    risk_gain = random.randint(4, 9)

    state["progress"] += progress_gain
    state["risk"] += risk_gain

    return state


def action_hide(state):
    """
    Reduce risk with diminishing returns
    """

    streak = state["hide_streak"]

    if streak == 0:
        risk_reduction = random.randint(10, 15)
        
    elif streak == 1:
        risk_reduction = random.randint(5, 8)

    else:
        risk_reduction = random.randint(1, 3)

    state["risk"] -= risk_reduction

    return state


def action_abort(state):
    """
    Immediate exit action
    """

    # do not change progress
    # do not change risk
    # game loop will handle termination

    return state