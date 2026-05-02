class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left = i + 1 #on commence après la valeur a
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -=1   
                if threeSum < 0:
                    left += 1
                if threeSum == 0:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:  
                        left +=1
        return res
       

