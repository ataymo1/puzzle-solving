# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        dummy = ListNode(0, head)

        leftPre, cur, pre = dummy, head, None

        for i in range(left - 1):
            cur, leftPre = cur.next, cur

        for i in range(right - left + 1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        leftPre.next.next = cur
        leftPre.next = pre

        return dummy.next
        






            

        