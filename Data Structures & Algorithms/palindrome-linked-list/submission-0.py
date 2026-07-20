# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        words = []

        while head:
            words.append(head.val)
            head = head.next

        for i in range(len(words) // 2):
            if words[i] != words[-1 - i]:
                return False
        
        return True

        