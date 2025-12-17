# src/result.py

def show_result(state, last_action):
    """
    Displays the final outcome of the game.
    """

    print("\n-------- Mission Report --------\n")

    if last_action == "abort":
        print("Status:")
        if state["progress"] >= 60:
            print("  Aborted with extracted intel")
            print("\nOutcome:\n  Partial Success")
        else:
            print("  Aborted too early")
            print("\nOutcome:\n  Failure")

    elif state["risk"] >= 100:
        print("Status:\n  Exposed")
        print("\nOutcome:\n  Mission Failed")

    elif state["progress"] >= 100:
        print("Status:\n  Objective completed")
        print("\nOutcome:\n  Success")

    else:
        print("Status:\n  Time expired")
        print("\nOutcome:\n  Mission Failed")

    print("\nSummary:")
    print(f"  Progress: {state['progress']}%")
    print(f"  Risk: {state['risk']}%")
    print(f"  Turns Used: {state['turn'] - 1}")
