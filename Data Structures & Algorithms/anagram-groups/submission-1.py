from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = defaultdict(list)

        for mot in strs:
            compteur = [0] * 26
            for lettre in mot:
                index = ord(lettre) - ord('a')
                compteur[index] += 1
            cle_signature = tuple(compteur)
            groupes[cle_signature].append(mot)
        return list(groupes.values())