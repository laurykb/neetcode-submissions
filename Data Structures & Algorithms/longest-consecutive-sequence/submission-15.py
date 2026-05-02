class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sac = set (nums)

        plus_longue_sequence = 0

        for num in sac:
            if (num - 1) not in sac:
                longueur_seq = 1
                while (num + longueur_seq) in sac :
                    longueur_seq += 1
                plus_longue_sequence = max(plus_longue_sequence, longueur_seq)
        return plus_longue_sequence
        