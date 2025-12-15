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
