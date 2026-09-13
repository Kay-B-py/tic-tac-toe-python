# Tic-Tac-Toe (Python)

**Kurzfassung (Deutsch):** Ein konsolenbasiertes Tic-Tac-Toe-Spiel in Python – Mensch (O) gegen Computer (X). Das Grundgerüst stammt aus dem Cisco Networking Academy Kurs "Python Essentials 1" (Abschlussprojekt), der Computer-Gegner wurde von mir eigenständig erweitert: Statt rein zufällig zu ziehen, prüft er zuerst, ob er selbst gewinnen kann, dann ob er den Spieler blockieren muss, und zieht erst danach zufällig. Details dazu im Abschnitt "Beyond the Course Task" weiter unten.

---

*(Full documentation in English below)*

## How to Play

- The computer always opens with the first move in the center of the board.
- Fields are numbered 1 to 9 (row 1: 1-3, row 2: 4-6, row 3: 7-9).
- Enter the number of the field where you want to place your O.
- Invalid input (a number outside 1-9, or an already taken field) gets rejected and asked again.
- The game ends once a row, column or diagonal is filled with the same sign, or all 9 fields are taken (draw).

## How to Run

Requires Python 3 (uses f-strings, so 3.6 or newer).

```
python tic_tac_toe.py
```

## Beyond the Course Task: The Computer's Move Logic

The original course task only asked for a computer opponent that picks a random free field. I replaced that with a simple priority logic in `draw_move`:

1. **Win if possible** – check every free field: if placing X there would win the game right away, take it.
2. **Block if necessary** – if no winning move exists, check whether the player could win on their next move, and take that field instead.
3. **Otherwise, pick randomly** – same as the original version.

For steps 1 and 2, the function temporarily places a sign on a field, checks it with the existing `victory_for` function, and reverts it if that field wasn't the one chosen — basically a one-move lookahead, no real recursion or depth search involved.

## Known Limitations

- The computer only looks one move ahead, not a full minimax search — a player could theoretically set up two threats at once and get around it.
- The computer always opens in the center, so its first random move almost always ends up two-in-a-row with it. In practice this means the computer often wins by its second move unless the player actively blocks that field early.
- Console-only, no GUI — the board is drawn with plain ASCII characters.

## Ideas for Improvement

- Full minimax logic for an unbeatable computer
- Let the player choose whether to play X or O
- More robust input handling (e.g. catching non-numeric input)
- A graphical version, e.g. with tkinter or as a small web app

## Technical Notes

A few things this project uses:

- Nested lists as a 2D structure (`board[row][col]`)
- Tuples for fixed coordinate pairs (`(row, col)`)
- Converting between the 1-9 input and row/column via `//` and `%`
- Recursion for re-asking on invalid input (`enter_move`)
- Separating game logic (functions) from flow control (main script)
- A simulate → check → revert pattern as the basis for decisions
