class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for pointer in range(i + 1, len(nums)):
                if nums[pointer] + nums[i] == target:
                    return [i, pointer]