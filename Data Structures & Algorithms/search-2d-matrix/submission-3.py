class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False
        
        lignes = len(matrix)
        colonnes = len(matrix[0])

        left = 0
        right = (lignes * colonnes) - 1

        while left <= right:
            middle = left + (right - left) // 2

            ligne = middle // colonnes
            colonne = middle % colonnes

            value_middle = matrix[ligne][colonne]

            if value_middle > target:
                right = middle - 1
            if value_middle < target:
                left = middle + 1
            if value_middle == target:
                return True
                
        return False        