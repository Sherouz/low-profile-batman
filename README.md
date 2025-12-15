# 🦇 Low-Profile Batman (Shadow Protocol)

## Overview

A minimal terminal-based game focused on **decision-making under risk**.
There are no graphics, no enemies to fight, and no safe choices.
Every action has consequences, and staying hidden matters.

This project was built as a **learning exercise** to practice clean game architecture, state management, and control flow in Python.

---

## Gameplay

You are handling a covert operation under time pressure.

Each turn, you choose one action:

* **Scan** → gain information faster, but increase risk significantly
* **Move** → steady progress with moderate risk
* **Hide** → reduce risk, but with strict limits
* **Abort** → exit the mission early and accept the outcome

The mission ends when:

* You complete the objective
* You get exposed
* You run out of time
* You abort

There is no perfect strategy.

---

## Design Goals

* Minimal and readable code
* Clear separation of responsibilities
* Decision-driven gameplay
* No overengineering
* Low-profile, terminal-only experience

---

## Project Structure

```
game.py
README.md
.gitignore
```

The project starts as a single file and is later refactored into modules to demonstrate clean architectural separation.

---

## How to Run

```bash
python game.py
```

Python 3.10+ recommended.

---

## Why This Project Exists

This is not meant to be a full game.
It is a **thinking exercise** disguised as a terminal game.

The goal is to practice:

* Managing state
* Designing systems that resist exploits
* Writing clean, understandable Python code

---

## License

Distributed under the [MIT License](LICENSE).