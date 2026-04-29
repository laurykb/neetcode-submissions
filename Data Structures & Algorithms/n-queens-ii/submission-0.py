class Solution:
    def totalNQueens(self, n: int) -> int:

        res = 0
        positiv_diag = set()
        negativ_diag = set()
        column = set()

        def backtrack(r):
            if r == n:
                nonlocal res
                res+=1
                return
            
            for c in range(n):
                if c in column or (r+c) in positiv_diag or (r-c) in negativ_diag:
                    continue
                
                column.add(c)
                positiv_diag.add(r+c)
                negativ_diag.add(r-c)
                backtrack(r +1)

                column.remove(c)
                positiv_diag.remove(r+c)
                negativ_diag.remove(r-c)
        backtrack(0)
        return res



        