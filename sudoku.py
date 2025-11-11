#!/usr/bin/env python3
import random, copy, sys

print("Welcome to Terminal Sudoku!")

# === ASK DIFFICULTY ===
difficulty = input("Choose difficulty (easy / medium / hard) [medium]: ").strip().lower() or "medium"
if difficulty not in ("easy", "medium", "hard"):
    difficulty = "medium"

# === GENERATE FULL BOARD ===
board = [[0]*9 for _ in range(9)]

def valid_inline(b, r, c, v):
    for j in range(9):
        if b[r][j] == v: return False
    for i in range(9):
        if b[i][c] == v: return False
    br, bc = 3*(r//3), 3*(c//3)
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if b[i][j] == v: return False
    return True

def find_empty_inline(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                return i, j
    return None

def solve_inline(b):
    pos = find_empty_inline(b)
    if not pos: return True
    r, c = pos
    nums = list(range(1,10))
    random.shuffle(nums)
    for n in nums:
        if valid_inline(b, r, c, n):
            b[r][c] = n
            if solve_inline(b): return True
            b[r][c] = 0
    return False

solve_inline(board)
full_board = copy.deepcopy(board)

# === MAKE PUZZLE ===
if difficulty == "easy":
    clues = random.randint(36, 40)
elif difficulty == "medium":
    clues = random.randint(30, 35)
else:
    clues = random.randint(22, 29)

cells = [(r,c) for r in range(9) for c in range(9)]
random.shuffle(cells)
puzzle = copy.deepcopy(full_board)
for i in range(81 - clues):
    r,c = cells[i]
    puzzle[r][c] = 0

solution = copy.deepcopy(full_board)
original = copy.deepcopy(puzzle)
working = copy.deepcopy(puzzle)

# === GAME LOOP ===
while True:
    print("\nCURRENT BOARD ('.' = empty):")
    sep = "+".join(["-"*7]*3)
    for r in range(9):
        if r % 3 == 0:
            print(sep)
        row = ""
        for c in range(9):
            if c % 3 == 0: row += "| "
            v = working[r][c]
            row += (str(v) if v != 0 else ".") + " "
        row += "|"
        print(row)
    print(sep)

    # check win
    if working == solution:
        print("🎉 Congratulations — you solved it!")
        ans = input("Play again? (y/n): ").strip().lower()
        if ans == "y":
            exec(open(__file__).read())
        else:
            print("Bye!")
            sys.exit(0)

    cmd = input("Enter (row col value), or 'hint', 'solve', 'restart', 'quit': ").strip().lower()

    if cmd == "quit":
        print("Goodbye!")
        sys.exit(0)

    if cmd == "restart":
        exec(open(__file__).read())

    if cmd == "solve":
        print("SOLUTION:")
        sep = "+".join(["-"*7]*3)
        for r in range(9):
            if r % 3 == 0:
                print(sep)
            row = ""
            for c in range(9):
                if c % 3 == 0: row += "| "
                v = solution[r][c]
                row += str(v) + " "
            row += "|"
            print(row)
        print(sep)
        ans = input("Play again? (y/n): ").strip().lower()
        if ans == "y":
            exec(open(__file__).read())
        else:
            sys.exit(0)

    if cmd == "hint":
        empties = [(r,c) for r in range(9) for c in range(9) if working[r][c] == 0]
        if not empties:
            print("No empty cells left.")
            continue
        r,c = random.choice(empties)
        working[r][c] = solution[r][c]
        print(f"Hint: placed {solution[r][c]} at row {r+1}, col {c+1}.")
        continue

    parts = cmd.split()
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        r, c, v = map(int, parts)
        if not (1 <= r <= 9 and 1 <= c <= 9 and 1 <= v <= 9):
            print("Values must be 1–9.")
            continue
        r -= 1; c -= 1
        if original[r][c] != 0:
            print("Cannot change a given clue.")
            continue
        # check validity
        ok = True
        for j in range(9):
            if working[r][j] == v:
                ok = False
        for i in range(9):
            if working[i][c] == v:
                ok = False
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if working[i][j] == v:
                    ok = False
        if not ok:
            print("Invalid move — conflicts exist.")
            continue
        working[r][c] = v
        continue

    print("Unrecognized input. Example: 4 7 2 (row 4 col 7 value 2)")
