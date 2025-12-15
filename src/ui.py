# src/ui.py

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