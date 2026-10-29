class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        
        h_to_name = {h: n for h, n in zip(heights, names)}

        return [h_to_name[h] for h in sorted(heights, reverse = True)]
