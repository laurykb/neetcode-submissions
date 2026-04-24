class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Initialisation des deux pointeurs
        left, right = 0, len(s) - 1
        
        while left < right:
            # 1. Ignorer les caractères non alphanumériques à gauche
            if not s[left].isalnum():
                left += 1
                continue
            
            # 2. Ignorer les caractères non alphanumériques à droite
            if not s[right].isalnum():
                right -= 1
                continue
            
            # 3. Comparer les caractères en minuscule
            if s[left].lower() != s[right].lower():
                return False
            
            # 4. Avancer vers le centre
            left += 1
            right -= 1
            
        return True



            
        