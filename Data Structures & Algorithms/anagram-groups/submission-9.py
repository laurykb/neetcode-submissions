class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for mot in strs:
            count = [0] * 26
            for lettre in mot:
                count[ord(lettre) - ord('a')] +=1
            cle = tuple(count)
            if cle not in groups:
                groups[cle] = []
            groups[cle].append(mot)
        return list(groups.values())