class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            
            for num in numbers: 
                somme = numbers[r] + numbers[l]

            if somme == target:
                return [l + 1, r+1]
            
            if somme < target:
                l += 1
            
            if somme > target : 
                r -=1 