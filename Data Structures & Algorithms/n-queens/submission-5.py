class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        positiv = set()
        negativ = set()
        board = [["."] * n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in column or (r+c) in positiv or (r-c) in negativ:
                    continue

                column.add(c)
                positiv.add(r+c)
                negativ.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                column.remove(c)
                positiv.remove(r+c)
                negativ.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
            
        