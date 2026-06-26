# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # bruteforce

        curr = head
        temp = []
        while curr:
            temp.append(curr.val)

            curr = curr.next
        del temp[-n]

        dummy = ListNode(0)
        curr = dummy

        for val in temp:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

