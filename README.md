# 🦇 Low-Profile Batman (Shadow Protocol)

A minimal terminal-based game focused on **decision-making under risk**.

No graphics.  
No enemies.  
No safe choices.

Every action has consequences, and staying hidden is never guaranteed.

This project was built as a **learning exercise** to practice clean architecture,
state-driven design, and decision-focused gameplay in Python.

---

## 🎮 Gameplay

You are running a covert operation under strict time pressure.

Each turn, you must choose one action:

- **Scan**  
  High progress, high risk. Fast but dangerous.

- **Move**  
  Steady progress with moderate risk.

- **Hide**  
  Reduces risk, but with diminishing returns and strict limits.

- **Abort**  
  Exit the mission early and accept the consequences.

The mission ends when:

- The objective is completed
- You get exposed
- You run out of time
- You abort the mission

There is no perfect strategy.

---

## ⚙️ Core Mechanics

- **Risk is partially hidden**  
  You see qualitative levels (LOW / MEDIUM / HIGH), not exact values.

- **High-risk exposure**  
  At high risk levels, each turn carries a chance of immediate exposure.

- **Anti-spam protection**  
  Repeated hiding becomes ineffective and is actively restricted.

- **Decision-driven flow**  
  The game punishes greedy or overly defensive play.

---

## 🧠 Design Goals

- Minimal and readable code
- Clear separation of responsibilities
- State-driven logic
- No overengineering
- Terminal-only, low-profile experience

This is a system-design exercise disguised as a game.

---

## 📁 Project Structure

```

low-profile-batman/
│
├── main.py          # Entry point and main game loop
├── README.md
├── LICENSE
│
└── src/
├── state.py     # Game state and rules
├── actions.py   # Action logic and state mutation
├── ui.py        # Terminal input/output
├── result.py    # Final outcome handling
└── **init**.py

````

The project starts as a single-file prototype and is later refactored into modules
to demonstrate clean architectural separation.

---

## ▶️ How to Run

From the project root:

```bash
python main.py
````

Python **3.10+** recommended.

---

## 🧪 Why This Project Exists

This is not meant to be a full game.

It exists to practice:

* Managing mutable state
* Designing systems that resist exploits
* Separating logic, presentation, and control flow
* Writing clean, understandable Python code

If you are learning Python or system design, this project is meant to be read,
modified, and experimented with.

---

## 📄 License

Distributed under the [MIT License](LICENSE).

---

*Last updated: Dec 2025*