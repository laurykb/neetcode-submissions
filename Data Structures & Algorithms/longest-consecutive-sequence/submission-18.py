class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sac = set(nums)
        plus_longue_seq = 0

        for num in sac:
            if (num - 1) not in sac:
                longueur_seq = 1
                while (num + longueur_seq) in sac:
                    longueur_seq += 1
                plus_longue_seq = max(plus_longue_seq, longueur_seq)
        return plus_longue_seq