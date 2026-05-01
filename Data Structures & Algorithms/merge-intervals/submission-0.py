class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i : i[0]) # on sort par paire d'interval avec i[0] la valeur de start
        output = [intervals[0]] #on met le premier intervalle

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] #la dernière valeur du dernier intervalle ajouté

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
        