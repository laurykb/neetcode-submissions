class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {}

        for n in nums:
            colors[n] = 1 + colors.get(n, 0)
        
        res = []

        for v in range(min(nums), max(nums) + 1):
            res.extend([v] * colors.get(v, 0))
        
        nums[:] = res

        return nums