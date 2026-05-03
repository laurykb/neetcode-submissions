class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sac = set()

        for num in nums:
            if num in sac:
                return True
            sac.add(num)
        return False