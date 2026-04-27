class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sac = {}

        for i, num in enumerate(nums):
            y = target - num
            if y in sac:
                return [sac[y], i]
            sac[num] = i