# main.py

from src.state import init_state, clamp_state, is_game_over
from src.actions import apply_action
from src.ui import display_state, get_player_action
from src.result import show_result

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


if __name__ == '__main__':
    run_game()
