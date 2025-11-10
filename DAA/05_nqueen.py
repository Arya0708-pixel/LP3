def solveNQueens(n: int, first_queen_col: int):
    col = set()        # Columns where queens are already placed
    posDiag = set()    # Positive diagonals (r + c)
    negDiag = set()    # Negative diagonals (r - c)

    res = []  # Stores all valid board configurations
    board = [["."] * n for _ in range(n)]  # n x n board initialized with '.'

    def backtrack(r):
        # If all queens are placed, store the board configuration
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            # Skip if column or diagonal already attacked
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # Place the queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            # Recur to place queen in next row
            backtrack(r + 1)

            # Backtrack: remove queen
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    # Place the first queen at user-specified column in row 0
    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "Q"

    # Start recursion from the 2nd row (row index 1)
    backtrack(1)
    return res


# ---------- MAIN ----------
if __name__ == "__main__":
    n = int(input("Enter number of queens (N): "))
    first_queen_col = int(input(f"Enter column (0 to {n-1}) for first queen: "))

    solutions = solveNQueens(n, first_queen_col)

    if solutions:
        print("\nOne of the possible N-Queens solutions:\n")
        for row in solutions[0]:
            print(" ".join(row))
    else:
        print("\nNo solution exists for this position.")
