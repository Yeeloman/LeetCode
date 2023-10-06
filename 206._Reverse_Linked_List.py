# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ttsp
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_list = []
        current = head
        while current is not None:
            rev_list.append(current.val)
            current = current.next
        new_crnt = head
        i = len(rev_list) - 1
        while new_crnt is not None:
            new_crnt.val = rev_list[i]
            new_crnt = new_crnt.next
            i -= 1
        return head
