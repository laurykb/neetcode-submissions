class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        resultat = max(piles)

        while left <= right:
            k = left + (right - left) //2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                resultat = min(resultat, k)
                right = k - 1
            else:
                left = k + 1
        return resultat






        