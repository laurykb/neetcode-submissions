class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob1, rob2 = 0, 0

        for n in nums : 
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2