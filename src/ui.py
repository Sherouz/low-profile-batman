# src/ui.py

def get_risk_level(risk):
    """Maps numeric risk value to a qualitative threat level."""
    
    if risk < 35:
        return "LOW"
    
    elif risk < 70:
        return "MEDIUM"
    
    else:
        return "HIGH"


def display_state(state):
    """
    Displays the current game status.
    Does NOT modify state.
    """

    risk_level = get_risk_level(state["risk"])

    print(f"Turn: {state['turn']}")
    print(f"Progress: {state['progress']}%")
    print(f"Risk: {risk_level}")


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
