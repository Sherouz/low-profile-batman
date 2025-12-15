# src/result.py

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