class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            somme_actuelle = numbers[left] + numbers[right]
            
            if somme_actuelle == target:
                return [left + 1, right + 1]
            
            if somme_actuelle > target:
                right -= 1

            if somme_actuelle < target:
                left += 1
            
        return []
        