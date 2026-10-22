class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for mot in strs:
                if i == len(mot) or mot[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]