class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}
        res = set()

        for n in nums:
            count[n] = 1 + count.get(n, 0)

            if count[n] > len(nums) // 3:
                res.add(n)
        return list(res)
        
        