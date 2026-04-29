class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []

        q = deque([]) #va contenir les index

        l  = r = 0

        while r < len(nums):
        #on doit être sur que aucune plus petite valeur existe : q[-1] = top value
            while q and nums[q[-1]] < nums[r]:
                q.pop() #on remove la plus petite valeur
            
            q.append(r)
    # q[0] valeur la plus à gauche
            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r+= 1
        return output


        