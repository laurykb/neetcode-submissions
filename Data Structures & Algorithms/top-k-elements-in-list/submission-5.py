class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countT = {}

        for num in nums:
            countT[num] = countT.get(num, 0) + 1
        
        freq = [[] * n for n in range(len(nums) + 1)]

        for num, c in countT.items():
            freq[c].append(num)
        
        res = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

