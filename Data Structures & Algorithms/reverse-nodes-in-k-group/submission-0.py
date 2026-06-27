# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        # dummy = head
        # curr = dummy
        # prev = None
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            kth_node = group_prev

            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            next_group_start = kth_node.next

            curr = group_prev.next
            prev = next_group_start

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            group_tail = group_prev.next
            group_prev.next = prev


            group_prev = group_tail
    