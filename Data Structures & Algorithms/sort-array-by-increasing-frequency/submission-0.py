class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        res = []
        for v in sorted(count, key = lambda x: (count[x], -x)):
            res.extend([v] * count.get(v, 0))
        return res


       

        