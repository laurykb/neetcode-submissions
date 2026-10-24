class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        res = []

        for v in range(min(nums), max(nums) + 1):
            res.extend([v] * count.get(v, 0))
            
        return res




        
            

        
        