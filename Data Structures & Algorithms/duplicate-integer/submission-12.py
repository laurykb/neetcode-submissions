class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sac = set()

        for num in nums:
            if num in sac:
                return True
            else:
                sac.add(num)
        return False
