class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0
        res = 0

        for n in nums:
            if n - 1 not in numSet:
                longest = 1
                while n + longest in numSet:
                    longest +=1
                res = max(res, longest)
        return res

