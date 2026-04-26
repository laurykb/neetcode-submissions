class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vu = set()

        for num in nums:
            if num in vu:
                return True
            vu.add(num)
        return False



