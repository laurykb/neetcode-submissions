class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sac = {}

        for i, num in enumerate(nums):
            y = target - num
            if y in sac:
                return [sac[y], i] #on retroune l'index lié à la valeur y
            else:
                sac[num] = i #on assigne à l'index la valeur de chaque nombre de la liste
