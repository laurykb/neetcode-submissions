class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        count = [0] * 1001
        for n in arr1:
            count[n] += 1

        res = []
        for v in arr2:
            res.extend([v] * count[v])
            count[v] = 0          # on vide pour ne pas le rajouter après

        for n in range(1001):
            res.extend([n] * count[n])
        return res