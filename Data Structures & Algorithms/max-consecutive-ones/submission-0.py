class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        compteur = 0
        maxSeq = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                compteur +=1
                maxSeq = max(maxSeq, compteur)
            else:
                compteur = 0
        return maxSeq
            


        