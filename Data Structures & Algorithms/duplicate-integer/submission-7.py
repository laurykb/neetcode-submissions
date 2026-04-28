class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sac = []
        for num in nums:
            if num in sac:
                return True
            sac.append(num)
        return False


