# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hash_set =set()

        curr = head

        while curr:
            nxt = curr.next

            if nxt in hash_set:
                return True

            hash_set.add(nxt)
            curr = nxt

        return False
        