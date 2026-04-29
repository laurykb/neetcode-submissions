class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        column = set()
        positiv_diag = set()
        negativ_diag = set()
        res = []

        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in column or r+c in positiv_diag or r-c in negativ_diag:
                    continue
                column.add(c)
                negativ_diag.add(r-c)
                positiv_diag.add(r+c)
                board[r][c] = "Q"
                backtrack(r +1)

                column.remove(c)
                negativ_diag.remove(r-c)
                positiv_diag.remove(r+c)
                board[r][c] = "."

        backtrack(0)
        return res