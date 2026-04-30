class Solution:
    def totalNQueens(self, n: int) -> int:

        res = 0
        column = set()
        positiv = set()
        negativ = set()

        def backtrack(r):
            nonlocal res
            if r == n:  
                res+=1
                return
            
            for c in range(n):
                if c in column or (r+c) in positiv or (r-c) in negativ:
                    continue

                column.add(c)
                positiv.add(r + c)
                negativ.add(r - c)

                backtrack(r+1)

                column.remove(c)
                positiv.remove(r + c)
                negativ.remove(r - c)
        backtrack(0)
        return res

        