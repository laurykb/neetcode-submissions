# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        prev_node = slow.next = None #on split les 2 listes

        #reverse la 2e partie
        while second_half:
            tmp = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = tmp
        
        first_half, second_half = head, prev_node
        while second_half:
            tmp1, tmp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = tmp1
            first_half, second_half = tmp1, tmp2



