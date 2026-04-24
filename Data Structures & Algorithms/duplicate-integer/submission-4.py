class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        pointer = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[pointer]:
                count = count + 1
            pointer = pointer + 1
        
        if count > 0 :
            return True
        else : 
            return False


