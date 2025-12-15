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
    Reduce risk, no progress
    """

    # risk should decrease
    risk_reduction = random.randint(8, 15)

    # progress stays the same
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


def display_state(state):
    """
    Displays the current game status.
    Does NOT modify state.
    """

    print(f"current turn: {state['turn']}")
    print(f"progress value: {state['progress']}")
    print(f"risk value: {state['risk']}")


def get_player_action():
    """
    Asks the player for an action.
    Returns a valid action string.
    """

    while True:

        print("""
Choose an action:
[s] Scan
[m] Move
[h] Hide
[a] Abort
""")

        choice = input("Select your choice: ").strip().lower()

        if choice in ("scan", "s"):
            return "scan"

        elif choice in ("move", "m"):
            return "move"

        elif choice in ("hide", "h"):
            return "hide"

        elif choice in ("abort", "a"):
            return "abort"

        else:
            print("Invalid choice. Try again.")


def run_game():
    """
    Main game loop.
    """

    state = init_state()
    last_action = None

    print("\n===== Shadow Protocol Initiated =====")
    print("Stay unseen. One wrong move ends the mission.")

    while not is_game_over(state):

        print("\n------------------------------")
        display_state(state)

        action = get_player_action()
        last_action = action

        if action == "abort":
            break

        # Anti-hide-spam logic
        if action == "hide":
            if state["hide_streak"] >= 2:
                print("You can't stay hidden forever.")
                # hide blocked, turn still passes
                state["turn"] += 1
                continue
            else:
                state["hide_streak"] += 1
        else:
            # reset streak if action is not hide
            state["hide_streak"] = 0

        state = apply_action(state, action)
        state = clamp_state(state)

        state["turn"] += 1

    show_result(state, last_action)


def show_result(state, last_action):
    """
    Displays the final outcome of the game.
    """

    print("\n--- Mission Report ---")

    if last_action == "abort":
        if state["progress"] >= 60:
            print("You aborted the mission, but extracted valuable intel.")
            print("Outcome: Partial Success")
        else:
            print("You aborted too early.")
            print("Outcome: Failure")

    elif state["risk"] >= 100:
        print("You were exposed.")
        print("Outcome: Mission Failed")

    elif state["progress"] >= 100:
        print("Mission completed successfully.")
        print("Outcome: Success")

    else:
        print("Time ran out before completing the mission.")
        print("Outcome: Mission Failed")

    print(f"Final Progress: {state['progress']}")
    print(f"Final Risk: {state['risk']}")
    print(f"Turns Used: {state['turn'] - 1}")


if __name__ == '__main__':
    run_game()
