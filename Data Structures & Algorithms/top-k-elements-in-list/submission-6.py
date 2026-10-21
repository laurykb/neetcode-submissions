class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        tri = sorted(count, key = lambda n: count[n], reverse = True)

        return tri[:k]

        
