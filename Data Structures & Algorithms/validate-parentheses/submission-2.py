class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correspondance = {"]" : "[", ")" : "(", "}" : "{"}

        for c in s:
            if c in correspondance:
                if stack and stack[-1] == correspondance[c]:
                    stack.pop()
                else :
                    return False
            else :
                stack.append(c)
        return True if not stack else False
            


        